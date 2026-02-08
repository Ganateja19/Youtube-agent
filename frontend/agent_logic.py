import os
from langgraph.graph import StateGraph
import google.generativeai as genai
from dotenv import load_dotenv
from youtube_utils import extract_transcript_from_url
from typing import TypedDict

# Configure GenAI
# Note: In Streamlit Cloud, keys should be accessed via st.secrets, but for local dev we use os.getenv
# We will handle the fallback in the main app.py, but here we assume genai is configured or we configure it if key is present.
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Use the fixed model name
model = genai.GenerativeModel("gemini-2.0-flash-001")

class AgentState(TypedDict):
    youtube_url: str
    result: str

def summarize_node(state: AgentState):
    youtube_url = state["youtube_url"]
    try:
        transcript_text = extract_transcript_from_url(youtube_url)
    except Exception as e:
        return {"result": f"Error extracting transcript: {str(e)}"}

    prompt = f"""
You are an expert video content analyst.

Generate a comprehensive summary for the following YouTube video transcript:

1. **Title & Topic Overview**: What is the video about?
2. **Executive Summary**: High-level summary of the content (3-5 sentences).
3. **Key Insights & Highlights**: Bullet points of the most important information.
4. **Actionable Takeaways**: Practical advice or steps mentioned in the video.
5. **Detailed Breakdown**: A structured summary of the main sections.

Transcript Content:
{transcript_text[:25000]}
"""

    try:
        response = model.generate_content(prompt)
        return {"result": response.text}
    except Exception as e:
        return {"result": f"Error generating summary: {str(e)}"}

# Compile the graph
graph = StateGraph(AgentState)
graph.add_node("summarize", summarize_node)
graph.set_entry_point("summarize")
graph.set_finish_point("summarize")
youtube_agent = graph.compile()
