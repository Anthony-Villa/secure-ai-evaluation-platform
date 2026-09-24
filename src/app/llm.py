from src.app.config import client

def ask_llm(prompt):
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt,
    )

    return response.output_text