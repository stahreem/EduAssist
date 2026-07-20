from models.ollama_client import OllamaClient
from summarization.prompts import SUMMARY_PROMPT
from summarization.chunker import split_into_chunks
from summarization.mearger import merge_summaries

client = OllamaClient()


def summarize_text(text):
    print("Entered summarize_text")
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
        
        print(f"\nChunk {i+1} Summary:\n")
        # print(chunk_summary)
        print("-" * 50)

        summaries.append(chunk_summary)

    print("All chunks completed")

    print("Starting merge...")

    final_summary = merge_summaries(summaries)

    print("Merge completed")
    # print(final_summary)

    return final_summary