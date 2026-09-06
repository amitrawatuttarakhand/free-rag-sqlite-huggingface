from vector_store import similarity_search
from db_loader import get_movies
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Model & Tokenizer ko load karein
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# Pipeline me explicit model aur tokenizer pass karein
llm = pipeline(
    task="text2text-generation", 
    model=model, 
    tokenizer=tokenizer
)

def contextual_retrieve(query: str):
    docs = similarity_search(query, k=2)
    return [doc.page_content for doc in docs]

def run_hybrid_rag(query: str, verbose: bool = False):
    vector_results = similarity_search(query, k=4)
    graph_results = get_movies()
    contextual_results = contextual_retrieve(query)

    context_text = "\n\n".join(
        [doc.page_content for doc in vector_results] +
        contextual_results +
        [f"Movies in DB: {[m['title'] for m in graph_results]}"]
    )

    prompt = f"Answer the query: {query}\n\nContext:\n{context_text}"
    
    # LLM call with max length parameters
    final_answer = llm(prompt, max_new_tokens=256)[0]["generated_text"]

    return {
        "vector": [doc.page_content for doc in vector_results],
        "graph": [m['title'] for m in graph_results],
        "contextual": contextual_results,
        "llm_answer": final_answer
    }
