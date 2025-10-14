import os
import json
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv

# Load env (works even if uvicorn is started from another folder)
load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# You can set the exact model name returned by /v1beta/models here, e.g.:
# models/gemini-2.0-flash  or  models/gemini-2.0-pro-exp  etc.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "models/gemini-2.0-flash")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing. Put it in backend/.env")

def gemini_url_for(model_name: str) -> str:
    # v1beta endpoint + model resource name
    return f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent"

GEMINI_URL = gemini_url_for(GEMINI_MODEL)

app = FastAPI(title="AI Resume Builder Backend")

# CORS (tighten in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # e.g. ["http://localhost:8080", "https://your-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    fullName: str
    contactInfo: str
    targetRole: str
    summary: str | None = ""
    experience: str
    education: str
    skills: str

SYSTEM_PROMPT = (
    "You are a world-class professional resume writer. Generate a polished, modern, "
    "high-impact resume in clear Markdown only (no extra prose before/after). "
    "Rules:\n"
    "1) Use '# ' for the full name.\n"
    "2) Use '## ' for section headers (Professional Summary, Experience, Education, Skills).\n"
    "3) Use '*' bullets for achievements and skills.\n"
    "4) Use strong action verbs, quantify results, ensure ATS-friendly keywords, inclusive language.\n"
    "5) Keep it concise and professional.\n"
)

def clamp(txt: str | None, n: int) -> str:
    if not txt:
        return ""
    return txt if len(txt) <= n else (txt[:n] + "…")

@app.get("/health")
def health():
    return {"ok": True, "model": GEMINI_MODEL}

@app.get("/models")
async def list_models():
    """
    Lists models available to your API key. Use one of the exact `name` values
    returned here as GEMINI_MODEL in your .env (e.g., models/gemini-2.0-flash).
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models"
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.get(url, params={"key": GEMINI_API_KEY})
            r.raise_for_status()
            return r.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate")
async def generate_resume(user: UserData):
    # Clamp inputs to keep prompts lean and avoid token overflow
    user = UserData(
        fullName=clamp(user.fullName, 120),
        contactInfo=clamp(user.contactInfo, 300),
        targetRole=clamp(user.targetRole, 160),
        summary=clamp(user.summary or "", 1200),
        experience=clamp(user.experience, 4000),
        education=clamp(user.education, 1200),
        skills=clamp(user.skills, 1200),
    )

    user_query = (
        "Generate a resume. Candidate data:\n"
        f"Full Name: {user.fullName}\n"
        f"Contact Information: {user.contactInfo}\n"
        f"Target Role: {user.targetRole}\n"
        f"Professional Summary: {user.summary}\n"
        f"Work Experience: {user.experience}\n"
        f"Education: {user.education}\n"
        f"Key Skills: {user.skills}\n"
    )

    payload = {
        # Top-level system instruction (snake_case per API spec)
        "system_instruction": { "parts": [ { "text": SYSTEM_PROMPT } ] },
        # User message with explicit role
        "contents": [ {
            "role": "user",
            "parts": [ { "text": user_query } ]
        } ],
        # Leave out response_mime_type (some endpoints reject markdown);
        # model still outputs Markdown-style text.
        "generation_config": {
            "temperature": 0.4,
            "max_output_tokens": 2048
        }
    }

    headers = { "Content-Type": "application/json" }
    params = { "key": GEMINI_API_KEY }

    try:
        async with httpx.AsyncClient(timeout=90) as client:
            r = await client.post(GEMINI_URL, headers=headers, params=params, json=payload)
            if r.status_code == 404:
                # Helpful hint: user likely needs to change GEMINI_MODEL to one from /models
                raise HTTPException(
                    status_code=502,
                    detail=(
                        "Model not found for this API version. "
                        "Set GEMINI_MODEL to one of the names from GET /models. "
                        f"Requested: {GEMINI_MODEL}. Provider says: {r.text}"
                    )
                )
            r.raise_for_status()
            data = r.json()

            # Robust parsing: grab first text part
            markdown = None
            candidates = data.get("candidates") or []
            if candidates:
                parts = (candidates[0].get("content") or {}).get("parts") or []
                for p in parts:
                    if isinstance(p, dict) and "text" in p:
                        markdown = p["text"]
                        break

            if not markdown:
                raise HTTPException(status_code=502, detail=f"Empty/malformed response: {json.dumps(data)}")

            return { "markdown": markdown }

    except httpx.HTTPStatusError as e:
        # Bubble up the provider error JSON so you can see exactly what it didn’t like
        try:
            provider_detail = e.response.text
        except Exception:
            provider_detail = str(e)
        raise HTTPException(status_code=502, detail=f"Model request failed: {provider_detail}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}") from e
