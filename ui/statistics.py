#  ui/statistics.py

import streamlit as st


def show_statistics():

    if st.session_state.summary is None:
        return

    extracted = st.session_state.extracted_text
    summary = st.session_state.summary

    original_words = len(extracted.split())
    summary_words = len(summary.split())

    compression = (
        (original_words - summary_words)
        / original_words
    ) * 100

    reading_time = round(original_words / 200)

    st.subheader("📊 Statistics")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Language",
        st.session_state.language_name
    )

    c2.metric(
        "Words",
        original_words
    )

    c3.metric(
        "Summary Words",
        summary_words
    )

    c4.metric(
        "Compression",
        f"{compression:.1f}%"
    )

    c5.metric(
        "Reading Time",
        f"{reading_time} min"
    )

# import streamlit as st


# def show_statistics():
#     """Display document statistics."""

#     metrics = st.session_state.metrics

#     st.subheader("📊 Document Statistics")

#     row1 = st.columns(3)
#     row2 = st.columns(3)
#     row3 = st.columns(2)

#     # ----------------------------
#     # Row 1
#     # ----------------------------

#     row1[0].metric(
#         "🌍 Language",
#         st.session_state.language_name
#     )

#     row1[1].metric(
#         "📄 Pages",
#         st.session_state.pages
#     )

#     row1[2].metric(
#         "🤖 Model",
#         "Gemini 2.5 Flash"
#     )

#     # ----------------------------
#     # Row 2
#     # ----------------------------

#     row2[0].metric(
#         "📝 Original Words",
#         metrics["original_words"]
#     )

#     row2[1].metric(
#         "📚 Summary Words",
#         metrics["summary_words"]
#     )

#     row2[2].metric(
#         "🧩 Chunks",
#         st.session_state.total_chunks
#     )

#     # ----------------------------
#     # Row 3
#     # ----------------------------

#     row3[0].metric(
#         "📉 Compression",
#         f'{metrics["compression"]}%'
#     )

#     row3[1].metric(
#         "⏱ Reading Time",
#         f'{metrics["reading_time"]} min'
#     )