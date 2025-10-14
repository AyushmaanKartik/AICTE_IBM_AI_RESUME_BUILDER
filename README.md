# 🧠 AI Resume Builder

A modern web app that uses Google's **Gemini API** to generate professional, AI‑written resumes automatically from user input.

---

## 📁 Project Structure

```
AI-Resume-Builder/
│
├── backend/
│   ├── app.py              # FastAPI backend (Gemini API handler)
│   ├── requirements.txt    # Backend dependencies
│   ├── .env.example        # Example env file (no real key)
│   └── .gitignore          # Ignore venv and secrets
│
├── frontend/
│   └── index.html          # Frontend with Tailwind & fetch API
│
└── README.md               # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/<your-username>/AI-Resume-Builder.git
cd AI-Resume-Builder
```

### 2. Backend setup

```bash
cd backend
python -m venv venv
# Activate
venv\Scripts\activate   # on Windows
# or
source venv/bin/activate  # on macOS/Linux

pip install -r requirements.txt
```

### 3. Configure `.env`

Create a file named `.env` inside the `backend` folder:

```env
GEMINI_API_KEY=your_google_api_key_here
GEMINI_MODEL=models/gemini-2.0-flash
```

> You can also copy `.env.example` and rename it to `.env`.

### 4. Run the backend

```bash
uvicorn app:app --reload --port 8000
```

Now visit: [http://localhost:8000/docs](http://localhost:8000/docs)

You can test it with:

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
        "fullName":"Jane Doe",
        "contactInfo":"jane@example.com · 555-1234",
        "targetRole":"Software Engineer",
        "summary":"Enthusiastic developer...",
        "experience":"Company A 2020–Present - Built systems",
        "education":"B.Tech 2020",
        "skills":"Python, React, SQL"
      }'
```

---

### 5. Frontend setup

You can open the `frontend/index.html` directly or run a local web server:

```bash
cd frontend
python -m http.server 8080
```

Open your browser: [http://localhost:8080](http://localhost:8080)

Make sure your backend is running on port 8000 and the line below exists in `index.html`:

```js
const BACKEND_URL = "http://localhost:8000/api/generate";
```

---

## 🌐 API Overview

**Base URL:** `http://localhost:8000`

| Endpoint        | Method | Description                                   |
| --------------- | ------ | --------------------------------------------- |
| `/health`       | GET    | Check backend and model health                |
| `/models`       | GET    | List Gemini models available for your API key |
| `/api/generate` | POST   | Generate a resume in Markdown                 |

### `/api/generate` request body

```json
{
  "fullName": "John Doe",
  "contactInfo": "john@example.com",
  "targetRole": "Data Scientist",
  "summary": "Results-driven analyst...",
  "experience": "Google 2020–2023...",
  "education": "MIT 2016–2020",
  "skills": "Python, TensorFlow, SQL"
}
```

Response:

```json
{
  "markdown": "# John Doe\n## Professional Summary\n..."
}
```

---

## 🖨️ Exporting PDF

Click **Save as PDF** in the web app — print settings are optimized for both **A4** and **US Letter** formats.

---

## 🧩 Requirements

```
fastapi
uvicorn
httpx
python-dotenv
pydantic
```

---

## 🔒 Environment & Security

* **Never commit your `.env` file.**
* Only share `.env.example`.
* Gemini API key must be added manually by the grader.

---

## 🚀 Optional Deployment

You can deploy the backend to **Render**, **Railway**, or **Heroku** easily.

**Procfile:**

```
web: uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}
```

**render.yaml:**

```yaml
services:
  - type: web
    name: ai-resume-backend
    env: python
    plan: free
    buildCommand: pip install -r backend/requirements.txt
    startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
    rootDir: backend
    envVars:
      - key: GEMINI_API_KEY
        sync: false
      - key: GEMINI_MODEL
        value: models/gemini-2.0-flash
```

---

## 🧭 Future Enhancements

* Dark theme toggle
* Multiple resume templates
* Cloud save (Firebase or Google Drive)
* Export to DOCX

---

## 📄 License

MIT © 2025
Developed for educational and research purposes.
