from .loaders.pdf_loader import load_pdf
from .chunking.recursive_character_splitter import recursive_character_splitter
from .embedding.chroma import generate_embeddings

def ingest_pdf(file_path):
    text = load_pdf(file_path)
    return text

def run_ingestion_pipeline():
    file_path = "data/pdf/TusharDhariaResume.pdf"
    text = ingest_pdf(file_path)
    chunks = recursive_character_splitter(text)
    generate_embeddings(chunks)
    return "Ingestion pipeline completed"

if __name__ == "__main__":
    run_ingestion_pipeline()