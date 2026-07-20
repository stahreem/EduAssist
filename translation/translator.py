from deep_translator import GoogleTranslator

from translation.languages import SUPPORTED_LANGUAGES


def translate_text(text, target_language):

    if not text.strip():
        return ""

    try:

        language_code = SUPPORTED_LANGUAGES[target_language]

        return GoogleTranslator(
            source="auto",
            target=language_code
        ).translate(text)

    except Exception as e:

        return f"Translation Error: {e}"