import ollama


while True:
    msg = input("You: ")

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    print("Bot:", response["message"]["content"])