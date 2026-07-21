import streamlit as st


def show_evaluation(metrics: dict, judge_report: str):
    """
    Display summary evaluation metrics.
    """

    if not metrics:
        return

    st.divider()
    st.subheader("📈 Summary Evaluation")

    # ---------------------------------
    # Basic Metrics
    # ---------------------------------

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Compression",
        f"{metrics['compression']:.2f}%"
    )

    c2.metric(
        "Original Words",
        metrics["original_words"]
    )

    c3.metric(
        "Summary Words",
        metrics["summary_words"]
    )

    c4, c5 = st.columns(2)

    c4.metric(
        "Reading Time",
        f"{metrics['original_reading_time']} min"
    )

    c5.metric(
        "Time Saved",
        f"{metrics['reading_time_saved']} min"
    )

    st.divider()

    # ---------------------------------
    # ROUGE
    # ---------------------------------

    st.markdown("### 📑 ROUGE Scores")

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "ROUGE-1",
        f"{metrics['rouge1']:.4f}"
    )

    r2.metric(
        "ROUGE-2",
        f"{metrics['rouge2']:.4f}"
    )

    r3.metric(
        "ROUGE-L",
        f"{metrics['rougeL']:.4f}"
    )

    st.divider()

    # ---------------------------------
    # BERTScore
    # ---------------------------------

    st.markdown("### 🤖 BERTScore")

    b1, b2, b3 = st.columns(3)

    b1.metric(
        "Precision",
        f"{metrics['bert_precision']:.4f}"
    )

    b2.metric(
        "Recall",
        f"{metrics['bert_recall']:.4f}"
    )

    b3.metric(
        "F1 Score",
        f"{metrics['bert_f1']:.4f}"
    )

    # ---------------------------------
    # LLM Judge
    # ---------------------------------

    if judge_report:

        st.divider()

        with st.expander("🧠 LLM-as-a-Judge", expanded=False):

            st.markdown(judge_report)