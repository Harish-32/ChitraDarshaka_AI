import requests

def generate_scenes(story):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3.2:3b",
            "prompt":f"""
Create exactly 5 movie scenes.

For each scene provide only an image prompt.

Story:
{story}
""",
            "stream":False
        }
    )

    return response.json()["response"]