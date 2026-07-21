"""
ROUGE evaluation metrics.
"""

from rouge_score import rouge_scorer


def calculate_rouge(reference_text, generated_summary):
    """
    Calculate ROUGE-1, ROUGE-2 and ROUGE-L scores.
    """

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True
    )

    scores = scorer.score(
        reference_text,
        generated_summary
    )

    return {
        "rouge1": round(scores["rouge1"].fmeasure, 4),
        "rouge2": round(scores["rouge2"].fmeasure, 4),
        "rougeL": round(scores["rougeL"].fmeasure, 4),
    }