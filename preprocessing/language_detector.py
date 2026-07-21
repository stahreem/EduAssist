from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

LANGUAGE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "ur": "Urdu",
    "te": "Telugu",
}


def detect_language(text: str) -> tuple[str, str]:

    if not text.strip():
        return "unknown", "Unknown"

    try:

        sample = text[:5000]

        language_code = detect(sample)

        language_name = LANGUAGE_MAP.get(
            language_code,
            language_code
        )

        return language_code, language_name

    except Exception:

        return "unknown", "Unknown"