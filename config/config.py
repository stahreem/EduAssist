"""
EduAssist Configuration File
"""

# -----------------------------
# Supported Languages
# -----------------------------

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "ur": "Urdu",
    "te": "Telugu"
}

DEFAULT_LANGUAGE = "en"

# -----------------------------
# PDF
# -----------------------------

SUPPORTED_FILE_TYPES = [".pdf"]

# -----------------------------
# Summarization
# -----------------------------

CHUNK_SIZE = 1000

MIN_SUMMARY_LENGTH = 50

MAX_SUMMARY_LENGTH = 200

# -----------------------------
# Ollama
# -----------------------------

OLLAMA_MODEL = "qwen3:1.7b"

OLLAMA_TEMPERATURE = 0.2

# -----------------------------
# Future OCR
# -----------------------------

OCR_ENGINE = "PaddleOCR"

# -----------------------------
# Translation
# -----------------------------

DEFAULT_TRANSLATION_LANGUAGE = "English"