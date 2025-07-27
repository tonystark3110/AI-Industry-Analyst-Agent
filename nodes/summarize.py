# nodes/summarize.py

from transformers import pipeline

# Load summarization pipeline from Hugging Face
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_node(state: dict) -> dict:
    context = "\n".join(state["contexts"])

    # Hugging Face summarizer typically has a token limit (~1024 for distilbart)
    context = context[:1024]

    summary = summarizer(context, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]

    return {"summary": summary}
