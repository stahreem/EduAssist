from models.ollama_client import OllamaClient

client = OllamaClient()


def judge_summary(original_text, summary):
    """
    Ask the LLM to evaluate the generated summary.
    """

    prompt = f"""
You are an expert evaluator for educational summaries.

Evaluate the summary based on the original document.

Original Document:
{original_text}

---------------------------------------

Generated Summary:
{summary}

---------------------------------------

Score the summary from 1 to 10 for:

1. Relevance
2. Coverage
3. Clarity
4. Coherence
5. Factual Accuracy

Then provide:

Overall Score: X/10

Strengths:
- ...

Weaknesses:
- ...

Suggestions:
- ...

Return only the evaluation.
"""

    evaluation = client.generate(prompt)

    if not evaluation.strip():
        return "LLM evaluation unavailable."

    return evaluation