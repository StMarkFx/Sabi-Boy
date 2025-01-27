import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(argument):
    prompt = f"""
    Provide a research-based or scientific answer to the following argument: '{argument}'. Follow these guidelines:
    1. Be concise and factual.
    2. If no specific research exists, state that and provide a general scientific explanation.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use GPT-4 or GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant that provides research-based or scientific answers to settle arguments."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']