from .loaders.pdf_loader import load_pdf
from .chunking.recursive_character_splitter import recursive_character_splitter
from .embedding.chroma import generate_embeddings
from config.settings import settings

def ingest_pdf(file_path):
    text = load_pdf(file_path)
    return text

def run_ingestion_pipeline():
    file_path = settings.get_pdf_path()
    print(f"Ingesting PDF from: {file_path}")
    text = ingest_pdf(str(file_path))
    print(f"Text loaded successfully ({len(text)} characters)")
    chunks = recursive_character_splitter(text)
    print(f"Text split into {len(chunks)} chunks")
    generate_embeddings(chunks)
    print(f"Embeddings generated and stored for {len(chunks)} chunks")
    return "Ingestion pipeline completed"

if __name__ == "__main__":
    run_ingestion_pipeline()