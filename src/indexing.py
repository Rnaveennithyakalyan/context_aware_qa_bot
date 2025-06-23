import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document  # Wrap extracted text for FAISS indexing

# Load the Hugging Face embedding model
model = SentenceTransformer("all-MiniLM-L6-v2", cache_folder="models/")
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def generate_embeddings(text):
    """Generate embeddings using Hugging Face's Sentence Transformers."""
    return model.encode(text, convert_to_tensor=False).tolist()  # Convert tensor to list for JSON storage

# Load extracted text
TEXT_FILE = "data/extracted_text.txt"

if not os.path.exists(TEXT_FILE):
    raise FileNotFoundError("Error: 'extracted_text.txt' is missing. Run ingest.py first.")

with open(TEXT_FILE, "r", encoding="utf-8") as f:
    text_data = f.read().strip()

if not text_data:
    raise ValueError("Error: 'extracted_text.txt' is empty. Check ingest.py.")

# Generate embeddings
embeddings = generate_embeddings(text_data)

if embeddings:
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    
    # Save embeddings in JSON format
    with open("data/embeddings.json", "w", encoding="utf-8") as f:
        json.dump(embeddings, f)

    print("✅ Embedding generation completed! Saved to 'data/embeddings.json'.")

    # Create FAISS index
    documents = [Document(page_content=text_data)]  # Wrap text for FAISS indexing
    vectorstore = FAISS.from_documents(documents, embeddings_model)

    # Save FAISS index locally
    vectorstore.save_local("faiss_index")
    print("✅ FAISS index created! Saved to 'faiss_index/index.faiss'.")
else:
    print("⚠ Embedding generation failed.")