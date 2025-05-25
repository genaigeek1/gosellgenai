from langchain.document_loaders import TextLoader, PyMuPDFLoader, UnstructuredHTMLLoader
import os

def load_documents_from_folder(folder_path):
    supported_extensions = [".txt", ".pdf", ".html", ".htm"]
    all_docs = []
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        if file.endswith(".txt"):
            all_docs += TextLoader(path).load()
        elif file.endswith(".pdf"):
            all_docs += PyMuPDFLoader(path).load()
        elif file.endswith(".html") or file.endswith(".htm"):
            all_docs += UnstructuredHTMLLoader(path).load()
    return all_docs