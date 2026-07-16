import time

from preprocessing.pdf_reader import extract_text_from_pdf
from preprocessing.cleaner import clean_text
from preprocessing.language_detector import detect_language


def process_document(uploaded_file):

    start = time.time()
    extracted_text = extract_text_from_pdf(uploaded_file)
    extract_time = time.time() - start

    if not extracted_text.strip():
        raise Exception("No readable text found.")

    start = time.time()
    language_code, language_name = detect_language(extracted_text)
    detect_time = time.time() - start

    start = time.time()
    cleaned_text = clean_text(extracted_text)
    clean_time = time.time() - start

    return {
        "extracted_text": extracted_text,
        "cleaned_text": cleaned_text,
        "language_code": language_code,
        "language_name": language_name,
        "processing_time": {
            "extract": extract_time,
            "detect": detect_time,
            "clean": clean_time,
        }
    }