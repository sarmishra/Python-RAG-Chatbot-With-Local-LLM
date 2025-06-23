# app.py

import streamlit as st
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

@st.cache_resource
def load_db():
    embedding_function = get_embedding_function()
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

def query_rag(query_text: str):
    db = load_db()
    results = db.similarity_search_with_score(query_text, k=5)

    if not results:
        return "⚠️ No relevant documents found.", []

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = OllamaLLM(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", "Unknown") for doc, _ in results]
    return response_text, sources

# Streamlit UI
st.set_page_config(page_title="📘 RAG PDF Chat With Local LLM", layout="centered")
st.title("📘 Chat with Your PDFs (RAG + Local LLM)")

query = st.text_input("Ask a question about your PDFs:")
submit = st.button("Ask")

if submit and query:
    with st.spinner("Thinking..."):
        response, sources = query_rag(query)

        st.markdown("### 💬 Answer")
        st.write(response)

        st.markdown("### 📚 Sources")
        for source in sources:
            st.markdown(f"- `{source}`")