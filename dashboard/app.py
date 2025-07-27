import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




import streamlit as st
import json
import os
from datetime import datetime
from langgraph_pipeline.graph_orchestrator import run_pipeline  # Ensure this import is valid

st.set_page_config(page_title="🧠 AI Industry Analyst", layout="centered")

st.title("🧠 AI Industry Analyst Dashboard")
st.caption("Stay updated on the latest AI trends, curated and summarized automatically.")

# Load the latest report
report_path = "data/latest_report.json"

if not os.path.exists(report_path):
    st.error("No report found. Please run the pipeline.")
    st.stop()

with open(report_path, "r", encoding="utf-8") as f:
    report = json.load(f)

# Handle old format (list or tuple)
if isinstance(report, (list, tuple)):
    summary = report[0] if len(report) > 0 else "No summary available."
    tags = report[1] if len(report) > 1 else []
    query = "What are the latest trends in open-source AI models?"
    report = {
        "summary": summary,
        "tags": tags,
        "query": query,
        "report": f"[🧠 AI Industry Trend Report]\n\nQuery: {query}\n\nSummary:\n  {summary}\n\nTags: {', '.join(tags)}"
    }

# Run pipeline manually
if st.button("🔁 Run Analysis Now"):
    with st.spinner("Running AI trend analysis pipeline..."):
        query = "What are the latest trends in open-source AI models?"
        result = run_pipeline(query)
        if isinstance(result, dict):
            with open(report_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            st.success("✅ New report generated! Please refresh the page.")
        else:
            st.error("⚠️ Pipeline failed to return a valid result.")

# Display Summary
st.subheader("📝 Summary")
st.markdown(report.get("summary", "No summary available."))

# Display Tags
st.subheader("🏷️ Tags")
tags = report.get("tags", [])
for tag in tags:
    st.markdown(f"- #{tag}")

# Context Section
st.subheader("📰 Context Articles")
st.markdown("**🔍 Query**")
st.markdown(report.get("query", "No query available."))

# Timestamp
st.markdown(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
