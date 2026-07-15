import time

from preprocessing.pdf_reader import extract_text_from_pdf
from preprocessing.cleaner import clean_text
from preprocessing.language_detector import detect_language
from summarization.summarizer import summarize_text


def process_document(uploaded_file):
    """
    Runs the complete document processing pipeline.
    Returns all processed data as a dictionary.
    """

    result = {}

    # -----------------------------
    # Extract Text
    # -----------------------------
    start = time.time()

    extracted_text = extract_text_from_pdf(uploaded_file)

    result["extraction_time"] = time.time() - start

    # Empty PDF
    if not extracted_text.strip():
        raise Exception("No readable text found inside PDF.")

    # -----------------------------
    # Detect Language
    # -----------------------------
    start = time.time()

    language_code, language_name = detect_language(extracted_text)

    result["detection_time"] = time.time() - start

    # -----------------------------
    # Clean Text
    # -----------------------------
    start = time.time()

    cleaned_text = clean_text(extracted_text)

    result["cleaning_time"] = time.time() - start

    # -----------------------------
    # Summary
    # -----------------------------
    start = time.time()

    summary = summarize_text(cleaned_text)

    result["summary_time"] = time.time() - start

    # -----------------------------
    # Store Everything
    # -----------------------------
    result["extracted_text"] = extracted_text
    result["cleaned_text"] = cleaned_text
    result["summary"] = summary

    result["language_code"] = language_code
    result["language_name"] = language_name

    return result