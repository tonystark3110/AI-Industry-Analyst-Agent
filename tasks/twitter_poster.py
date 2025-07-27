import tweepy
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

consumer_key = os.getenv("X_CONSUMER_KEY")
consumer_secret = os.getenv("X_CONSUMER_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def post_to_x(content: str):
    try:
        if len(content) > 280:
            print("[⚠️] Content exceeds 280 characters, truncating.")
            content = content[:277] + "..."
        api.update_status(content)
        print("[✅] Tweet posted successfully.")
    except Exception as e:
        print("[❌] Error posting to X:", e)
