def evaluate_summary(original_text, summary):
    """
    Evaluate AI-generated summary.
    """

    original_words = len(original_text.split())
    summary_words = len(summary.split())

    compression = (
        ((original_words - summary_words) / original_words) * 100
        if original_words > 0 else 0
    )

    reading_time = round(summary_words / 200, 2)

    return {
        "original_words": original_words,
        "summary_words": summary_words,
        "compression": round(compression, 2),
        "reading_time": reading_time
    }