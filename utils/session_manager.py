import streamlit as st


def initialize_session():

    defaults = {

        "summary": None,
        "keywords": None,
        "quiz": None,
        
        "cleaned_text": None,
        "extracted_text": None,

        "language_code": None,
        "language_name": None,

        "flashcards": None,
        "mindmap": None,
        "translation": None,
        "chat_history": [],
        "current_file": None,
        "processing_time": {},
        "active_tool": "summary",
        "current_file": None,
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value