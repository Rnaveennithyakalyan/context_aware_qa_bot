import os
import sys
import time
import subprocess
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv(dotenv_path="configs/.env")
api_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

if not api_key:
    raise ValueError("❌ Missing GEMINI_API_KEY in configs/.env!")

#  Configure Gemini API
genai.configure(api_key=api_key)

#  Run ingestion and indexing using the current Python interpreter
print("📄 Extracting text from documents...")
subprocess.run([sys.executable, "src/ingest.py"], check=True)

print("🔧 Building FAISS index from extracted text...")
subprocess.run([sys.executable, "src/indexing.py"], check=True)

#  Load FAISS vector store
print("🔎 Loading vector store...")
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embeddings_model, allow_dangerous_deserialization=True)

def retrieve_context(query):
    """Retrieve top-k relevant chunks from FAISS index."""
    results = vectorstore.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in results]) if results else "No relevant context found."

def ask_gemini(question):
    """Generate a response using Gemini with contextual grounding."""
    context = retrieve_context(question)
    prompt = f"Use the following context to answer the question:\n\n{context}\n\nQuestion: {question}"
    model = genai.GenerativeModel(gemini_model)
    response = model.generate_content(prompt)
    return response.text.strip()

#  User interaction loop
print("\n🤖 AI Bot is ready! Ask me anything about your document.")
print("Type 'exit' or 'quit' to end the session.\n")

while True:
    user_input = input("🔹 Ask a question: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        print("👋 Goodbye! Have a productive day!")
        break

    answer = ask_gemini(user_input)
    print(f"\n💡 AI Response:\n{answer}\n")
    time.sleep(1)
