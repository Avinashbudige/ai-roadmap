# llm_chat_loop_v2.py - Upgrade
import os
from mistralai import Mistral

import os
print("Key loaded:", bool(os.getenv("MISTRAL_API_KEY")))


client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
messages = [{"role": "system", "content": "AI/ML coach. Use CoT for reasoning."}]

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        
        messages.append({"role": "user", "content": user_input})
        stream = client.chat.stream(model="mistral-small-latest", messages=messages, stream=True)
        
        print("AI: ", end="", flush=True)
        full_reply = ""
        for chunk in stream:
            if chunk.data.choices[0].delta.content:
                content = chunk.data.choices[0].delta.content
                print(content, end="", flush=True)
                full_reply += content
        print("\n")
        
        messages.append({"role": "assistant", "content": full_reply})
    except Exception as e:
        print(f"Error: {e}")
