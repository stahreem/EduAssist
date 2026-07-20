import streamlit as st
from translation.languages import SUPPORTED_LANGUAGES

def translation_widget(key):
    st.write(f"Creating translation widget: {key}")   # Temporary debug
    language = st.selectbox(
        "Translate to",
        list(SUPPORTED_LANGUAGES.keys()),
        key=f"{key}_language"

    )

    button = st.button(
        "🌍 Translate",
        key=f"{key}_translate"

    )

    return button, language