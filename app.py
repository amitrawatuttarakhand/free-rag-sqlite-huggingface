import streamlit as st
from rag_chain import run_hybrid_rag
from db_loader import init_db

init_db()  # initialize free SQLite DB

st.title("Hybrid RAG Demo (Free DB + Free LLM)")

query = st.text_input("Enter your query:")

if query:
    result = run_hybrid_rag(query, verbose=False)

    st.subheader("Vector Store Results")
    for doc in result["vector"]:
        st.write(doc)

    st.subheader("Graph Results (SQLite DB)")
    for movie in result["graph"]:
        st.write(movie)

    st.subheader("Contextual Results")
    for ctx in result["contextual"]:
        st.write(ctx)

    st.subheader("LLM Final Answer")
    st.write(result["llm_answer"])
