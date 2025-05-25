from langchain.vectorstores import FAISS

def build_retriever_from_texts(texts, embedder):
    db = FAISS.from_texts(texts, embedder)
    return db.as_retriever(), db