import streamlit as st


def show_processing_time():

    if st.session_state.summary is None:
        return

    t = st.session_state.processing_time

    st.subheader("⚡ Processing Time")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Extraction", f"{t['extract']:.2f}s")
    c2.metric("Detection", f"{t['detect']:.2f}s")
    c3.metric("Cleaning", f"{t['clean']:.2f}s")
    c4.metric("Summary", f"{t['summary']:.2f}s")