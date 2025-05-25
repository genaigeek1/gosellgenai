# 🧠 macRAG: Local RAG Stack on Mac

macRAG is a modular, secure, and locally-deployable Retrieval-Augmented Generation (RAG) framework that runs on your Mac with full Dockerized support. It allows developers to:
- Load & chunk documents
- Embed & index them into vector databases
- Retrieve relevant content for LLM-based Q&A
- Visualize and evaluate model performance with integrated benchmarking tools

---

## 📐 Architecture Overview

![Architecture](images/architecture.png)

---

## 📂 Project Structure

- `src/` - Core modules: loaders, chunkers, retriever, embeddings, reranker
- `data/` - Sample datasets including `hotpot_sample.json`
- `streamlit_app/` - Interactive UI powered by Streamlit
- `notebooks/` - Embedding visualization and metric evaluation notebooks
- `eval/` - Evaluation scripts and charts
- `tests/` - Unit tests for each major component
- `.env.example` - Environment variable template
- `docker-compose.yml` - Local deployment using Docker
- `setup.sh` - End-to-end setup script

---

## 🚀 Getting Started

```bash
bash setup.sh
```

Then visit the UI at: http://localhost:8501

---

## 🔐 Security Considerations

This is a local demo stack for experimentation. In production, add:

- Authentication (e.g., Streamlit Authenticator)
- HTTPS/TLS with a reverse proxy
- Rate-limiting, API auditing, input sanitization
- Data encryption for local storage

---

## 📊 Evaluation Support

- Supports BLEU, Precision, Recall
- Metric charts via Matplotlib
- Evaluation Notebook included under `notebooks/`

---

## 🛠️ Requirements

- Python 3.9+
- Docker
- Ollama CLI or similar for local LLMs

---

## 🙌 Acknowledgments

macRAG leverages open-source technologies including:
- LangChain
- FAISS / Chroma
- Streamlit
- Ollama

Inspired by practical needs for local GenAI prototyping.
---

## 🧠 Secure RAG Architecture on Vertex AI

![Secure RAG on Vertex AI](architecture.png)

This diagram illustrates a secure retrieval-augmented generation (RAG) pipeline leveraging Vertex AI, with integrated components like:

- **Security Layer**: Authentication, encryption, and audit logging
- **Vector Database**: Storing semantically indexed embeddings
- **Generative Model**: Vertex AI + Custom Foundation Models
- **Prompt Flow**: Query understanding, context injection, and synthesis
- **Enterprise Data**: Structured and unstructured sources under access control

---

## 🧱 Platform-Based RAG Approach

This project is structured to enable modular replacement and experimentation:

| Layer              | Component                        | Replaceable With                |
|-------------------|----------------------------------|---------------------------------|
| Chunking          | `src/chunkers.py`                | Markdown/semantic chunking     |
| Embeddings        | `src/embeddings.py`              | ELSER / OpenAI / Cohere        |
| Vector Store      | FAISS / Chroma                   | Weaviate / Pinecone / Qdrant   |
| Reranker (opt)    | `src/rerankers.py`               | Relevance classifier / BM25    |
| LLM Backend       | Ollama + LangChain               | Vertex AI / OpenAI / Claude    |
| App Interface     | Streamlit                        | Gradio / FastAPI               |
| Evaluation        | `notebooks/metric_eval.ipynb`    | Custom BLEU / ROUGE pipelines  |

---

