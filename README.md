# 🎬 Hybrid RAG Demo (SQLite + HuggingFace + Streamlit)

A free, cloud‑ready **Hybrid RAG (Retrieval‑Augmented Generation)** project that combines:
- **Vector retriever** (FAISS + HuggingFace embeddings)
- **Contextual retriever** (semantic similarity search)
- **Graph retriever** (SQLite database, no paid instance required)
- **LLM** (Flan‑T5 via HuggingFace Transformers, free, no API key)

Deployed easily on **Streamlit Cloud** without any external credentials.

---

## 🚀 Features
- 🔎 **Semantic search** across movie dataset using FAISS
- 📚 **SQLite database** with 15+ sample movies (no username/password needed)
- 🤖 **Free LLM** (Flan‑T5) for natural language answers
- 🌐 **Streamlit UI** for interactive queries
- 💡 **No API keys, no paid DB** — fully free setup

---

## 📂 Project Structure
ree-rag-sqlite-huggingface/
│
├── app.py              # Streamlit UI
├── db_loader.py        # SQLite DB + sample movies
├── vector_store.py     # FAISS vector retriever
├── rag_chain.py        # Hybrid RAG pipeline
├── requirements.txt    # Dependencies



---

## ⚙️ Installation & Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/amitrawatuttarakhand/free-rag-sqlite-huggingface.git
   cd free-rag-sqlite-huggingface

pip install -r requirements.txt

streamlit run app.py


🎯 Usage Examples

Type queries in the Streamlit search box:

Movie title search → Tell me about The Matrix

Director search → Movies directed by Christopher Nolan

Genre search → List Sci-Fi movies in the database

Year search → Movies released in 1994

Plot explanation → Explain the plot of Inception in 2 lines

Comparison → Compare The Matrix and Inception





🛠 Requirements
Python 3.9+

Streamlit

LangChain

HuggingFace Transformers

FAISS

Torch

Dependencies are pinned in requirements.txt for Streamlit Cloud compatibility.

❤️ Credits
Built by Amit Rawat  
Powered by SQLite, HuggingFace, FAISS, LangChain, Streamlit
