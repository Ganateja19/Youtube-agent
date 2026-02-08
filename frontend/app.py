import streamlit as st
import os
import google.generativeai as genai
from agent_logic import youtube_agent

# Page config
st.set_page_config(page_title="YouTube Summarizer Agent", page_icon="🎥", layout="wide")

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #CC0000;
        color: white;
    }
    .success-box {
        padding: 20px;
        background-color: #D4EDDA;
        color: #155724;
        border-radius: 10px;
        border: 1px solid #C3E6CB;
        margin-bottom: 20px;
    }
    .report-view {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎥 YouTube Summarizer Agent")
st.markdown("### 🤖 Powered by Gemini 2.0 Flash & LangGraph")
st.markdown("---")

st.info("💡 **Tip:** This agent extracts the transcript from a YouTube video and uses advanced AI to generate a structured, insightful summary.")

# Sidebar for Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("To use this app, you need a Google API Key.")
    
    # Check for API Key in Secrets (Streamlit Cloud) or Environment (Local)
    api_key = os.getenv("GOOGLE_API_KEY")
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]

    if not api_key:
        api_key_input = st.text_input("Enter Google API Key", type="password")
        if api_key_input:
            api_key = api_key_input
            os.environ["GOOGLE_API_KEY"] = api_key # Temporarily set for this session
    
    if api_key:
        st.success("✅ API Key connected")
        genai.configure(api_key=api_key)
    else:
        st.warning("⚠️ Please provide an API Key to proceed.")
        st.markdown("[Get a Gemini API Key](https://aistudio.google.com/app/apikey)")

    st.markdown("---")
    st.markdown("Created with ❤️ by **Ganateja19**")

# Main Content
youtube_url = st.text_input("🔗 Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("🚀 Generate Summary"):
    if not api_key:
        st.error("Please configure your Google API Key in the sidebar first!")
    elif not youtube_url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        with st.spinner("⏳ accessing video transcript and analysing content..."):
            try:
                # Invoke the agent
                payload = {"youtube_url": youtube_url}
                # Using the imported agent logic directly
                from agent_logic import youtube_agent 
                # Re-import to ensure fresh execution context if needed, though top-level is fine
                
                result = youtube_agent.invoke(payload)
                summary = result.get("result", "No result returned.")
                
                if "Error extracting transcript" in summary or "Error generating summary" in summary:
                     st.error(summary)
                else:
                    st.balloons()
                    st.markdown('<div class="success-box">✅ Summary Generated Successfully!</div>', unsafe_allow_html=True)
                    
                    with st.expander("📄 View Transcript Snippet", expanded=False):
                        st.text("Transcript processing completed...")
                    
                    st.markdown("### 📝 Video Summary")
                    st.markdown(f'<div class="report-view">{summary}</div>', unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
