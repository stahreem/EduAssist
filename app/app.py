import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
from preprocessing.pdf_reader import extract_text_from_pdf
import streamlit as st

from preprocessing.pdf_reader import extract_text_from_pdf


# Page Title
st.set_page_config(page_title="EduAssist")

st.title("📚 EduAssist")
st.subheader("Multilingual AI Learning Assistant")

st.write("Upload a PDF document to extract text.")


uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success("PDF Uploaded Successfully!")

    st.write("Filename:", uploaded_file.name)

    with st.spinner("Extracting text..."):

        extracted_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Text")

    st.text_area(
        label="PDF Content",
        value=extracted_text,
        height=400
    )