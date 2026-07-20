import streamlit as st


def initialize_session():

    defaults = {

        "summary": None,
        "keywords": None,
        "quiz": None,
        "flashcards": None,
        
        "cleaned_text": None,
        "extracted_text": None,

        "language_code": None,
        "language_name": None,

        "mindmap": None,
        # "translation": None,
        "chat_history": [],
        "processing_time": {},
        "active_tool": "summary",
        "current_file": None,

        "translated_summary": {},
        "translated_keywords": {},
        "translated_quiz": {},
        "translated_flashcards": {},
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value