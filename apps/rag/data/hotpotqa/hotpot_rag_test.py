import os
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from hotpotqa.hotpot_loader import load_hotpotqa_documents
import json

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "mistral")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

print("📚 Loading HotpotQA test set...")
docs = load_hotpotqa_documents("hotpotqa/hotpot_sample.json")

print("🔍 Creating vector DB...")
embedder = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
db = FAISS.from_documents(docs, embedder)

print("🧠 Running RAG pipeline on sample questions...")
with open("hotpotqa/hotpot_sample.json", "r") as f:
    data = json.load(f)

llm = Ollama(model=MODEL_NAME)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

for i, entry in enumerate(data):
    question = entry["question"]
    expected = entry["answer"]
    print(f"\n--- Q{i+1}: {question}")
    print(f"Expected: {expected}")
    try:
        result = qa.run(question)
        print(f"Generated: {result}")
    except Exception as e:
        print(f"❌ Failed to answer: {e}")