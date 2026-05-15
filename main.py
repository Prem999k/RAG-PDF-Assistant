import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Check if DB exists
if not os.path.exists("./chroma_db"):
    print("❌ Chroma database not found!")
    print("Run create_database.py first.")
    exit()

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

# Retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

# LLM
llm = ChatMistralAI(
    model="mistral-small-latest"
)

# Prompt Template
template = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Use only the provided context to answer the question.

If the answer is not in the context,
say: 'Could not find the answer in the document.'
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

print("✅ RAG System Created")
print("Press 0 to exit")

while True:

    query = input("\nEnter your question: ")

    if query == "0":
        print("Exiting...")
        break

    # Retrieve documents
    docs = retriever.invoke(query)

    # Combine context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Create prompt
    final_prompt = template.format_prompt(
        context=context,
        question=query
    )

    # Generate response
    response = llm.invoke(final_prompt)

    print("\n🤖 AI:", response.content)