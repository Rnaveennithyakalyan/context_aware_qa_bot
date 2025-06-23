#  Context-Aware QA Bot (Powered by Gemini & FAISS)

A powerful, modular command-line assistant that uses Retrieval-Augmented Generation (RAG) to answer questions based on your documents—leveraging Google's Gemini API and FAISS-based semantic search for fast, relevant, and contextually accurate responses.

---

##  Features

-  Retrieval-Augmented Generation (RAG) using custom PDFs
-  Gemini-powered natural language responses (`gemini-2.0-flash` by default)
-  PDF ingestion and semantic vector indexing in one command
-  High-speed document similarity search with FAISS
-  Multi-turn terminal chat with real-time AI responses
   API key and model configuration via secure `.env`
-  Modular components for CLI, web app, or API integration

---

##  Folder Structure

```
context_aware_qa_bot/
├── configs/
│   ├── .env                # Stores Gemini API key (not committed)
│   └── config.yaml         # Optional configuration (paths, defaults)
├── data/
│   └── attention.pdf       # Upload your PDF(s) here
│   └── extracted_text.txt  # Auto-generated during ingestion
├── faiss_index/            # FAISS vector index (auto-generated)
├── models/                 # Model cache / temp storage (auto-populated)
├── src/
│   ├── ingest.py           # Extracts text from your uploaded PDF
│   ├── indexing.py         # Embeds and indexes text using FAISS
│   ├── qa_bot.py           # Gemini response logic
│   ├── retrieval.py        # FAISS-based context retriever
│   └── run_bot.py          # All-in-one launcher script
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  What is RAG (Retrieval-Augmented Generation)?

**Retrieval-Augmented Generation** is a hybrid AI architecture that combines two components:

1. **Retriever** — Finds the most relevant information from a local knowledge base using vector similarity (powered by FAISS in this project).
2. **Generator** — A language model (Gemini) that uses this retrieved content to generate grounded, coherent answers.

This prevents hallucinations, increases traceability, and makes the model act more like a smart assistant tied directly to your documents.

---

##  Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/context_aware_qa_bot.git
cd context_aware_qa_bot
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate            # Windows
# OR
source venv/bin/activate         # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
```
google-generativeai
python-dotenv
langchain-community
langchain-huggingface
sentence-transformers
faiss-cpu
PyMuPDF
tqdm
```

---

##  API Key Setup

Create a `.env` file in the `configs/` folder and add your Gemini API key:

```env
GEMINI_API_KEY=your-google-api-key
GEMINI_MODEL=gemini-2.0-flash
```

---

##  Upload Your PDF (Before Running)

To use this bot, you must upload at least one PDF document:

- Place your file (e.g., `attention.pdf`) inside the `data/` folder
- You can rename your file or change the file path in `src/ingest.py` as needed

---

##  Running the Assistant

Start the full pipeline with:

```bash
python src/run_bot.py
```

This will:
1. Extract text from the uploaded PDF
2. Generate vector embeddings and build a FAISS index
3. Launch a terminal chat loop using Gemini + semantic search

Example:

```
🤖 AI Bot is ready! Ask me anything about your document.
🔹 Ask a question: What is the purpose of positional encoding?
💡 AI Response:
Positional encoding allows the model to incorporate order information into the input tokens...
```

Type `exit` or `quit` to end the session.

---

##  How It Works (RAG Pipeline)

- `ingest.py` → Reads the uploaded PDF and saves clean text
- `indexing.py` → Embeds the text and builds the FAISS index for semantic search
- `retrieval.py` → Pulls the top-k relevant chunks from your document
- `qa_bot.py` → Builds Gemini prompts using those chunks as context
- `run_bot.py` → Automates the full pipeline and launches the interactive terminal bot

---

##  Document Guidelines

- Format: PDF only (support for other formats can be added)
- Place your file inside the `data/` folder before running
- Large or image-heavy PDFs should contain extractable text

---

##  Configuration Tips

- Adjust `k` in `similarity_search(query, k=3)` to expand/restrict retrieved context
- Update `GEMINI_MODEL` in `.env` for better accuracy or response quality
- Want to expose this bot as a web app or API? Just reuse `qa_bot.py` and `retrieval.py`!

---

##  Future Enhancements

-  Streamlit front-end (web-based version)
-  Persistent memory or history across sessions
-  Telegram / WhatsApp chatbot modes
-  Multi-file or folder-based ingestion
-  FAISS visual diagnostics and cluster heatmaps

---

##  License

This project is licensed under the **MIT License**.  
Use it freely, modify it, and contribute!

---

##  Contact & Credits

Created by [@Rnaveennithyakalyan](https://github.com/Rnaveennithyakalyan)  
Email: [naveennithyakalyan@gmail.com](mailto:naveennithyakalyan@gmail.com)

---
