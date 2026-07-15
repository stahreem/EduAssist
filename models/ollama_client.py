import ollama

class OllamaClient:

    def __init__(self, model="qwen3:1.7b"):
        self.model = model

    def generate(self, prompt):

        response = ollama.generate(
            model=self.model,
            prompt=prompt
        )

        print("\n========== RAW RESPONSE ==========")
        print(response)
        print("==================================")

        print("response field:")
        print(repr(response.get("response")))

        print("thinking field:")
        print(repr(response.get("thinking")))

        return response.get("response", "")