from src.embeddings import get_embedding_model

def test_embedding_vector_shape():
    model = get_embedding_model()
    vectors = model.embed_documents(["Paris", "Rome", "New York"])
    assert len(vectors) == 3
    assert all(isinstance(vec, list) for vec in vectors)