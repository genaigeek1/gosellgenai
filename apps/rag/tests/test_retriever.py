from src.embeddings import get_embedding_model
from src.retriever import build_retriever_from_texts

def test_retrieval():
    embedder = get_embedding_model()
    retriever, _ = build_retriever_from_texts(["Paris is in France", "Rome is in Italy"], embedder)
    results = retriever.get_relevant_documents("Where is Paris?")
    assert any("Paris" in doc.page_content for doc in results)