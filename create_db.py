import chromadb
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = "data"
CHROMADB_PATH = "chroma_db"

if __name__ == "__main__":
    client = chromadb.PersistentClient(path=CHROMADB_PATH)
    collection = client.get_or_create_collection(name= "books")
    print("Collection created successfully!")

    loader = PyMuPDFLoader(f"{DATA_PATH}/book.pdf")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    collection.delete(ids=[str(i) for i in range(len(texts))])

    collection.add(
        documents=[text.page_content for text in texts],
        ids=[str(i) for i in range(len(texts))],
        metadatas= [{"Page Number": text.metadata["page"],
                     "Author": text.metadata["author"],
                     "Year": "2014",
                     "Book Name": text.metadata["title"]} for text in texts]
    )
