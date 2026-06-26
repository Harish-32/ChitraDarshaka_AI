import requests
import random
import os
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_image(prompt, filename):

    prompt = f"""
{prompt},
ultra realistic,
cinematic movie scene,
high detail,
8k,
dramatic lighting,
seed {random.randint(1,100000)}
"""

    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt
        },
        timeout=300
    )

    if response.status_code != 200:
        print(response.text)
        return

    with open(filename, "wb") as f:
        f.write(response.content)

    print("Saved:", filename)