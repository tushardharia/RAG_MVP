from src.retriever.pipeline import run_retriever_pipeline
from openai import OpenAI
from config.settings import settings

def run_chat_service():
    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is required for chat_service. Please set it in your .env file.")
    
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    user_query = "Who is the person in resume?"
    top_chunks = run_retriever_pipeline(user_query,2)

    prompt = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the answer concise."
        "\n\nContext:\n" + top_chunks + "\n\nQuestion:\n" + user_query
    )

    response = client.chat.completions.create(
        model=settings.OPENAI_MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": user_query,
            },
        ],
    )

    answer = response.choices[0].message
    return answer
