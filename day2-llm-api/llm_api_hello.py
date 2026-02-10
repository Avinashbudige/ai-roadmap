# llm_api_hello.py - GitHub ready
from dotenv import load_dotenv
import os
from mistralai import Mistral

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    print("Set MISTRAL_API_KEY env var")
    exit(1)

client = Mistral(api_key=api_key)
response = client.chat.complete(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Hello from Bengaluru! Suggest ML project."}]
)
print(response.choices[0].message.content)
