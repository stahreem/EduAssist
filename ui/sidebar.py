import streamlit as st


def show_sidebar():

    st.sidebar.title("📚 EduAssist")

    st.sidebar.info("""
Version 0.2

Completed Modules

✅ PDF Upload
✅ Text Extraction
✅ Cleaning
✅ Language Detection
✅ AI Summary

Upcoming

⬜ KeyBERT
⬜ Flashcards
⬜ Quiz
⬜ Translation
⬜ RAG
""")