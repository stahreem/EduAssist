from bert_score import score


def calculate_bertscore(reference, candidate):
    """
    Calculate semantic similarity using BERTScore.
    """

    try:

        P, R, F1 = score(
            [candidate],
            [reference],
            lang="en",
            verbose=False
        )

        return {
            "bert_precision": round(P.mean().item(), 4),
            "bert_recall": round(R.mean().item(), 4),
            "bert_f1": round(F1.mean().item(), 4),
        }

    except Exception as e:
        print(f"BERTScore Error: {e}")

        return {
            "bert_precision": 0,
            "bert_recall": 0,
            "bert_f1": 0,
        }