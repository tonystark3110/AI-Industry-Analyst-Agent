from langgraph.graph import StateGraph, END
from typing import TypedDict
from retriever.rag_retriever import retrieve_relevant_chunks
from nodes.summarize import summarize_node
from nodes.classify import classify_node
from nodes.report_generator import report_generator_node

class RAGState(TypedDict):
    query: str
    contexts: list[str]
    summary: str
    tags: list[str]     # ✅ new
    report: str

def build_graph():
    builder = StateGraph(RAGState)

    builder.add_node("retrieve", lambda state: {"contexts": retrieve_relevant_chunks(state["query"])} )
    builder.add_node("summarize", summarize_node)
    builder.add_node("classify", classify_node)
    builder.add_node("generate_report", report_generator_node)  # ✅ renamed from 'report'

    builder.set_entry_point("retrieve")
    builder.add_edge("retrieve", "summarize")
    builder.add_edge("summarize", "classify")
    builder.add_edge("classify", "generate_report")  # ✅ updated
    builder.add_edge("generate_report", END)         # ✅ updated

    return builder.compile()
