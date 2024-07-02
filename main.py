from pdf_processing import process_pdfs
from embedding import generate_embeddings
from query_engine import setup_query_engine

def main():
    pdf_paths = ["data/goog-10-k-2023 (1).pdf", "data/tsla-20231231-gen.pdf", "data/uber-10-k-2023.pdf"]
    pdf_texts = process_pdfs(pdf_paths)
    embeddings = generate_embeddings(pdf_texts)
    setup_query_engine(embeddings)

if __name__ == "__main__":
    main()
