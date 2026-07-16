import streamlit as st
from keybert import KeyBERT

print("Loading KeyBERT Model...")

kw_model = KeyBERT(model="all-MiniLM-L6-v2")

print("KeyBERT Loaded Successfully")

@st.cache_resource
def extract_keywords(text):

    if not text:
        return []

    # -------------------------
    # Decide keyword count
    # -------------------------

    word_count = len(text.split())

    if word_count < 1000:
        top_n = 10

    elif word_count < 3000:
        top_n = 15

    elif word_count < 6000:
        top_n = 20

    else:
        top_n = 25

    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1,3),
        stop_words="english",
        top_n=top_n,
        use_mmr=True,
        diversity=0.7
    )

    cleaned_keywords = []

    for keyword, score in keywords:

        if keyword.isdigit():
            continue

        if len(keyword) < 3:
            continue

        cleaned_keywords.append(keyword)

    return cleaned_keywords