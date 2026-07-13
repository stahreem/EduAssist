import sys
from pathlib import Path
import time

# --------------------------------------------------
# Add Project Root
# --------------------------------------------------
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# --------------------------------------------------
# Imports
# --------------------------------------------------
import streamlit as st

from preprocessing.pdf_reader import extract_text_from_pdf
from preprocessing.cleaner import clean_text
from preprocessing.language_detector import detect_language
from summarization.summarizer import summarize_text

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="EduAssist",
    page_icon="📚",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("📚 EduAssist")

st.sidebar.info("""
### Version 0.1

### Completed Modules

✅ PDF Upload

✅ Text Extraction

✅ Text Cleaning

✅ Language Detection

✅ AI Summarization
""")

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📚 EduAssist")
st.subheader("Multilingual AI Learning Assistant")

st.write("""
Upload a PDF document to:

- 📄 Extract Text
- 🌍 Detect Language
- 🧹 Clean Text
- 🤖 Generate AI Summary
""")

# --------------------------------------------------
# Upload PDF
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

# ==================================================
# Processing
# ==================================================

if uploaded_file is not None:

    st.success("✅ PDF Uploaded Successfully")
    st.write(f"**Filename:** {uploaded_file.name}")

    progress = st.progress(0)
    status = st.empty()

    try:

        # --------------------------------------------------
        # Extraction
        # --------------------------------------------------

        status.text("📄 Extracting text from PDF...")

        start = time.time()

        extracted_text = extract_text_from_pdf(uploaded_file)

        extraction_time = time.time() - start

        progress.progress(20)

        # --------------------------------------------------
        # Empty PDF Check
        # --------------------------------------------------

        if not extracted_text.strip():

            st.error("❌ No readable text found.")

            st.info("""
This PDF appears to be scanned or image-based.

OCR support (PaddleOCR / Surya OCR) will be added in the next version.
""")

            st.stop()

        # --------------------------------------------------
        # Language Detection
        # --------------------------------------------------

        status.text("🌍 Detecting language...")

        start = time.time()

        language_code, language_name = detect_language(extracted_text)

        detection_time = time.time() - start

        progress.progress(40)

        # --------------------------------------------------
        # Cleaning
        # --------------------------------------------------

        status.text("🧹 Cleaning text...")

        start = time.time()

        cleaned_text = clean_text(extracted_text)

        cleaning_time = time.time() - start

        progress.progress(60)

        # --------------------------------------------------
        # Summarization
        # --------------------------------------------------

        status.text("🤖 Generating AI summary...")

        start = time.time()

        summary = summarize_text(cleaned_text)

        summary_time = time.time() - start

        progress.progress(100)

        status.success("✅ Processing Complete")

    except Exception as e:

        st.error(f"An error occurred:\n\n{e}")

        st.stop()
        for i, chunk in enumerate(chunks):

            print("=" * 50)
            print(f"Processing Chunk {i+1} of {len(chunks)}")
            print(f"Words in Chunk: {len(chunk.split())}")
            print("=" * 50)

            prompt = SUMMARY_PROMPT.format(text=chunk)

            chunk_summary = client.generate(prompt)

            summaries.append(chunk_summary)
    # ==================================================
    # Processing Times
    # ==================================================

    st.subheader("⚡ Processing Time")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Extraction", f"{extraction_time:.2f}s")
    c2.metric("Detection", f"{detection_time:.2f}s")
    c3.metric("Cleaning", f"{cleaning_time:.2f}s")
    c4.metric("Summary", f"{summary_time:.2f}s")

    # ==================================================
    # Statistics
    # ==================================================

    original_words = len(extracted_text.split())
    cleaned_words = len(cleaned_text.split())
    summary_words = len(summary.split())

    compression = (
        ((original_words - summary_words) / original_words) * 100
        if original_words > 0 else 0
    )

    reading_time = round(original_words / 200)

    st.subheader("📊 Document Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Language", language_name)
    col2.metric("Original Words", original_words)
    col3.metric("Summary Words", summary_words)
    col4.metric("Compression", f"{compression:.1f}%")
    col5.metric("Reading Time", f"{reading_time} min")

    # ==================================================
    # Tabs
    # ==================================================

    tab1, tab2, tab3 = st.tabs([
        "📝 AI Summary",
        "📄 Extracted Text",
        "🧹 Cleaned Text"
    ])

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    with tab1:

        st.markdown("### AI Generated Summary")

        st.markdown(summary)

    # --------------------------------------------------
    # Extracted Text
    # --------------------------------------------------

    with tab2:

        st.text_area(
            "Extracted Text",
            extracted_text,
            height=500
        )

    # --------------------------------------------------
    # Cleaned Text
    # --------------------------------------------------

    with tab3:

        st.text_area(
            "Cleaned Text",
            cleaned_text,
            height=500
        )

    # ==================================================
    # Upcoming Features
    # ==================================================

    with st.expander("🚀 Upcoming Features"):

        st.markdown("""
### Planned Features

- ✅ Chunk-based Summarization
- ✅ OCR for Scanned PDFs
- ✅ Keyword Extraction
- ✅ Flashcards
- ✅ Quiz Generation
- ✅ Ask Questions from PDF (RAG)
- ✅ Translation
- ✅ Mind Maps
- ✅ AI Tutor
- ✅ Summary Quality Evaluation
- ✅ Export Summary (PDF / DOCX)
""")
        

# status.info("📄 Extracting text...")
# extracted_text = extract_text_from_pdf(uploaded_file)
# progress.progress(15)

# status.success("✅ Text extracted")
# status.info("🌍 Detecting language...")
# language_code, language_name = detect_language(extracted_text)
# progress.progress(30)

# status.success(f"✅ Language detected: {language_name}")
# status.info("🧹 Cleaning text...")
# cleaned_text = clean_text(extracted_text)
# progress.progress(45)

# status.success("✅ Text cleaned")
# status.success("🎉 Summary generated successfully!")
# progress.progress(100)