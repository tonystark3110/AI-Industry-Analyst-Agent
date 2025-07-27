import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_DIR = "vectorstore/db"

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = FAISS.load_local(DB_DIR, embedding_model, allow_dangerous_deserialization=True)

def retrieve_relevant_chunks(query: str, k: int = 4):
    docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]
