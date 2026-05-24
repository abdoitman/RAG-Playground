from langchain_ollama import ChatOllama
import chromadb
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

DATA_PATH = "data"
CHROMADB_PATH = "chroma_db"

if __name__ == "__main__":
    _llm = ChatOllama(model= "qwen3.5:9b")

    query = input("Enter your query: ")
    client = chromadb.PersistentClient(path=CHROMADB_PATH)
    collection = client.get_or_create_collection(name= "books")

    results = collection.query(query_texts= [query], n_results=5)
    retrieved_docs = results['documents'][0]

    RAG_PROMPT = PromptTemplate(
        input_variables= ["query", "retrieved_docs"],
        template= """
        DOCUMENTS:
        {retrieved_docs}
        
        USER QUERY:
        {query}
        
        Based on the above documents only, provide a concise answer to the user's query. If the answer is not present in the documents, say 'I don't know'.
        """
    )

    chain = (
        RAG_PROMPT | _llm | StrOutputParser()
    )

    response = chain.invoke({
        "query": query, 
        "retrieved_docs": "\n\n".join(retrieved_docs)
    })

    print("Response from the model:")
    print(response)