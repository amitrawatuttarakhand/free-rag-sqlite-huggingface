from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from db_loader import get_movies

_vector_store = None

def build_documents():
    movies = get_movies()
    docs = []
    for movie in movies:
        content = (
            f"Title: {movie['title']}\n"
            f"Year: {movie['year']}\n"
            f"Genre: {movie['genre']}\n"
            f"Description: {movie['description']}\n"
            f"Director: {movie['director']}\n"
        )
        docs.append(Document(page_content=content))
    return docs

def create_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docs = build_documents()
    return FAISS.from_documents(docs, embeddings)

def get_vector_store():
    global _vector_store
    if _vector_store is None:
        _vector_store = create_vector_store()
    return _vector_store

def similarity_search(query: str, k: int = 4):
    vs = get_vector_store()
    return vs.similarity_search(query, k=k)
