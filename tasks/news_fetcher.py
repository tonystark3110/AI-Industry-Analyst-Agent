import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

DATA_DIR = "data/articles"

def fetch_and_vectorize_articles():
    print("[📡] Fetching AI news articles...")

    # Dummy articles for testing
    articles = [
        {
            "title": "Meta open-sources new multimodal model",
            "content": "Meta has released a new open-source multimodal AI model that supports both vision and text input.",
        },
        {
            "title": "OpenAI partners with Reddit to train models",
            "content": "OpenAI has entered into a partnership with Reddit to use public posts for training future GPT models.",
        },
    ]

    os.makedirs(DATA_DIR, exist_ok=True)

    for idx, article in enumerate(articles):
        filename = f"{DATA_DIR}/article_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(article["title"] + "\n" + article["content"])

    return articles  # ✅ RETURN ARTICLES!
