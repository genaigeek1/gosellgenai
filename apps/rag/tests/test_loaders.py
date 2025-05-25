import os
from src.loaders import load_documents_from_folder

def test_load_txt_file(tmp_path):
    txt_file = tmp_path / "sample.txt"
    txt_file.write_text("This is a test document about Paris.")
    docs = load_documents_from_folder(str(tmp_path))
    assert any("Paris" in doc.page_content for doc in docs)