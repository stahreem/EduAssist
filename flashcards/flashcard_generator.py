import ollama
from flashcards.parser import parse_flashcards

def generate_flashcards(summary):

    """
    Generate flashcards from summary using Gemma.
    """

    prompt = f"""
You are an educational AI assistant.


Create between 5 and 10 high-quality flashcards.

Create exactly 10 flashcards.

Every flashcard must cover a unique concept.

Do not repeat information.

Return ONLY:

Q: ...
A: ...

No numbering.
No markdown.
No explanations.

Summary:

{summary}
"""

    response = ollama.chat(

        model="qwen3:1.7b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    raw_output = response["message"]["content"]

    flashcards = parse_flashcards(raw_output)

    return flashcards