import streamlit as st

from translation.formatter import translation_widget
from translation.translator import translate_text


def show_translation(text, key):

    translated_key = f"translated_{key}"

    if translated_key not in st.session_state:
        st.session_state[translated_key] = {}

    clicked, language = translation_widget(key)

    if clicked:

        if language not in st.session_state[translated_key]:

            with st.spinner(f"🌍 Translating to {language}..."):

                translated = translate_text(
                    text,
                    language
                )

                st.session_state[translated_key][language] = translated

        else:

            st.info(
                f"Translation already available in {language}"
            )

    if language in st.session_state[translated_key]:

        st.subheader(f"🌍 Translation ({language})")

        st.text_area(
            "Translated Output",
            st.session_state[translated_key][language],
            height=250
        )