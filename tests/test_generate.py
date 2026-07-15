import ollama

response = ollama.generate(
    model="qwen3:1.7b",
    prompt="What is Artificial Intelligence? Reply in one sentence."
)

print(response)