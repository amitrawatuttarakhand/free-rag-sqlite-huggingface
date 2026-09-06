from vector_store import similarity_search
from db_loader import get_movies
from transformers import pipeline

def contextual_retrieve(query: str):
    docs = similarity_search(query, k=2)
    return [doc.page_content for doc in docs]

def run_hybrid_rag(query: str, verbose: bool = False):
    vector_results = similarity_search(query, k=4)
    graph_results = get_movies()
    contextual_results = contextual_retrieve(query)

    # ✅ Use text2text-generation (works with Flan-T5 if version pinned)
    llm = pipeline("text2text-generation", model="google/flan-t5-base")

    context_text = "\n\n".join(
        [doc.page_content for doc in vector_results] +
        contextual_results +
        [f"Movies in DB: {[m['title'] for m in graph_results]}"]
    )

    final_answer = llm(f"Answer the query: {query}\n\nContext:\n{context_text}")[0]["generated_text"]

    return {
        "vector": [doc.page_content for doc in vector_results],
        "graph": [m['title'] for m in graph_results],
        "contextual": contextual_results,
        "llm_answer": final_answer
    }
