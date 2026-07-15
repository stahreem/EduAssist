import time
import streamlit as st

from summarization.summarizer import summarize_text
from ui.tabs import show_tabs


def show_summary():

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

    # -------------------------
    # Display Summary
    # -------------------------

    if st.session_state.summary is not None:

        extracted_text = st.session_state.extracted_text
        cleaned_text = st.session_state.cleaned_text
        summary = st.session_state.summary

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

        a.metric("Language", st.session_state.language_name)
        b.metric("Words", original_words)
        c.metric("Summary Words", summary_words)
        d.metric("Compression", f"{compression:.1f}%")
        e.metric("Reading Time", f"{reading_time} min")

        show_tabs(
            extracted_text=extracted_text,
            cleaned_text=cleaned_text,
            summary=summary
        )

        with st.expander("🐞 Debug Session"):

            st.write(st.session_state)