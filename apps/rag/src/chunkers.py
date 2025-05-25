from langchain.text_splitter import CharacterTextSplitter, MarkdownHeaderTextSplitter

def basic_chunk(docs, chunk_size=200, chunk_overlap=50):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def markdown_chunk(docs):
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("##", "Section")])
    return splitter.split_documents(docs)