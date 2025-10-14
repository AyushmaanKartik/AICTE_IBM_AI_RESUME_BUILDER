# 🧠 AI Resume Builder

An **AI-powered resume generator** that instantly creates professional, ATS-friendly resumes using **Google Gemini API** and a modern **Python + TailwindCSS** interface.

Built for simplicity, speed, and accuracy — just enter your details and get a complete, editable resume with one click.

---

## 🚀 Features

* 🤖 **AI-Powered Resume Generation** – Automatically creates polished resumes using the Gemini API based on your raw input.
* 📝 **Inline Editing** – Edit and refine the generated resume content directly within the browser before exporting.
* 🧾 **PDF Export** – Generates a clean, professional, print-ready PDF layout via the browser's native print function.
* 🎨 **Responsive UI** – Modern, minimal, and mobile-friendly design built with **TailwindCSS**.
* 🔒 **Environment Secure** – Safely handles the API key via a **FastAPI backend** using a `.env` file, protecting it from client-side exposure.

---

## 🧩 Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | **Python (FastAPI)** | Provides a fast, asynchronous API endpoint to securely handle the Gemini key. |
| **Frontend** | HTML5, TailwindCSS, JavaScript | A modern, responsive interface for input and display. |
| **AI Model** | **Google Gemini 1.5 / 2.0 Flash** | The large language model responsible for generating and formatting the resume content. |
| **PDF Export** | Browser-Native | Relies on the browser's print-to-PDF functionality for high-quality document saving. |
| **Version Control** | Git & GitHub | Used for source control and collaboration. |

---

## ⚙️ Installation & Setup

This project requires both the Python backend (FastAPI) and a local frontend server (for `index.html`) to run concurrently.

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/AI-Resume-Builder.git
cd AI-Resume-Builder
````

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

You must provide your Gemini API key for the backend to function.

1.  Obtain your key from the [Google AI Studio documentation](https://ai.google.dev).

2.  Create a file named **`.env`** in the root directory.

3.  Add your key inside the file, following the format in `.env.example`:

    ```bash
    GEMINI_API_KEY=your_google_gemini_api_key_here
    ```

### 4️⃣ Run the Backend Server (Terminal 1)

This starts the FastAPI server which handles the secure AI calls.

```bash
uvicorn app:app --reload
```

The API will be available at 👉 **`http://localhost:8000`**

### 5️⃣ Open the Frontend UI (Terminal 2)

Open a **second terminal** window in the same directory and use Python's simple HTTP server to serve the `index.html` file.

```bash
python -m http.server 8080
```

Now open your web browser and navigate to the frontend: 👉 **`http://localhost:8080`**

-----

## 🧠 API Endpoint Details

The frontend sends user data to this single endpoint for processing.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/api/generate` | Sends user resume data to the Gemini API and returns the Markdown-formatted resume content. |

### Sample Request Payload

```json
{
  "fullName": "Jane Doe",
  "contactInfo": "jane@ex.com | (555) 123-4567 | Miami",
  "targetRole": "Software Engineer",
  "summary": "Results-driven developer skilled in AI & cloud technologies.",
  "experience": "Worked on chatbots, SaaS platforms, and automation tools.",
  "education": "B.Sc. Computer Science, Penn State University",
  "skills": "Python, React, TensorFlow, FastAPI"
}
```

### Sample Successful Response

```json
{
  "markdown": "# Jane Doe\njane@ex.com | (555) 123-4567 | Miami\n\n## Professional Summary\nResults-driven developer skilled in AI & cloud technologies.\n\n## Experience\n* Developed AI chatbots for multiple clients.\n* Improved automation systems by 30%.\n\n## Education\nB.Sc. Computer Science, Penn State University\n\n## Skills\n* Python\n* FastAPI\n* React\n* TensorFlow"
}
```

-----

## 📁 File Structure

```
📦 AI-Resume-Builder/
│
├── app.py              # Backend (FastAPI API)
├── index.html          # Frontend UI (TailwindCSS + JS)
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── README.md           # This documentation file
└── Screenshot.png      # Demo screenshot
```

> 💡 All files are placed in the root directory for **easy setup and grading**, ensuring both frontend and backend run without additional path configuration.

-----

## 🧾 Usage Guide

1.  Ensure both the **FastAPI backend** (`:8000`) and the **Frontend server** (`:8080`) are running.
2.  Fill out your details in the input fields on the left panel.
3.  Click the **Generate Resume** button. The frontend sends the data to the FastAPI API, which then calls Gemini.
4.  The generated content appears on the right panel, where it can be edited.
5.  Click **Save as PDF** to export the final document.

-----

## 📸 Screenshot

-----

## 🧭 Future Scope

  * **🌐 Integration:** Add LinkedIn and Indeed integration for auto-fill functionality.
  * **🧠 Templates:** Include multiple AI-suggested resume templates (Modern, Minimalist, Corporate).
  * **💾 Data Management:** Implement functionality to save and manage previous resumes locally or in the cloud.
  * **🗣️ Language Support:** Add multilingual resume generation support.
  * **🧩 Job Matching:** Integrate AI-driven job-matching and keyword optimization suggestions.

-----

## 🛡️ License

This project is licensed under the **[MIT License](https://www.google.com/search?q=LICENSE)**.
You can freely use, modify, and distribute it with proper attribution.

-----

## ✨ Acknowledgments

  * [Google Gemini API](https://ai.google.dev) for the powerful AI model.
  * [TailwindCSS](https://tailwindcss.com) for the sleek, responsive UI.
  * [FastAPI](https://fastapi.tiangolo.com) for the fast, async backend.

-----

## 👩‍💻 Author

**Developed by:** *Ayushmaan Kartik*

-----

⭐ *If you found this project helpful, please give it a star on GitHub\!*

```
```
