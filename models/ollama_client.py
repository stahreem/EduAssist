import logging
import ollama

from config.config import OLLAMA_MODEL

logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Reusable Ollama client for all AI modules.
    """

    def __init__(self, model=None):
        self.model = model or OLLAMA_MODEL

    def generate(self, prompt):
        """
        Generate response using Ollama.
        """

        try:
            logger.info(f"Calling Ollama model: {self.model}")
            print(f"🚀 Calling Ollama ({self.model})...", flush=True)

            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                think=False, 
                options={
                    "temperature": 0 ,
                    "num_predict": 500,
                    "top_p": 0.9,
                    "num_ctx": 4096,
                }
            )
            print("=" * 70)
            print(response)
            print("=" * 70)
            result = response.get("response", "").strip()

            print(f"📥 Received {len(result)} characters", flush=True)

            if not result:
                print("❌ Ollama returned EMPTY response", flush=True)
                logger.error("Ollama returned empty response")
                return "[ERROR: Empty model response]"

            return result

        except Exception as e:
            logger.exception("Ollama generation failed: %s", e)
            print(f"❌ Ollama exception: {e}", flush=True)
            return f"[ERROR: {e}]"