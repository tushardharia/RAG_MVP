from qdrant_client import QdrantClient
from config.settings import settings

def initialize_qdrant():
    return QdrantClient(url=settings.QDRANT_URL)

def generate_embeddings(chunks):
    return chunks