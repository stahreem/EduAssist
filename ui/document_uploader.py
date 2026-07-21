import streamlit as st


def show_document_uploader():
    """
    Display PDF uploader.
    """

    return st.file_uploader(
        "📄 Upload a PDF document",
        type=["pdf"],
        help="Supported format: PDF"
    )