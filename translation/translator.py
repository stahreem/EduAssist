import ollama


def translate_text(text, target_language):

    """
    Translate text into the selected language.
    """

    if not text or len(text.strip()) == 0:
        return ""

    prompt = f"""
You are a professional translator.

Translate the following text into {target_language}.

Rules:
- Preserve the original meaning.
- Preserve formatting wherever possible.
- Do NOT summarize.
- Do NOT explain.
- Do NOT add extra information.
- Return ONLY the translated text.

Text:

{text}
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

    return response["message"]["content"].strip()