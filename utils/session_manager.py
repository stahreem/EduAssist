import streamlit as st


def initialize_session():
    """
    Initialize Streamlit session state with
    default values used throughout EduAssist.
    """
     
    defaults = {
        # AI Outputs
        "summary": None,
        "keywords": None,
        "quiz": None,
        "flashcards": None,
        
        # Document
        "cleaned_text": None,
        "extracted_text": None,
        "language_code": None,
        "language_name": None,

         # UI
        "active_tool": "summary",
        "processing_time": {},
        "current_file": None,

         # Translation Cache
        "translated_summary": {},
        "translated_keywords": {},
        "translated_quiz": {},
        "translated_flashcards": {},

        # Future Modules
        "mindmap": None,
        # "translation": None,
        "chat_history": [],

        "evaluation": None,
        "judge_report": None,
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value