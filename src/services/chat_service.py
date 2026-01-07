from src.retriever.pipeline import run_retriever_pipeline

def run_chat_service():
    user_query = "Who is the person in resume?"
    top_chunks = run_retriever_pipeline(user_query,2)

    prompt = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the answer concise."
        "\n\nContext:\n" + top_chunks + "\n\nQuestion:\n" + user_query
    )
