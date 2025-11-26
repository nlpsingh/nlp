OPENAI_API_KEY="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"

import requests, json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

data = {
    "model": "gpt-5.1",
    "messages": [
        {"role": "user", "content": "GIve full code of nlp pipeline"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
