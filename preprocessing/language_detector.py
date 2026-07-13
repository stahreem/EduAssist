from langdetect import detect, DetectorFactory

# Makes language detection consistent every time
DetectorFactory.seed = 0

# Dictionary for readable language names
LANGUAGE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "ur": "Urdu",
    "te": "Telugu",
}


def detect_language(text):
    """
    Detect language from original extracted text.
    """

    try:

        language_code = detect(text)

        language_name = LANGUAGE_MAP.get(
            language_code,
            language_code
        )

        return language_code, language_name

    except Exception:

        return "unknown", "Unknown"