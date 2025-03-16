from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

class EmbeddingEngine:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.vector_store = Chroma(embedding_function=self.embeddings, persist_directory="./chroma_db")

    def create_embeddings(self, articles):
        """Create and store embeddings for articles."""
        documents = [f"{article['title']}\n{article['content']}" for article in articles]
        metadatas = [{"url": article['url']} for article in articles]
        
        self.vector_store.add_texts(
            texts=documents,
            metadatas=metadatas
        )
        self.vector_store.persist()
        
    def search_similar(self, query, k=3):
        """Search for similar articles."""
        return self.vector_store.similarity_search(query, k=k)