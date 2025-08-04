import re
from agent.summarizer_agent import run_agent

def extract_video_id(url: str) -> str:
    """
    Very simple extractor for YouTube IDs.
    """
    # handles URLs like https://www.youtube.com/watch?v=VIDEOID
    m = re.search(r"v=([^&]+)", url)
    if m:
        return m.group(1)
    # handles URLs like https://youtu.be/VIDEOID
    m = re.search(r"youtu\.be/([^?]+)", url)
    if m:
        return m.group(1)
    # fallback: assume the URL *is* the ID
    return url

if __name__ == "__main__":
    url = input("Enter YouTube URL or ID: ").strip()
    video_id = extract_video_id(url)
    run_agent(video_id)
