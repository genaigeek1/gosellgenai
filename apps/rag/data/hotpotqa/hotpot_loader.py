import json
from langchain.schema import Document

def load_hotpotqa_documents(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    all_chunks = []
    for entry in data:
        for title, paras in entry["context"]:
            combined = f"## {title}\n" + "\n".join(paras)
            all_chunks.append(Document(page_content=combined))
    return all_chunks