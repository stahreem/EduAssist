import ollama


class OllamaClient:

    def __init__(self, model="qwen3:1.7b"):
        self.model = model

    def generate(self, prompt):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "num_predict":350,
                "temperature":0.2
            }
        )

        return response["message"]["content"]