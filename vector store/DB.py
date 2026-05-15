from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(
        page_content="Artificial Intelligence helps machines learn and make decisions.",
        metadata={"source": "ai.txt"}
    ),
    Document(
        page_content="RAG combines retrieval systems with language models.",
        metadata={"source": "rag.txt"}
    ),
    Document(
        page_content="Cloud computing provides storage and services over the internet.",
        metadata={"source": "cloud.txt"}
    )
]

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Create Chroma vector database
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

print("ChromaDB created successfully!")

result=vectorstore.similarity_search("What is RAG?",k=2)
for r in result :
    print(r.page_content)
    print(r.metadata)

retriver=vectorstore.as_retriever()
docs=retriver.invoke('what is data science?')

for d in docs :
    print(d.page_content)
