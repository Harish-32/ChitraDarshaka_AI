import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def generate_scene_prompts(story):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2:3b",
            "prompt": f"""
You are a Hollywood storyboard artist.

Read the movie story and create EXACTLY 5 DIFFERENT cinematic image prompts.

Rules:
- Each prompt must describe a different scene.
- Include character appearance.
- Include location.
- Include lighting.
- Include camera angle.
- Include mood.
- Make every scene visually unique.
- One prompt per line.
- No numbering.
- No explanations.

Story:
{story}
""",
            "stream": False
        }
    )

    data = response.json()

    prompts = [
        p.strip()
        for p in data["response"].split("\n")
        if p.strip()
    ]

    return prompts[:5]