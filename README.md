# 🎥 YouTube Summarizer Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://youtube-agent-b7pzxe8gxihe4jacehdytf.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange)](https://deepmind.google/technologies/gemini/)
[![LangGraph](https://img.shields.io/badge/Framework-LangGraph-green)](https://langchain-ai.github.io/langgraph/)

An intelligent **AI Agent** that turns long YouTube videos into concise, structured, and actionable summaries. Built with the power of **Google Gemini 2.0 Flash** and **LangGraph**.

## 🚀 Live Demo
**[Click here to try the App!](https://youtube-agent-b7pzxe8gxihe4jacehdytf.streamlit.app/)**

---

## ✨ Features
- **🔍 Transcript Extraction**: Automatically fetches video transcripts (even from videos without manual captions).
- **🧠 Intelligent Summarization**: Uses Gemini 2.0 Flash to analyze content depth.
- **📊 Structured Output**: Delivers:
    - 📌 Executive Summary
    - 💡 Key Insights & Highlights
    - 🛠️ Actionable Takeaways
    - 📖 Detailed Breakdown
- **⚡ Fast & Responsive**: Built on Streamlit for a smooth user experience.

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM**: [Google Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/)
- **Agent Framework**: [LangGraph](https://langchain-ai.github.io/langgraph/)
- **Transcript Tool**: `youtube-transcript-api`

## 📦 Local Installation

If you want to run this locally:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Ganateja19/Youtube-agent.git
    cd Youtube-agent
    ```

2.  **Install Dependencies**:
    Requires Python 3.9+
    ```bash
    pip install -r frontend/requirements.txt
    ```

3.  **Set up Environment**:
    Create a `.env` file in the root directory:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    ```

4.  **Run the App**:
    ```bash
    streamlit run frontend/app.py
    ```

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a Pull Request.

---
*Created by [Ganateja19](https://github.com/Ganateja19)*
