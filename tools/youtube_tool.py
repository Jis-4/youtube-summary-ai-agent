from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    """
    Returns the full transcript text for a given YouTube video ID.
    """
    try:
        # Create an instance and use the fetch method
        api = YouTubeTranscriptApi()
        transcript_list = api.fetch(video_id)
        
        # The API returns FetchedTranscriptSnippet objects with .text attribute
        return " ".join(segment.text for segment in transcript_list)
            
    except Exception as e:
        return f"Error getting transcript: {str(e)}"
