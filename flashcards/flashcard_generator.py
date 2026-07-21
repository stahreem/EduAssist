import logging

from models.ollama_client import OllamaClient
from flashcards.prompts import FLASHCARD_PROMPT
from flashcards.parser import parse_flashcards

logger = logging.getLogger(__name__)

client = OllamaClient()


def generate_flashcards(summary):
    """
    Generate educational flashcards from the summary.
    Returns a list of dictionaries:
    [
        {
            "question": "...",
            "answer": "..."
        }
    ]
    """

    if not summary or not summary.strip():
        return []

    try:

        prompt = FLASHCARD_PROMPT.format(
            text=summary
        )

        raw_output = client.generate(prompt)

        flashcards = parse_flashcards(raw_output)

        return flashcards

    except Exception as e:

        logger.exception(
            "Flashcard generation failed: %s",
            e
        )

        return []