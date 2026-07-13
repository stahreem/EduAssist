def evaluate_summary(original_text, summary):

    original_words = len(original_text.split())
    summary_words = len(summary.split())

    compression = (
        (original_words - summary_words)
        / original_words
    ) * 100

    reading_time = summary_words / 200

    return {
        "compression": compression,
        "reading_time": reading_time
    }