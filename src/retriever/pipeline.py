from src.ingestion.embedding.chroma import initialize_chroma

def run_retriever_pipeline(query_texts,n_results):
    collection = initialize_chroma()
    results = collection.query(query_texts=query_texts, n_results=n_results)
    # Extract the relevant chunks
    relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
    print("relevant_chunks",relevant_chunks, len(relevant_chunks))
    return relevant_chunks

if __name__ == "__main__":
    run_retriever_pipeline()