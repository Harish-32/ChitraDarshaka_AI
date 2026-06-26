import requests

def generate_trailer_script(story, language):

    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": f"""
You are a professional movie trailer writer.

Create a cinematic trailer narration.

Rules:
- Write ONLY in {language}
- Maximum 120 words
- Short dramatic sentences
- Trailer voice-over style
- No scene descriptions
- No bullet points
- No headings

Story:
{story}
""",
            "stream": False
        }
    )

    script = response.json()["response"]

    print("Language:", language)
    print("Script Length:", len(script))

    return script