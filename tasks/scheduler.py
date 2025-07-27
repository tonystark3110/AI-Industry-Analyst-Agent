import schedule
import time
from datetime import datetime
import json
import os
from langgraph_pipeline.graph_orchestrator import run_pipeline
from utils.twitter_utils import post_to_x  # Make sure your credentials are set

# Path to save the latest report
REPORT_PATH = "data/latest_report.json"

def daily_job():
    print(f"[🕒] Running daily job at {datetime.now()}")

    try:
        # Step 1: Run the AI trend analysis pipeline
        result = run_pipeline(query="What are the latest trends in open-source AI and model capabilities?")
    except Exception as e:
        print(f"[❌] Error running pipeline: {e}")
        return

    if not isinstance(result, dict) or "summary" not in result:
        print("[❌] Invalid result format from pipeline. Skipping save/post.")
        return

    # Step 2: Save the result to JSON
    try:
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[✅] Saved report to {REPORT_PATH}")
    except Exception as e:
        print(f"[❌] Error saving report: {e}")
        return

    # Step 3: Post to X
    summary = result.get("summary", "")
    tags = result.get("tags", [])
    hashtags = " ".join([f"#{tag.replace(' ', '')}" for tag in tags])

    x_post = (
        f"🧠 AI Trend Summary – {datetime.now().strftime('%b %d')}\n\n"
        f"{summary}\n\n"
        f"Tags: {hashtags}\n\n"
        f"(Auto-posted by an autonomous agent 🤖)"
    )

    try:
        post_to_x(x_post)
        print("[✅] Daily AI report posted to X.")
    except Exception as e:
        print(f"[❌] Error posting to X: {e}")

# Schedule to run daily at 9:00 AM
schedule.every().day.at("09:00").do(daily_job)
print("[INFO] Scheduler started. Running daily at 9:00 AM.")

# Run immediately for testing
daily_job()

# Keep running
while True:
    schedule.run_pending()
    time.sleep(60)
