from models.ollama_client import OllamaClient
from summarization.prompts import SUMMARY_PROMPT
from summarization.chunker import split_into_chunks
from summarization.mearger import merge_summaries

client = OllamaClient()


def summarize_text(text):

    # Split document into chunks
    chunks = split_into_chunks(text)

    print(f"\nDocument divided into {len(chunks)} chunks.\n")

    summaries = []

    for i, chunk in enumerate(chunks):

        print("=" * 50)
        print(f"Summarizing Chunk {i+1}/{len(chunks)}")
        print("=" * 50)

        prompt = SUMMARY_PROMPT.format(text=chunk)

        chunk_summary = client.generate(prompt)

        summaries.append(chunk_summary)

    print("\nMerging summaries...\n")

    final_summary = merge_summaries(summaries)

    return final_summary