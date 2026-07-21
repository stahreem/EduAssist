import streamlit as st


def show_sidebar():
    st.sidebar.title("📚 EduAssist")

    st.sidebar.info("""
### Version 1.0

### Completed Modules

✅ PDF Upload

✅ Text Extraction

✅ Text Cleaning

✅ Language Detection

✅ AI Summarization

✅ Keyword Extraction

✅ Quiz Generation

✅ Flashcards

✅ Translation

### Upcoming

⬜ Mind Map

⬜ RAG Chat

⬜ OCR Support

⬜ Export to PDF / DOCX
""")