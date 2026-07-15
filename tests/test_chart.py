import ollama

response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence? Reply in one sentence."
        }
    ]
)

print(response)