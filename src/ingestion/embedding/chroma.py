import uuid
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def initialize_chroma():
    # Initialize the Chroma client with persistence
    chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
    collection_name = "document_collection"
    collection = chroma_client.get_or_create_collection(
        name=collection_name, embedding_function=SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    )
    return collection

def generate_embeddings(chunks):
    collection = initialize_chroma()
    for chunk in chunks:
        collection.upsert(documents=[chunk], ids=[str(uuid.uuid4())])
    return collection