# YouTube Summary AI Agent

A Python-based AI agent that automatically extracts transcripts from YouTube videos, creates structured summaries, and optionally posts them to Twitter.

## 🚀 Features

- **YouTube Transcript Extraction**: Automatically extracts transcripts from any YouTube video with captions
- **Structured Summarization**: Creates professional summaries with title, important points, and conclusion
- **File Generation**: Saves both full transcripts and summaries as text files
- **Twitter Integration**: Optional posting to Twitter (requires API keys)
- **Free & Open Source**: No paid API keys required for core functionality

## 📋 Requirements

- Python 3.8+
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/youtube-summary-ai-agent.git
   cd youtube-summary-ai-agent
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\Activate.ps1
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Enter a YouTube URL when prompted:**
   ```
   Enter YouTube URL or ID: https://youtu.be/n6MRsGwyMuQ?si=example
   ```

3. **View the results:**
   - Transcript saved as: `transcript_{video_id}.txt`
   - Summary saved as: `summary_{video_id}.txt`

## 📁 Project Structure

```
youtube-summary-ai-agent/
├── agent/
│   └── summarizer_agent.py    # Main AI agent logic
├── tools/
│   ├── youtube_tool.py        # YouTube transcript extraction
│   └── twitter_tool.py        # Twitter posting functionality
├── config.py                  # Configuration and environment variables
├── main.py                    # Main application entry point
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root for Twitter integration:

```env
# Twitter API Keys (optional)
TWITTER_API_KEY=your_twitter_api_key_here
TWITTER_API_SECRET=your_twitter_api_secret_here
TWITTER_ACCESS_TOKEN=your_twitter_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret_here
```

## 📊 Example Output

### Input
```
YouTube URL: https://youtu.be/n6MRsGwyMuQ?si=example
```

### Generated Files

**transcript_n6MRsGwyMuQ.txt:**
```
Daniel Goleman argues that IQ isn't everything our current view of intelligence is too narrow...
[Full transcript content]
```

**summary_n6MRsGwyMuQ.txt:**
```
Title: Emotional Intelligence: The Key to Life Success

Important Points:
1. Daniel Goleman argues that IQ isn't everything - EQ (Emotional Intelligence) is the superior metric for life success
2. The ventilation fallacy - venting anger prolongs mood rather than ending it
3. Managing anger through deep breaths, walking, and reframing thoughts
4. Breaking negative thought cycles with distractions and reframing
5. Practical strategies for emotional management

Conclusion: Emotional intelligence is more important than IQ for life success, involving self-awareness, empathy, and relationship management skills.
```

## 🛠️ Dependencies

- `youtube-transcript-api`: YouTube transcript extraction
- `tweepy`: Twitter API integration
- `python-dotenv`: Environment variable management
- `langchain`: AI framework (for future enhancements)
- `openai`: OpenAI integration (for future enhancements)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [Tweepy](https://github.com/tweepy/tweepy) for Twitter integration
- [LangChain](https://github.com/langchain-ai/langchain) for AI framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/youtube-summary-ai-agent/issues) page
2. Create a new issue with detailed information
3. Include the YouTube URL and error messages

## 🔮 Future Enhancements

- [ ] Support for multiple video processing
- [ ] Advanced AI-powered summarization
- [ ] Web interface
- [ ] Support for other social media platforms
- [ ] Video thumbnail extraction
- [ ] Multi-language support

---

**Made with ❤️ for the AI community** 