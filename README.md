# 🤖 RAG-Powered PDF Chatbot with Local LLM (Ollama + Streamlit UI)

Build a **Retrieval-Augmented Generation (RAG)** chatbot for local PDFs/texts using **ChromaDB**, **LangChain**, and **Ollama** with a **Mistral** model—completely offline, no OpenAI API needed.

---

## 📌 Features

- Chat with your own PDFs or text data
- Powered by local LLMs via **Ollama**
- Uses **ChromaDB** for fast semantic search
- Lightweight, private, and fast
- Clean UI via **Streamlit**

---

## 🗂️ Project Structure

```text
.
├── chroma/ # Persisted ChromaDB vector store
├── data/ # Source documents (PDFs/texts)
├── get_embedding_function.py # Returns embedding function
├── populate_database.py.py # Create vector embedding and store to the ChromaDB
├── query_data.py # CLI version of the query flow
├── app.py # Streamlit UI for the chatbot
├── test_rag.py # Run few unit test cases
├── requirements.txt # Python dependencies
└── README.md # This file
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Pull Mistral via Ollama and start Ollama server

Make sure Ollama is instaled and then run:

```bash
ollama pull mistral
ollama serve
```

### 3. Create database

Create the Chroma DB.

```bash
python populate_database.py
```

---

## 🧠 Run the App

### 1.1: Streamlit UI (Recommended)

Launch the UI:

```bash
streamlit run app.py
```

- Input your question in the text field
- Get answers and see cited source chunks
- Uses local Chroma vector store + Mistral model

### 1.2: Command-Line Interface

```bash
python query_data.py "What are the rules for Monopoly?"
```

### 2. Run Test Cases

```bash
pytest -s
```

---

## 🧱 How It Works

1. Document Ingestion – Load and chunk PDFs/text files
2. Embedding – Embed text chunks using your preferred model (OllamaEmbeddings is used)
3. Vector Search – Retrieve top 5 relevant chunks using Chroma
4. Prompting – Feed context + user query into a prompt
5. LLM Answering – Generate response using Ollama LLM
6. Citations – Output source IDs used in the answer

---

## 🖼️ Preview

![Landing Page](https://github.com/sarmishra/Python-RAG-Chatbot-With-Local-LLM/blob/main/RAG-Chatbot-WIth-Local-LLM-Preview.png)

---
