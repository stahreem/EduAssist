import streamlit as st
from keybert import KeyBERT
import logging

logger = logging.getLogger(__name__)

logger.info("Loading KeyBERT model...")

kw_model = KeyBERT(model="all-MiniLM-L6-v2")

logger.info("KeyBERT Loaded Successfully")


@st.cache_resource
def extract_keywords(text):
    """
    Extract important keywords from cleaned text
    using KeyBERT.
    """

    if not text:
        return []

    word_count = len(text.split())

    if word_count < 1000:
        top_n = 10
    elif word_count < 3000:
        top_n = 15
    elif word_count < 6000:
        top_n = 20
    else:
        top_n = 25

    try:
        keywords = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            stop_words="english",
            top_n=top_n,
            use_mmr=True,
            diversity=0.7
        )
    except Exception:
        logger.exception("Keyword extraction failed.")
        return []

    cleaned_keywords = []

    for keyword, score in keywords:

        if keyword.isdigit():
            continue

        if len(keyword) < 3:
            continue

        cleaned_keywords.append(keyword.strip())

    unique_keywords = list(dict.fromkeys(cleaned_keywords))

    return unique_keywords