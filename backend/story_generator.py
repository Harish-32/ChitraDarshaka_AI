import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def generate_story(prompt, language):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2:3b",
            "prompt": f"""
Write a cinematic movie story in {language}.

Movie Idea:
{prompt}
""",
            "stream": False
        }
    )

    data = response.json()

    return data["response"]