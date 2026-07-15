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
    print("=" * 60)
    print("MERGE PROMPT")
    print("=" * 60)
    print(prompt[:2000])     # print first 2000 chars
    print("=" * 60)

    result = client.generate(prompt)

    print("MERGE RESULT:")
    print(repr(result))

    return result
    # return client.generate(prompt)