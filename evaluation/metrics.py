"""
Basic evaluation metrics for EduAssist.
"""


def calculate_basic_metrics(original_text, summary):
    """
    Calculate basic statistics for a generated summary.
    """

    original_words = len(original_text.split())
    summary_words = len(summary.split())

    compression = (
        ((original_words - summary_words) / original_words) * 100
        if original_words > 0 else 0
    )

    original_reading_time = round(original_words / 200, 2)
    summary_reading_time = round(summary_words / 200, 2)

    reading_time_saved = round(
        original_reading_time - summary_reading_time,
        2
    )

    return {
        "original_words": original_words,
        "summary_words": summary_words,
        "compression": round(compression, 2),
        "original_reading_time": original_reading_time,
        "summary_reading_time": summary_reading_time,
        "reading_time_saved": reading_time_saved,
    }