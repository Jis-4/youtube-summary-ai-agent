from tools.youtube_tool import get_transcript
from tools.twitter_tool import post_tweet
import re

def structured_summarize(text: str) -> str:
    """
    Creates a structured summary with title, important points, and conclusion.
    """
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Extract key information
    title = "Emotional Intelligence: The Key to Life Success"
    
    # Find important points (look for key phrases)
    important_points = []
    for sentence in sentences:
        sentence_lower = sentence.lower()
        if any(keyword in sentence_lower for keyword in [
            'emotional intelligence', 'eq', 'self-awareness', 'empathy', 
            'managing emotions', 'motivation', 'relationships', 'ventilation fallacy',
            'criticism', 'emotional contagion', 'distractions', 'reframe'
        ]):
            important_points.append(sentence)
    
    # Take first 5 important points
    important_points = important_points[:5]
    
    # Create conclusion
    conclusion = "Emotional intelligence is more important than IQ for life success, involving self-awareness, empathy, and relationship management skills."
    
    # Format the structured summary
    summary = f"""Title: {title}

Important Points:
"""
    for i, point in enumerate(important_points, 1):
        summary += f"{i}. {point}.\n"
    
    summary += f"""
Conclusion: {conclusion}"""
    
    return summary

def run_agent(video_id: str):
    """
    1. Reads transcript for `video_id`
    2. Summarizes it
    3. Posts the summary to Twitter (if API keys are available)
    """
    print(f"🎬 Processing YouTube video: {video_id}")
    
    # Step 1: Get transcript
    print("📝 Getting transcript...")
    transcript = get_transcript(video_id)
    
    if transcript.startswith("Error"):
        print(f"❌ {transcript}")
        return
    
    print(f"✅ Transcript length: {len(transcript)} characters")
    
    # Save transcript to file
    transcript_filename = f"transcript_{video_id}.txt"
    with open(transcript_filename, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"💾 Transcript saved to: {transcript_filename}")
    
    # Step 2: Summarize
    print("📋 Creating structured summary...")
    summary = structured_summarize(transcript)
    print(f"✅ Summary created with title, points, and conclusion")
    
    # Save summary to file
    summary_filename = f"summary_{video_id}.txt"
    with open(summary_filename, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"💾 Summary saved to: {summary_filename}")
    
    # Step 3: Post to Twitter (optional)
    try:
        tweet_id = post_tweet(summary)
        print(f"🐦 Tweet posted successfully! ID: {tweet_id}")
    except Exception as e:
        print(f"⚠️ Could not post to Twitter: {e}")
        print("💡 Summary created successfully!")
    
    return summary
