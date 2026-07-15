# ui/statistics.py

import streamlit as st


def show_statistics():
    """Display document statistics."""

    metrics = st.session_state.metrics

    st.subheader("📊 Document Statistics")

    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(2)

    # ----------------------------
    # Row 1
    # ----------------------------

    row1[0].metric(
        "🌍 Language",
        st.session_state.language_name
    )

    row1[1].metric(
        "📄 Pages",
        st.session_state.pages
    )

    row1[2].metric(
        "🤖 Model",
        "Gemini 2.5 Flash"
    )

    # ----------------------------
    # Row 2
    # ----------------------------

    row2[0].metric(
        "📝 Original Words",
        metrics["original_words"]
    )

    row2[1].metric(
        "📚 Summary Words",
        metrics["summary_words"]
    )

    row2[2].metric(
        "🧩 Chunks",
        st.session_state.total_chunks
    )

    # ----------------------------
    # Row 3
    # ----------------------------

    row3[0].metric(
        "📉 Compression",
        f'{metrics["compression"]}%'
    )

    row3[1].metric(
        "⏱ Reading Time",
        f'{metrics["reading_time"]} min'
    )