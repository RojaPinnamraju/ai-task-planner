# AI Agent Chatbot with FastAPI & Modern Frontend

This project is a full-stack AI chatbot application using a FastAPI backend and a modern static HTML/JS frontend. The backend integrates with Groq and Tavily APIs for LLM and search capabilities. The frontend is designed for easy deployment on Netlify, while the backend is ready for Render or similar cloud platforms.

---

## Features
- **FastAPI** backend with CORS enabled
- **LLM integration** (Groq, Tavily)
- **Modern, responsive frontend** (HTML/CSS/JS)
- **Markdown-formatted AI responses**
- **Environment variable support** for API keys
- **Easy deployment**: Backend on Render, frontend on Netlify

---

## Project Structure
```
├── ai_agent.py         # Core AI agent logic
├── backend.py          # FastAPI backend API
├── index.html          # Frontend (static, deploy to Netlify)
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore secrets, venv, etc.
├── Pipfile / Pipfile.lock (optional)
└── Readme.md           # This file
```

---

## Local Development

### 1. Backend (FastAPI)
1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```
4. **Run the backend:**
   ```bash
   python backend.py
   ```
   The API will be available at `http://127.0.0.1:10000` (or as configured).

### 2. Frontend (Static HTML/JS)
- Open `index.html` directly in your browser for local testing.
- **For production:** Deploy to Netlify (see below).

---

## Deployment

### Backend (Render)
1. Push your code to GitHub.
2. On [Render](https://dashboard.render.com/):
   - New Web Service → Connect repo
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend:app --host 0.0.0.0 --port 10000`
   - **Port:** `10000`
   - Add environment variables (`GROQ_API_KEY`, `TAVILY_API_KEY`)
3. Deploy and note your public backend URL (e.g., `https://your-backend.onrender.com`).

### Frontend (Netlify)
1. Place `index.html` (and any assets) in a folder (e.g., `frontend-dist`).
2. In `index.html`, set:
   ```js
   const API_URL = 'https://your-backend.onrender.com/chat';
   ```
3. Push to GitHub.
4. On [Netlify](https://app.netlify.com/):
   - New site from Git → Connect repo
   - Set publish directory to your frontend folder
   - Deploy
5. Your site will be live at `https://your-frontend.netlify.app`.

---

## API Usage
- **POST** `/chat`
  - Request body:
    ```json
    {
      "model_name": "llama-3.3-70b-versatile",
      "model_provider": "Groq",
      "system_prompt": "act as a teacher",
      "messages": ["What is Python programming?"],
      "allow_search": true
    }
    ```
  - Response:
    ```json
    { "response": "...AI response..." }
    ```

---
