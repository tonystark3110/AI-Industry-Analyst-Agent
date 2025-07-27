def report_generator_node(state: dict) -> dict:
    query = state["query"]
    summary = state["summary"]
    tags = state.get("tags", [])
    report = (
        f"[🧠 AI Industry Trend Report]\n\n"
        f"Query: {query}\n\n"
        f"Summary:\n {summary}\n\n"
        f"Tags: {', '.join(tags) if tags else 'None'}"
    )
    return {"report": report}
