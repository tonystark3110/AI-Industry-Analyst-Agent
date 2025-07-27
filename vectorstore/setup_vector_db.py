import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_DIR = "data/articles"
DB_DIR = "vectorstore/db"

def chunk_and_embed_articles():
    print("[📄] Loading articles...")
    docs = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt") or filename.endswith(".md"):
            loader = TextLoader(os.path.join(DATA_DIR, filename))
            docs.extend(loader.load())

    print(f"[🔍] Loaded {len(docs)} documents. Chunking...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    print("[🔢] Embedding and storing to FAISS DB...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectorstore = FAISS.from_documents(chunks, embedding_model)

    os.makedirs(DB_DIR, exist_ok=True)
    vectorstore.save_local(DB_DIR)
    print("[✅] FAISS DB saved to vectorstore/db")

if __name__ == "__main__":
    chunk_and_embed_articles()
