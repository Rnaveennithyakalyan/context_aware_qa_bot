#  Context-Aware QA Bot (Powered by Gemini & FAISS)

A powerful, modular command-line assistant that lets you ask questions grounded in documents—leveraging Google's Gemini API and FAISS-based semantic search for precise, contextually accurate responses.

---

##  Features

-  Context-aware question answering using your own document content  
-  Natural language responses powered by Gemini (`gemini-2.0-flash` by default)  
-  Fully integrated ingestion, indexing, and retrieval in a single command  
-  PDF-based knowledge embedding using Sentence Transformers + FAISS  
-  Multi-turn interactive CLI conversations with real-time Q&A  
-  Secure environment variable handling via `.env`  
-  Modular design for easy extension into web apps or APIs

---

##  Folder Structure

```
context_aware_qa_bot/
├── configs/
│   ├── .env                # Stores Gemini API key & model name (excluded from repo)
│   └── config.yaml         # Optional configuration (e.g. paths, settings)
├── data/
│   └── extracted_text.txt  # Auto-generated from PDFs
├── faiss_index/            # FAISS embedding index (auto-generated)
├── models/                 # Model cache or exported models (auto-populated)
├── src/
│   ├── ingest.py           # Extracts text from input PDFs
│   ├── indexing.py         # Converts text into vector embeddings
│   ├── qa_bot.py           # Gemini response module with retrieval
│   ├── retrieval.py        # Reusable FAISS retrieval logic
│   └── run_bot.py          # Unified launcher for ingestion + indexing + Q&A loop
├── .gitignore
├── requirements.txt
└── README.md
```

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

Required packages include:
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

##  API Key Configuration

Create a `.env` file inside the `configs/` folder:

```env
GEMINI_API_KEY=your-google-api-key
GEMINI_MODEL=gemini-2.0-flash
```

*Do NOT upload this `.env` file to GitHub.*

Optionally, you may define other paths or settings in `configs/config.yaml`.

---

##  Running the Assistant

Once your document is placed in the `data/` folder (e.g. `attention.pdf`), launch the bot with:

```bash
python src/run_bot.py
```

This will:
1.  Extract text from the PDF using `ingest.py`  
2.  Generate semantic embeddings and build the FAISS index via `indexing.py`  
3.  Start a chat loop where you can query the content using Gemini responses

Sample CLI interaction:

```
🤖 AI Bot is ready! Ask me anything about your document.
🔹 Ask a question: What is the purpose of positional encoding?
💡 AI Response:
Positional encoding allows the model to incorporate order information into the input tokens...
```

Type `exit` or `quit` to end the session.

---

##  How It Works

- `ingest.py` → Extracts full text from a PDF using PyMuPDF  
- `indexing.py` → Converts text into embeddings with `sentence-transformers` and stores in FAISS  
- `run_bot.py` → Orchestrates the full pipeline, launches the terminal-based Q&A loop  
- `retrieval.py` & `qa_bot.py` → Contain modular logic for semantic search and Gemini response generation—can be reused in other interfaces

---

##  Document Requirements

- File format: PDF  
- Place the file in the `data/` folder (default)  
- You can adjust the file path in `ingest.py` if needed

---

##  Configuration Tips

- Adjust `k=3` in `similarity_search()` for more or fewer retrieved chunks  
- Switch to `gemini-1.5-pro` or other supported model by updating `.env`  
- Want persistent memory or a web UI? This structure makes it easy to extend!

---

##  Future Enhancements

-  Streamlit or Flask-based Web Interface  
-  Telegram Chatbot integration  
-  Persistent memory across sessions  
-  Upload-anywhere document interface  
-  Visualization dashboard for FAISS embeddings

---

##  License

This project is licensed under the **MIT License**.  
You're free to use, modify, and build on it!

---

## Contact & Credits

Created by [@Rnaveennithyakalyan](https://github.com/Rnaveennithyakalyan)  
Email: [naveennithyakalyan@gmail.com](mailto:naveennithyakalyan@gmail.com)

---

