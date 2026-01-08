from google import genai
from src.retriever.pipeline import run_retriever_pipeline
from config.settings import settings

def run_gemini_chat(query):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    top_chunks = run_retriever_pipeline(query,2)
    user_query = "Who is the person in resume?"

    prompt = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the answer concise."
        "\n\nContext:\n" + top_chunks + "\n\nQuestion:\n" + user_query
    )

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL_NAME,
        contents=[
            {
                "role": "system", 
                "content": prompt
                },
            {
            "role": "user",
            "content": query
        }]
    )
    print("response",response)
    print(response.text)

    return response.text

if __name__ == "__main__":
    run_gemini_chat("Who is the person in resume?")