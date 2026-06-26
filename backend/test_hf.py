import requests
import os
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

response = requests.get(
    "https://huggingface.co/api/whoami-v2",
    headers=headers
)

print(response.status_code)
print(response.text)