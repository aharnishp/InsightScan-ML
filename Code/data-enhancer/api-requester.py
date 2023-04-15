import requests
import json

def ask_gpt(question, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    prompt = f"{question}"
    data = {
        # "model": "gpt-3.5-turbo",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["text"].strip()

with open("data-enhancer/chat-gpt.key", "r") as f:
    key = f.read()

# Replace YOUR_API_KEY with your actual OpenAI API key
api_key = key

# Ask a question and get a response from ChatGPT
# question = input("Ask a question: ")

item = "Amul Butter"

question = "list all the ingredients of 12 food products similar to the product" + str(item) + "?"
response = ask_gpt(question, api_key)
print(response)
