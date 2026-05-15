from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

splitter=CharacterTextSplitter(separator='',
                               chunk_size=100,
                                chunk_overlap=1)

loader = TextLoader("document loaders/notes.txt")

documents = loader.load()
chunks = splitter.split_documents(documents)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk.page_content}")

