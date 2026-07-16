import ollama


def generate_flashcards(summary):

    """
    Generate flashcards from summary using Gemma.
    """

    prompt = f"""
You are an educational AI assistant.

Create between 5 and 10 high-quality flashcards.

Rules:
- Each flashcard must cover a different concept.
- Do not repeat questions.
- Do not paraphrase the same fact twice.
- Keep questions concise.
- Keep answers under 25 words.

Format EXACTLY like this:

Q: Question here
A: Answer here

Q: Question here
A: Answer here

Do not number them.
Do not add explanations.
Only return flashcards.

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

    return response["message"]["content"]