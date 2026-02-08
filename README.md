# 🎥 YouTube Summarizer Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://youtube-agent-b7pzxe8gxihe4jacehdytf.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange)](https://deepmind.google/technologies/gemini/)
[![LangGraph](https://img.shields.io/badge/Framework-LangGraph-green)](https://langchain-ai.github.io/langgraph/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent **AI Agent** that turns long YouTube videos into concise, structured, and actionable summaries. Built with the power of **Google Gemini 2.0 Flash** and **LangGraph**.

## 🚀 Live Demo
**[Click here to try the App!](https://youtube-agent-b7pzxe8gxihe4jacehdytf.streamlit.app/)**

---

## ✨ Features
- **🔍 Transcript Extraction**: Automatically fetches video transcripts (even from videos without manual captions).
- **🧠 Intelligent Summarization**: Uses Gemini 2.0 Flash to analyze content depth through LangGraph.
- **📊 Structured Output**: Delivers:
    - 📌 Executive Summary
    - 💡 Key Insights & Highlights
    - 🛠️ Actionable Takeaways
    - 📖 Detailed Breakdown
- **⚡ Fast & Responsive**: Built on Streamlit for a smooth user experience.

## 🛠️ Tech Stack

This project leverages cutting-edge AI and web technologies:

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend UI** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) | Interactive web interface for seamless user interaction |
| **Core Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | The backbone of the application logic |
| **AI Model** | ![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white) | **Gemini 2.0 Flash** for high-speed, high-quality reasoning |
| **Agent Framework** | ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) | Orchestrates the AI workflow and state management |
| **Tools & APIs** | `youtube-transcript-api` | Robustly extracts subtitles and transcripts from YouTube |
| **Deployment** | ![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | Instant cloud hosting and continuous deployment |

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
