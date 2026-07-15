import streamlit as st


def initialize_session():

    defaults = {

        "summary": None,
        "cleaned_text": None,
        "extracted_text": None,

        "language_code": None,
        "language_name": None,

        "keywords": None,
        "flashcards": None,
        "quiz": None,
        "mindmap": None,
        "translation": None,
        "chat_history": [],

        "processing_time": {}
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value