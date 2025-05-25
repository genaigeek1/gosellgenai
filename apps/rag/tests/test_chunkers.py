from langchain.schema import Document
from src.chunkers import basic_chunk

def test_basic_chunking():
    docs = [Document(page_content="Hello World. " * 50)]
    chunks = basic_chunk(docs, chunk_size=100, chunk_overlap=20)
    assert len(chunks) >= 1
    assert all(isinstance(chunk.page_content, str) for chunk in chunks)