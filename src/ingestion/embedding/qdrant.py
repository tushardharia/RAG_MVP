from qdrant_client import QdrantClient

def initialize_qdrant():
    return QdrantClient(url="http://localhost:6333")

def generate_embeddings(chunks):
    return chunks