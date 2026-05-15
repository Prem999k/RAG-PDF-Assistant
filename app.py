import streamlit as st
from dotenv import load_dotenv
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="RAG Book Assistant")

st.title("📚 RAG Book Assistant")
st.write("Upload a PDF and ask questions from the document")

# HuggingFace Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF Book",
    type="pdf"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    if st.button("Create Vector Database"):

        with st.spinner("Processing document..."):

            # Load PDF
            loader = PyPDFLoader(file_path)
            docs = loader.load()

            # Split Text
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)

            # Create Temporary ChromaDB
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embedding_model
            )

            # Save in session state
            st.session_state.vectorstore = vectorstore

            st.success("Vector Database Created Successfully!")

# Load Vector DB from Session
if "vectorstore" in st.session_state:

    vectorstore = st.session_state.vectorstore

    # Retriever
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    # Mistral LLM
    llm = ChatMistralAI(
        model="mistral-small-latest"
    )

    # Prompt Template
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),

        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ])

    st.divider()
    st.subheader("Ask Questions From the Book")

    query = st.text_input("Enter your question")

    if query:

        with st.spinner("Generating answer..."):

            # Retrieve Docs
            docs = retriever.invoke(query)

            # Combine Context
            context = "\n\n".join([
                doc.page_content
                for doc in docs
            ])

            # Create Prompt
            final_prompt = prompt.invoke({
                "context": context,
                "question": query
            })

            # Generate Response
            response = llm.invoke(final_prompt)

            st.write("### 🤖 AI Answer")
            st.write(response.content)

            # Show Retrieved Chunks
            with st.expander("📄 Retrieved Context"):

                for i, doc in enumerate(docs):

                    st.markdown(f"### Chunk {i+1}")
                    st.write(doc.page_content)
                    st.divider()