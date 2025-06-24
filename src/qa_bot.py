import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

#  Load environment variables from `.env`
load_dotenv(dotenv_path="configs/.env")

#  Retrieve API key and model name securely
api_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")  # Default model

#  Validate API key before configuring Gemini API
if not api_key:
    raise ValueError("API key missing! Ensure 'GEMINI_API_KEY' is set in configs/.env.")

genai.configure(api_key=api_key)

#  Load stored FAISS embeddings for retrieval
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embeddings_model, allow_dangerous_deserialization=True)

def retrieve_context(query):
    """Fetch relevant context from FAISS embeddings."""
    docs = vectorstore.similarity_search(query, k=3)  # Get top 3 matches

    if not docs:
        return "No relevant context found. Answer based on general knowledge."

    return "\n".join([doc.page_content for doc in docs])

def ask_gemini(query):
    """Query Gemini API with retrieved context for better responses."""
    relevant_context = retrieve_context(query)
    prompt = f"Use this context to answer: {relevant_context}\n\nUser question: {query}"

    model = genai.GenerativeModel(gemini_model)  # Use model from .env
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    user_question = input("Ask a question: ")
    print(ask_gemini(user_question))
