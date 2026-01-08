import uuid
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from config.settings import settings

def initialize_chroma():
    # Initialize the Chroma client with persistence
    chroma_client = chromadb.PersistentClient(path=str(settings.get_chroma_storage_path()))
    collection_name = settings.CHROMA_COLLECTION_NAME
    collection = chroma_client.get_or_create_collection(
        name=collection_name, embedding_function=SentenceTransformerEmbeddingFunction(model_name=settings.EMBEDDING_MODEL_NAME)
    )
    return collection

def generate_embeddings(chunks):
    collection = initialize_chroma()
    for chunk in chunks:
        collection.upsert(documents=[chunk], ids=[str(uuid.uuid4())])
    return collection