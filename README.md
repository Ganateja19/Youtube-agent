# 🎥 YouTube Summarizer Agent (Gemini + LangGraph)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Ganateja19/Youtube-agent)

An end-to-end **AI-powered YouTube Summarizer Agent** that extracts high-quality insights from video transcripts using **Google Gemini**, **LangGraph**, **FastAPI**, and **Streamlit**.

## ✨ Features

- Accepts a **YouTube URL** as input
- Extracts text via `youtube-transcript-api`
- Generates:
  - Executive Summary
  - Key Insights
  - Actionable Takeaways
  - Detailed Breakdown
- Uses **Gemini LLM only**
- Agent orchestration with **LangGraph**
- Backend API with **FastAPI**
- Simple UI using **Streamlit**

## 🛠 Tech Stack

- **LLM**: Google Gemini (`gemini-1.5-flash`)
- **Agent Framework**: LangGraph
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Utilities**: youtube-transcript-api

## 🚀 Setup

### 1. Environment Variables
Create a `.env` file in the root directory:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 2. Backend
```bash
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
uvicorn app.main:app --reload
```

### 3. Frontend
```bash
cd frontend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
streamlit run app.py
```
