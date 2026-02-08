from fastapi import FastAPI
from .agent import youtube_agent
from .schemas import YouTubeRequest

app = FastAPI(title="YouTube Summarizer Agent")

@app.post("/summarize")
def summarize_video(req: YouTubeRequest):
    result = youtube_agent.invoke({"youtube_url": req.youtube_url})
    return {"summary": result.get("result", "No result generated.")}
