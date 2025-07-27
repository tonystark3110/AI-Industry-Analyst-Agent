# utils/twitter_utils.py

import tweepy
import os

# Load your X (Twitter) API credentials from environment variables
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

def post_to_x(text: str):
    try:
        if len(text) > 280:
            print("[⚠️] Content exceeds 280 characters, truncating.")
            text = text[:277] + "..."

        auth = tweepy.OAuth1UserHandler(
            X_API_KEY, X_API_SECRET,
            X_ACCESS_TOKEN, X_ACCESS_SECRET
        )
        api = tweepy.API(auth)
        api.update_status(text)

        print("[✅] Daily AI report posted to X.")
    except Exception as e:
        print(f"[❌] Error posting to X: {e}")
