"""
Main evaluation controller.
"""

from evaluation.metrics import calculate_basic_metrics
from evaluation.rouge_score import calculate_rouge


def evaluate_summary(original_text, summary):

    results = {}

    # Basic Metrics
    results.update(
        calculate_basic_metrics(original_text, summary)
    )

    # ROUGE
    results.update(
        calculate_rouge(original_text, summary)
    )

    # Import BERTScore only when needed
    from evaluation.bertscore import calculate_bertscore

    results.update(
        calculate_bertscore(
            original_text,
            summary
        )
    )

    return results