# Content Engine Chatbot
## Overview
This repository contains a Streamlit application that processes PDF files, generates embeddings for their text content using a SentenceTransformer model, and sets up a query engine to find relevant information based on user queries.
<img width="1440" alt="Screenshot 2024-07-02 at 11 27 24 PM" src="https://github.com/MihirLodaya/Content-Engine-Chatbot/assets/154822670/f2397047-5639-4715-9c1d-6d4a50f91e83">

## Features
PDF Processing: Extracts text from uploaded PDF files.
Text Embedding: Uses a pre-trained SentenceTransformer model to generate embeddings for the extracted text.
Query Engine: Uses cosine similarity to find and display the most relevant text snippets from the PDFs in response to user queries.

## Modules
1.PDF_PROCESSING:<br>The pdf_processing.py module is responsible for extracting text from PDF files using the PyPDF2 library. It reads each page of the PDFs and accumulates the extracted text, returning a dictionary with file paths as keys and extracted text as values. This enables the application to handle multiple PDF files and consolidate their content efficiently.

2.EMBEDDING:<br>The embedding.py module generates embeddings for the extracted text content. Using the SentenceTransformer library, specifically the 'all-MiniLM-L6-v2' model, it encodes the text into high-dimensional vector representations. These embeddings capture the semantic meaning of the text, making them suitable for similarity comparisons. The module provides a function to convert a list of text strings into their corresponding embeddings, facilitating the subsequent querying process.

3.QUERY_ENGINE:<br>The query_engine.py module sets up a query engine that allows users to search for relevant text snippets within the processed PDFs. It uses cosine similarity to compare the query embedding with the embeddings of the PDF texts. The module initializes the query engine with the embeddings and corresponding texts and returns a function that performs searches. This function computes the cosine similarity between the query embedding and the stored embeddings, retrieves the most relevant text snippets, and sorts the results based on similarity scores. Together, these modules enable the application to process PDFs, generate embeddings, and perform efficient and accurate searches, providing users with relevant information based on their queries.
