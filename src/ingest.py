import fitz  # PyMuPDF
import os

# Define the PDF filename
PDF_NAME = "attention.pdf"

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text").strip() for page in doc])

        if not text.strip():
            raise ValueError(f"Extracted text from '{pdf_path}' is empty.")

        return text
    except Exception as e:
        print(f"Error while extracting text: {e}")
        return None

def ingest_documents():
    """Load document text for processing and save it."""
    pdf_path = f"./data/{PDF_NAME}"
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF '{PDF_NAME}' not found. Please check the 'data/' folder.")
        return []

    extracted_text = extract_text_from_pdf(pdf_path)
    
    if extracted_text:
        # Ensure the 'data/' directory exists before saving
        os.makedirs("data", exist_ok=True)
        
        with open("data/extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(extracted_text)
        
        print(f"Text extraction completed! Saved to 'data/extracted_text.txt'.")
        
        return [{"filename": PDF_NAME, "content": extracted_text}]
    
    return []

if __name__ == "__main__":
    docs = ingest_documents()
    if docs:
        print(f"Loaded: {docs[0]['filename']}, Length: {len(docs[0]['content'])} characters")