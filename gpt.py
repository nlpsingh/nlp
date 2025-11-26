import google.generativeai as genai

genai.configure(api_key="AIzaSyCFqZVCQLKJTM2vnqYz_xdGSRRXiP098vk")

model = genai.GenerativeModel("gemini-2.5-pro")

response = model.generate_content(
    "Give complete TF-IDF example with explanation.",
    stream=True
)

for chunk in response:
    print(chunk.text, end="")
