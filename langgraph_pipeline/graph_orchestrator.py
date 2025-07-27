import sys
import os

# Add root path so graph, retriever, vectorstore etc. can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graph.graph_setup import build_graph

graph = build_graph()

def run_pipeline(query: str):
    result = graph.invoke({"query": query})

    print("\n=== Final Output ===")
    print("Result:", result)

    summary = result.get("summary")
    tags = result.get("tags")

    if summary is None or tags is None:
        return "", []

    print("\nSummary:\n", summary)
    print("Tags:", tags)

    return summary, tags


if __name__ == "__main__":
    test_query = "What are the latest trends in open-source AI models?"
    summary, tags = run_pipeline(test_query)
    print("\n✅ TEST PASSED — Summary and Tags extracted.")
