# summarizers/groq_mistral.py

import requests

def summarize_with_groq(text, api_key):
    """
    Sends text to Groq's Mixtral model and returns summary.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",  # Groq model ID
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant. Summarize this mining inspection log into a concise report of any issues found in the machine."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "temperature": 0.3,
        "max_tokens": 512
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                             headers=headers, json=payload)
    if response.status_code != 200:
        print("❌ Error:", response.text)  # 👈 Add this line
        response.raise_for_status()
    # response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
