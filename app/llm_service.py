import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Api key is missing please check the .env file")


client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"

def get_llm_response(prompt:str) -> str:
    response = client.models.generate_content(
        model = MODEL,
        contents = prompt
    )

    if not response.text:
        raise HTTPException(
            status_code = status.HTTP_502_BAD_GATEWAY,
            detail= "No response from gemini"
        )

    return response.text