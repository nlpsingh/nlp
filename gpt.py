import requests

OPENAI_API_KEY = "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"   # rotate your key first

url = "https://api.openai.com/v1/responses"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

data = {
    "model": "gpt-5.1",
    "input": "Give full code of NLP pipeline"
}

response = requests.post(url, headers=headers, json=data)

print(response.json()["output_text"])

