import streamlit as st
import requests

st.set_page_config(page_title="YouTube Summarizer Agent", layout="wide")

st.title("🎥 YouTube Summarizer Agent (Gemini)")
st.markdown("Enter a YouTube URL to generate a comprehensive summary.")

youtube_url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

import os

# Get backend URL from environment or default to localhost
backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")
if not backend_url.startswith("http"):
    backend_url = f"https://{backend_url}"
backend_url = backend_url.rstrip("/")

if st.button("Generate Summary", type="primary"):
    if not youtube_url:
        st.warning("Please enter a YouTube URL.")
    else:
        with st.spinner("⏳ Extracting transcript and generating summary... This may take a moment."):
            try:
                # Call the backend API
                response = requests.post(
                    f"{backend_url}/summarize",
                    json={"youtube_url": youtube_url},
                    timeout=180
                )
                
                if response.status_code == 200:
                    data = response.json()
                    summary = data.get("summary")
                    
                    st.success("Summary Generated Successfully!")
                    st.markdown("---")
                    st.markdown(summary)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Error: Could not connect to the backend server. Is it running?")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

st.markdown("---")
st.markdown("Built with **Gemini 1.5 Flash** | **LangGraph** | **FastAPI** | **Streamlit**")
