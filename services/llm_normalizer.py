import os
import openai
import json
from typing import Literal
from config import OPENROUTER_KEY

# Load from env
openai.api_key = os.getenv("OPENAI_API_KEY")

TEMPLATE = {
    "weather": """
        Normalize the following JSON response from a weather API to this schema:
        {
        "location": string,
        "temperature_c": float,
        "condition": string
        }
        Only respond with valid JSON.
        """,
        "currency": """
        Normalize this JSON to:
        {
        "from": string,
        "to": string,
        "rate": float,
        "converted": float
        }
        Only respond with valid JSON.
    """,
}

def llm_normalize(task: Literal["weather", "currency"], provider_response: dict) -> dict:
    if task not in TEMPLATE:
        raise ValueError(f"Unsupported normalization type: {task}")

    prompt = TEMPLATE[task]
    
    client = openai.OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key=OPENROUTER_KEY
    )

    try:
        completion = client.chat.completions.create(
            model="openrouter/auto",  
            temperature=0,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": str(provider_response)}
            ]
        )

        content = completion.choices[0].message.content
        return json.loads(content)  # If using trusted models & sandbox, or use json.loads if sure it's JSON
    except Exception as e:
        print(f"[LLM Normalization Error] {e}")
        raise e