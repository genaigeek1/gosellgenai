import os
import streamlit as st
import tempfile
from dotenv import load_dotenv

from langchain.llms import Ollama
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader, PyMuPDFLoader, UnstructuredHTMLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

import streamlit_authenticator as stauth

# Load environment variables
load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "mistral")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

# Auth Setup
credentials = {
    "usernames": {
        "admin": {
            "name": "Admin User",
            "password": stauth.Hasher(["adminpass"]).generate()[0]
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "rag_app",  # cookie_name
    "auth_token",  # key
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("Username/password is incorrect")
    st.stop()
elif authentication_status is None:
    st.warning("Please enter your username and password")
    st.stop()

authenticator.logout("Logout", "sidebar")
st.sidebar.success(f"Welcome *{name}*")

# Streamlit UI
st.title("📚 Local RAG Chat (w/ Login)")

uploaded_file = st.file_uploader("Upload a .txt, .pdf, or .html file", type=["txt", "pdf", "html"])
query = st.text_input("Ask a question")

if uploaded_file and query:
    ext = os.path.splitext(uploaded_file.name)[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if ext == ".txt":
        docs = TextLoader(tmp_path).load()
    elif ext == ".pdf":
        docs = PyMuPDFLoader(tmp_path).load()
    elif ext == ".html":
        docs = UnstructuredHTMLLoader(tmp_path).load()
    else:
        st.error("Unsupported file type")
        st.stop()

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    texts = [doc.page_content for doc in chunks]

    embedder = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = FAISS.from_texts(texts, embedder)

    retrieved = db.similarity_search_with_score(query, k=3)

    st.markdown("### Retrieved Contexts with Similarity Scores")
    for i, (doc, score) in enumerate(retrieved):
        st.markdown(f"**Chunk {i+1} (Score: {score:.4f})**")
        st.code(doc.page_content)

    llm = Ollama(model=MODEL_NAME, base_url=OLLAMA_HOST)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    result = qa.run(query)

    st.markdown("### 💬 Answer")
    st.success(result)