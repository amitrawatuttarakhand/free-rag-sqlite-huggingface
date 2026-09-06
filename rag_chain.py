from vector_store import similarity_search
from db_loader import get_movies
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Script load hone par model initialize karein
MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def contextual_retrieve(query: str):
    docs = similarity_search(query, k=2)
    return [doc.page_content for doc in docs]


def run_hybrid_rag(query: str, verbose: bool = False):
    vector_results = similarity_search(query, k=4)
    graph_results = get_movies()
    contextual_results = contextual_retrieve(query)

    # Context formatting
    vector_text = "\n".join([doc.page_content for doc in vector_results])
    contextual_text = "\n".join(contextual_results)
    
    context_text = f"Vector Data:\n{vector_text}\n\nContextual Data:\n{contextual_text}"

    # Detailed summary prompt
    prompt = f"""Based on the provided context, give a brief summary of the movie including year, genre, director, and plot description.

Context:
{context_text}

Question: {query}
Answer:"""

    # Direct Model Generation
    inputs = tokenizer(
        prompt, return_tensors="pt", truncation=True, max_length=512
    )
    outputs = model.generate(**inputs, max_new_tokens=150)
    final_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "vector": [doc.page_content for doc in vector_results],
        "graph": [m["title"] for m in graph_results],
        "contextual": contextual_results,
        "llm_answer": final_answer,
    }
