import streamlit as st

from translation.formatter import translation_widget
from translation.translator import translate_text


def show_translation(text, key):
    
    st.write("show_translation called")
    st.write(f"key = {key}")
    translated_key = f"translated_{key}"

    # Store translations as a dictionary
    if translated_key not in st.session_state:
        st.session_state[translated_key] = {}

    clicked, language = translation_widget(key)

    if clicked:

        # Translate only if this language hasn't been translated yet
        if language not in st.session_state[translated_key]:

            with st.spinner(f"🌍 Translating to {language}..."):

                translated = translate_text(
                    text,
                    language
                )

                st.session_state[translated_key][language] = translated

        else:

            st.info(f"Translation already available in {language}")

    # Display the translation for the currently selected language
    if language in st.session_state[translated_key]:

        st.subheader(f"🌍 Translation ({language})")

        st.info(
            st.session_state[translated_key][language]
        )