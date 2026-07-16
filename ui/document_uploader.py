import streamlit as st


def show_document_uploader():

    return st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )