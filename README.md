# 📚 RAG PDF Assistant

A Retrieval-Augmented Generation (RAG) application built using Streamlit, LangChain, Mistral AI, HuggingFace Embeddings, and ChromaDB.

https://rag-pdf-assistant-premkumark.streamlit.app/


This project allows users to:

* Upload PDF books/documents
* Create vector embeddings
* Ask questions from uploaded PDFs
* Get AI-generated answers using retrieved context

---

# 🚀 Features

* 📄 PDF Upload Support
* ✂️ Automatic Text Chunking
* 🧠 HuggingFace Embeddings
* 🗂️ Chroma Vector Database
* 🔍 MMR Retrieval Search
* 🤖 Mistral AI Integration
* 🌐 Streamlit Web UI
* 📚 Context-Based Question Answering
* 🔒 Secure API Key Handling
* ☁️ Streamlit Cloud Deployment Ready

---

# 🛠️ Tech Stack

| Component       | Technology                     |
| --------------- | ------------------------------ |
| Frontend        | Streamlit                      |
| LLM             | Mistral AI                     |
| Embeddings      | HuggingFace                    |
| Vector Database | ChromaDB                       |
| Framework       | LangChain                      |
| PDF Loader      | PyPDFLoader                    |
| Text Splitting  | RecursiveCharacterTextSplitter |
| Language        | Python                         |

---

# 📂 Project Structure

```bash
RAG/
│
├── app.py
├── main.py
├── create_database.py
├── requirements.txt
├── .gitignore
├── README.md
├── .env
├── document_loaders/
│   └── deeplearning.pdf
│
└── chroma_db/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Prem999k/RAG-PDF-Assistant.git
```

```bash
cd RAG-PDF-Assistant
```

---

## 2️⃣ Create Virtual Environment

```bash
py -3.11 -m venv .venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
```

---

# ▶️ Run Streamlit App

```bash
python -m streamlit run app.py
```

---

# 🧠 How It Works

## Step 1 — Upload PDF

The user uploads a PDF document.

## Step 2 — Load PDF

The application extracts text using:

```python
PyPDFLoader
```

## Step 3 — Split Text

The document is split into chunks using:

```python
RecursiveCharacterTextSplitter
```

## Step 4 — Generate Embeddings

Embeddings are created using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

## Step 5 — Store in ChromaDB

Embeddings are stored temporarily in Chroma vector database.

## Step 6 — Retrieval

Relevant chunks are retrieved using:

```python
MMR (Max Marginal Relevance)
```

## Step 7 — Generate Answer

Mistral AI generates context-aware responses.

---

# 📌 Main Functionalities

## 📄 PDF Processing

* Upload any PDF document
* Extract text automatically
* Chunk document into manageable sections

---

## 🔍 Semantic Search

* Uses vector similarity search
* Retrieves relevant document chunks
* Improves answer accuracy

---

## 🤖 AI Question Answering

Users can ask:

* Definitions
* Summaries
* Concept explanations
* Chapter questions
* Technical queries

---

# 📸 Screenshots

## Home Page

Add screenshot here.

## Upload PDF

Add screenshot here.

## AI Generated Response

Add screenshot here.

---

# 📦 Requirements

```txt
openai==1.99.9

langchain==0.3.27
langchain-core==0.3.86
langchain-community==0.3.27
langchain-openai==0.3.28
langchain-mistralai==0.2.11
langchain-huggingface==0.1.2
langchain-text-splitters==0.3.11

chromadb==1.0.15

pypdf==5.9.0
python-dotenv==1.1.1
tiktoken==0.9.0
sentence-transformers==5.0.0
unstructured==0.18.11

streamlit==1.47.1
fastapi==0.116.1
uvicorn==0.35.0

numpy==2.3.2
pandas==2.3.1
scikit-learn==1.7.1
rank-bm25==0.2.2
huggingface_hub==0.34.4

idna==3.10
jsonschema==4.25.1
pydantic==2.11.7
langsmith==0.4.14
```

---

# 🌐 Streamlit Deployment

## Deploy on Streamlit Community Cloud

1. Push project to GitHub
2. Open Streamlit Cloud
3. Select repository
4. Set `app.py` as main file
5. Add secrets:

```toml
MISTRAL_API_KEY="your_api_key"
```

6. Deploy application

---

# 🔒 Security

API keys are protected using:

```bash
.gitignore
```

Ignored files:

```txt
.venv/
.env
chroma_db/
__pycache__/
```

---

# 📈 Future Improvements

* Multi-PDF Support
* Chat History
* Streaming Responses
* Source Citations
* Hybrid Search
* OCR Support
* Advanced Retrieval Pipelines
* Local LLM Support
* Authentication System

---

# 🎯 Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* Prompt Engineering
* LLM Integration
* Streamlit Deployment
* LangChain Pipelines

---

# 👨‍💻 Author

Prem Kumar

GitHub:
[https://github.com/Prem999k](https://github.com/Prem999k)

---

# ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub.
