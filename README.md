# 🧠 AI Industry Analyst Agent

A LangGraph-powered AI agent that tracks breaking trends in the AI industry, performs RAG-based summarization, classifies trend tags, and delivers daily reports via dashboard or X (Twitter).

## 🔧 Features
- 📰 Fetches latest AI news articles
- 🔍 Embeds and stores in FAISS vector database
- 🧠 RAG-based summarization with LLMs
- 🏷️ Zero-shot classification of AI trends (e.g., open-source, multimodal)
- 📊 Streamlit dashboard to view reports & manually trigger pipeline
- 🕒 Daily scheduler for full autonomous updates



## This agent can post trend summaries daily to your X (formerly Twitter) account.

To enable:

Go to developer.twitter.com and create a developer app.

Generate these keys:

API Key

API Secret

Access Token

Access Token Secret

Create a file secrets_twitter.py at the project root:

python
Copy
Edit
# secrets_twitter.py
TWITTER_API_KEY = "your_key"
TWITTER_API_SECRET = "your_secret"
TWITTER_ACCESS_TOKEN = "your_token"
TWITTER_ACCESS_SECRET = "your_token_secret"
Done! Now every daily job (via scheduler) will post your AI trend report automatically to your X feed.

Sample output:

less
Copy
Edit
🧠 AI Industry Trend Report

Summary:
Meta open-sources a new multimodal AI model with vision + text capabilities.

Tags: #open-source #multimodal #agentic


## 📸 Demo
![dashboard-screenshot](path/to/screenshot.png)

## 🚀 Run Locally

```bash
git clone https://github.com/yourusername/ai-industry-analyst.git
cd ai-industry-analyst
pip install -r requirements.txt
streamlit run dashboard/app.py

## 🚀 Demo

### 📊 Streamlit Dashboard

```bash
streamlit run dashboard/app.py

⏱ Scheduled Daily Pipeline
```bash

python tasks/scheduler.py
Runs the full end-to-end pipeline once daily (simulated if needed).

🧠 Powered By
LangGraph

LangChain

FAISS

HuggingFace Embeddings

Streamlit

[Claude / GPT API](https://www.anthropic.com/ or https://openai.com/)

X (Twitter) API (optional)

📌 Features
✅ Automated RAG (Retrieval-Augmented Generation)

✅ LLM-based summarization + zero-shot classification

✅ Vector DB updates daily

✅ Streamlit dashboard with manual trigger

✅ Optional posting to X (Twitter)

✅ Modular and scalable architecture



🙋‍♂️ Author
Manikandan Meenakshi Sundaram
🚀 AI Research & Analytics | Data Science | LLMs | Autonomous Agents
📍 Boston, MA
🔗 LinkedIn | Portfolio (optional)


