from transformers import pipeline
from typing import Dict

# Load zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define candidate labels
CANDIDATE_LABELS = [
    "open-source", "multimodal", "agentic", "LLM eval", "LLM infra",
    "robotics", "healthcare AI", "genAI tools", "AI policy"
]

def classify_node(state: Dict) -> Dict:
    summary = state["summary"]
    result = classifier(summary, CANDIDATE_LABELS, multi_label=True)
    top_labels = [label for label, score in zip(result["labels"], result["scores"]) if score > 0.4]
    return {"tags": top_labels}
