import PyPDF2

def process_pdfs(pdf_paths):
    pdf_texts = {}
    for path in pdf_paths:
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            pdf_texts[path] = text
    return pdf_texts
