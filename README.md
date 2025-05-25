
# 🧠 GoSell AI RAG Demo

Welcome to the Precision AI RAG Demo hosted via GitHub Pages and powered by a backend on Fly.io. This interactive experience demonstrates how Retrieval-Augmented Generation (RAG) pipelines can be launched and monitored entirely from your browser.

---

## 🚀 How It Works
- **UI** is hosted on GitHub Pages → [Visit UI](https://your-username.github.io/gosellgenai)
- **Backend** (Flask + Streamlit + terminal) is deployed to Fly.io
- Clicking the `RAG Demo` tile:
  - Triggers backend reset script via `/trigger-bootstrap`
  - Launches terminal, loads editor, and boots RAG UX (Streamlit)

---

## 🔄 Backend Services (Fly.io)
Make sure these URLs are updated in:
- `docs/html/ragdemo.html`
- `index.html` RAG tile

```
https://rag-backend-demo.fly.dev/trigger-bootstrap
https://rag-backend-demo.fly.dev:8501
https://rag-backend-demo.fly.dev:5050
https://rag-backend-demo.fly.dev:7681
```

---

## 🧪 Local Testing
If you want to run this locally:
```bash
git clone https://github.com/your-username/gosellgenai.git
cd gosellgenai
make
```
Then open:
```
http://localhost:8080/docs/html/ragdemo.html
```

---

## ✨ Credits
Built using:
- Python, Streamlit, Flask
- Docker + Fly.io
- GitHub Pages + HTML5 frontend tiles

---

## 📬 Contact
Want to reuse this architecture or deploy a similar demo? Open an issue or [connect on LinkedIn](https://www.linkedin.com/in/genaigeek/)
