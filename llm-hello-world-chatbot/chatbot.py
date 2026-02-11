# chatbot.py
import os
from mistralai import Mistral

def main():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY not set.")
        return

    client = Mistral(api_key=api_key)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI development coach. Think step by step and explain clearly."
        }
    ]

    print("LLM Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Bot: Goodbye! 👋")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.complete(
                model="mistral-small-latest",
                messages=messages
            )
            reply = response.choices[0].message.content
        except Exception as e:
            print(f"Bot: Error calling API: {e}")
            continue

        print("Bot:", reply)
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
