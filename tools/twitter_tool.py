import tweepy
from config import (
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

def post_tweet(text: str):
    """
    Posts `text` to your Twitter timeline.
    """
    tweet = api.update_status(status=text)
    return tweet.id_str
