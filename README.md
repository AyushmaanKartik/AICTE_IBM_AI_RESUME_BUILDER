# AI Resume Builder (Firebase Deployment)

This project is a single-page web application that uses HTML, Tailwind CSS, and plain JavaScript to interface with the **Google Gemini API** for generating professional resumes in Markdown format. The application is designed to be deployed using **Firebase Hosting**.

## 🛠️ Project Setup and Local Run

1.  **Clone the Repository**
    ```bash
    git clone [Your-Repo-URL]
    cd [Your-Repo-Name]
    ```
2.  **Get Your API Key**
    Obtain a **Gemini API Key** from [Google AI Studio].
3.  **Insert Key**
    Open `index.html` and replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual key in the `<script>` section.
4.  **Run Locally**
    You can open `index.html` directly in your web browser to test it.

## 🚀 Deployment on Firebase Hosting

To deploy this static application:

1.  **Install Firebase CLI**
    ```bash
    npm install -g firebase-tools
    ```
2.  **Log In**
    ```bash
    firebase login
    ```
3.  **Initialize Project (in the project root directory)**
    ```bash
    firebase init
    ```
    * Select **"Hosting: Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys."**
    * Choose an existing project or create a new one.
    * Specify the **public directory** as `.` (a single dot, since `index.html` is in the root).
    * Configure as a single-page app: **No**.
4.  **Deploy**
    ```bash
    firebase deploy --only hosting
    ```
    The application will be live at the provided Firebase Hosting URL.
