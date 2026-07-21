from models.ollama_client import OllamaClient

from quiz.prompts import QUIZ_PROMPT

client = OllamaClient()


def generate_quiz(summary):

    """
    Generate MCQs from summary using Ollama.
    """

    if not summary or len(summary.strip()) == 0:
        return ""

    prompt = QUIZ_PROMPT.format(text=summary)

    quiz = client.generate(prompt)
    print(quiz)

    return quiz