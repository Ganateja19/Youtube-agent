from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str) -> str:
    """
    Extracts the video ID from a YouTube URL.
    Supports formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    """
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            p = parse_qs(parsed_url.query)
            return p['v'][0]
    raise ValueError("Invalid YouTube URL")

def extract_transcript_from_url(youtube_url: str) -> str:
    try:
        video_id = extract_video_id(youtube_url)
        # Fetch the transcript using instance-based API
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        
        # Combine the transcript text from snippets
        transcript_text = ""
        # The transcript is a FetchedTranscript object containing snippets
        for snippet in transcript.snippets:
            transcript_text += snippet.text + " "
            
        return transcript_text.strip()
    except Exception as e:
        raise Exception(f"Failed to extract transcript: {str(e)}")
