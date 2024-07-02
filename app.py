import sys
import os
import streamlit as st
from sentence_transformers import SentenceTransformer

# Ensure backend module is recognized
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.pdf_processing import process_pdfs
from backend.embedding import generate_embeddings
from backend.query_engine import setup_query_engine

st.title("Content Engine Chatbot")

uploaded_files = st.file_uploader("Choose PDFs", accept_multiple_files=True, type="pdf")

if uploaded_files:
    pdf_paths = []
    for uploaded_file in uploaded_files:
        path = os.path.join("data", uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        pdf_paths.append(path)
    
    st.write(f"Processing files: {pdf_paths}")  # Print the paths to verify
    
    pdf_texts_dict = process_pdfs(pdf_paths)
    pdf_texts = list(pdf_texts_dict.values())
    embeddings = generate_embeddings(pdf_texts)
    query_engine = setup_query_engine(embeddings, pdf_texts)

    query = st.text_input("Ask a question about the PDFs")
    if query:
        query_embedding = SentenceTransformer('all-MiniLM-L6-v2').encode([query])
        distances, top_texts = query_engine(query_embedding)
        st.write("Top results:")
        for distance, text in zip(distances, top_texts):
            st.write(f"Relevance: {distance}")
            st.write(text[:500])  # Display the first 500 characters as a snippet
