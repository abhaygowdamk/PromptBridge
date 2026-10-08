import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from google import genai
from google.genai import errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is missing or not loaded.")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"


def get_llm_response(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    if not response.text:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="LLM returned an empty response",
        )

    return response.text