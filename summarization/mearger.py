from models.ollama_client import OllamaClient

client = OllamaClient()


def merge_summaries(summaries):
    """
    Merge chunk summaries into a final concise summary.
    Optimized for low-memory laptops.
    """

    # Remove empty summaries
    summaries = [s for s in summaries if s and not s.startswith("[ERROR")]

    if not summaries:
        return "Failed to generate summary."

    # If only one chunk, no need to merge
    if len(summaries) == 1:
        return summaries[0]

    merged_text = "\n\n".join(summaries)

    prompt = f"""
Combine these section summaries into ONE concise study note.

Requirements:
- Use headings.
- Use bullet points.
- Remove repetition.
- Keep important concepts only.
- Keep the final answer under 250 words.

Section Summaries:
{merged_text}
"""

    return client.generate(prompt)