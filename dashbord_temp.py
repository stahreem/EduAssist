import time
import streamlit as st

from preprocessing.pdf_reader import extract_text_from_pdf
from preprocessing.cleaner import clean_text
from preprocessing.language_detector import detect_language
from summarization.summarizer import summarize_text

from ui.sidebar import show_sidebar
from ui.tabs import show_tabs
from utils.session_manager import initialize_session
from keywords.keyword_extractor import extract_keywords
from quiz.quiz_generator import generate_quiz
from quiz.parser import parse_quiz
from quiz.formatter import display_quiz

def run_dashboard():

    initialize_session()

    st.set_page_config(
        page_title="EduAssist",
        page_icon="📚",
        layout="wide"
    )

    show_sidebar()

    st.title("📚 EduAssist")
    st.subheader("Multilingual AI Learning Assistant")

    st.write("""
Upload a PDF document to

- 📄 Extract Text
- 🌍 Detect Language
- 🧹 Clean Text
- 🤖 Generate Summary
""")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    st.success("PDF Uploaded Successfully")

    progress = st.progress(0)
    status = st.empty()

    # ------------------------------
    # Process only once
    # ------------------------------

    if st.session_state.extracted_text is None:

        try:

            status.text("Extracting PDF...")

            start = time.time()

            extracted_text = extract_text_from_pdf(uploaded_file)

            extraction_time = time.time() - start

            progress.progress(20)

            if not extracted_text.strip():

                st.error("No readable text found.")
                st.stop()

            status.text("Detecting language...")

            start = time.time()

            language_code, language_name = detect_language(extracted_text)

            detection_time = time.time() - start

            progress.progress(40)

            status.text("Cleaning text...")

            start = time.time()

            cleaned_text = clean_text(extracted_text)

            cleaning_time = time.time() - start

            progress.progress(60)

            # status.text("Generating summary...")
            # start = time.time()
            # summary = summarize_text(cleaned_text)
            # summary_time = time.time() - start
            # progress.progress(100)
            # status.success("Completed")

            # ----------------------------
            # Save into session
            # ----------------------------

            st.session_state.extracted_text = extracted_text
            st.session_state.cleaned_text = cleaned_text
            # st.session_state.summary = summary

            st.session_state.language_name = language_name
            st.session_state.language_code = language_code

            st.session_state.processing_time = {
                "extract": extraction_time,
                "detect": detection_time,
                "clean": cleaning_time,
                # "summary": summary_time
            }

        except Exception as e:

            st.error(e)
            st.stop()

    extracted_text = st.session_state.extracted_text
    cleaned_text = st.session_state.cleaned_text
    summary = st.session_state.summary

    language_name = st.session_state.language_name

    times = st.session_state.processing_time

    st.divider()

    # ==========================================
    # Generate Summary Button
    # ==========================================

    if st.button("🤖 Generate Summary", use_container_width=True):

        if st.session_state.summary is None:

            with st.spinner("Generating Summary..."):

                start = time.time()

                summary = summarize_text(
                    st.session_state.cleaned_text
                )

                summary_time = time.time() - start

                st.session_state.summary = summary
                st.session_state.processing_time["summary"] = summary_time

            st.success("Summary Generated Successfully!")

        else:
            st.info("Summary already generated.")

    # ==========================================
    # Display Summary if available
    # ==========================================

    if st.session_state.summary is not None:

        extracted_text = st.session_state.extracted_text
        cleaned_text = st.session_state.cleaned_text
        summary = st.session_state.summary

        language_name = st.session_state.language_name
        times = st.session_state.processing_time

        st.subheader("⚡ Processing Time")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Extraction", f"{times['extract']:.2f}s")
        c2.metric("Detection", f"{times['detect']:.2f}s")
        c3.metric("Cleaning", f"{times['clean']:.2f}s")
        c4.metric("Summary", f"{times['summary']:.2f}s")

        original_words = len(extracted_text.split())
        summary_words = len(summary.split())

        compression = (
            (original_words - summary_words)
            / original_words
        ) * 100

        reading_time = round(original_words / 200)

        st.subheader("📊 Statistics")

        a, b, c, d, e = st.columns(5)

        a.metric("Language", language_name)
        b.metric("Words", original_words)
        c.metric("Summary Words", summary_words)
        d.metric("Compression", f"{compression:.1f}%")
        e.metric("Reading Time", f"{reading_time} min")

        show_tabs(
            extracted_text=extracted_text,
            cleaned_text=cleaned_text,
            summary=summary
        )

        with st.expander("🐞 Debug Session State"):

            st.write(st.session_state)

    st.divider()

    if st.button("🔑 Generate Keywords", use_container_width=True):

        if st.session_state.summary is None:
            st.warning("Please generate the summary first.")

        elif st.session_state.keywords is None:

            with st.spinner("Extracting Keywords..."):

                keywords = extract_keywords(
                    st.session_state.cleaned_text
                )

                st.session_state.keywords = keywords

            st.success("Keywords Generated Successfully!")

        else:

            st.info("Keywords already generated.")

        if st.session_state.keywords is not None:

            st.subheader("🔑 Extracted Keywords")

            cols = st.columns(4)

            for i, keyword in enumerate(st.session_state.keywords):

                cols[i % 4].success(keyword)

    st.divider()

    if st.button("📝 Generate Quiz", use_container_width=True):

        if st.session_state.summary is None:

            st.warning("Please generate the summary first.")

        elif st.session_state.quiz is None:

            with st.spinner("Generating Quiz..."):

                raw_quiz = generate_quiz(
                    st.session_state.summary
                )

                parsed_quiz = parse_quiz(raw_quiz)

                st.session_state.quiz = parsed_quiz

            st.success("Quiz Generated Successfully!")

        else:

            st.info("Quiz already generated.")      

        if st.session_state.quiz is not None:

            display_quiz(
                st.session_state.quiz
            )      