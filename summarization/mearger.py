from models.ollama_client import OllamaClient

client = OllamaClient()

def merge_summaries(summaries):

    merged_text = "\n\n".join(summaries)

    prompt = f"""
You are an expert document editor.

Below are summaries from different parts of a document.

Create ONE final summary.

Requirements:
- Remove duplicate information.
- Keep logical flow.
- Use headings.
- Use bullet points.
- Preserve important details.

Summaries:

{merged_text}
"""

    return client.generate(prompt)