import time
import logging

from models.ollama_client import OllamaClient
from summarization.prompts import SUMMARY_PROMPT
from summarization.chunker import split_into_chunks
from summarization.mearger import merge_summaries

logger = logging.getLogger(__name__)

client = OllamaClient()


def summarize_text(text):
    """
    Generate a document summary using chunk-based summarization.
    """

    if not text.strip():
        logger.warning("Empty input received for summarization.")
        return ""

    total_start = time.time()

    logger.info("=" * 60)
    logger.info("Starting document summarization...")
    logger.info("=" * 60)

    chunks = split_into_chunks(text)

    logger.info("Document divided into %d chunks.", len(chunks))

    summaries = []

    # -----------------------------------
    # Summarize each chunk
    # -----------------------------------

    for i, chunk in enumerate(chunks):

        logger.info(
            "Summarizing chunk %d/%d (%d words)...",
            i + 1,
            len(chunks),
            len(chunk.split())
        )

        chunk_start = time.time()

        prompt = SUMMARY_PROMPT.format(text=chunk)

        try:

            chunk_summary = client.generate(prompt)

            if chunk_summary.strip():

                summaries.append(chunk_summary)

                logger.info(
                    "Chunk %d completed in %.2f sec (%d chars).",
                    i + 1,
                    time.time() - chunk_start,
                    len(chunk_summary)
                )

            else:

                logger.warning(
                    "Chunk %d returned an EMPTY summary.",
                    i + 1
                )

        except Exception:

            logger.exception(
                "Error while summarizing chunk %d",
                i + 1
            )

    # -----------------------------------
    # Merge summaries
    # -----------------------------------

    if not summaries:

        logger.error("No valid chunk summaries generated.")
        return ""

    logger.info(
        "Merging %d chunk summaries...",
        len(summaries)
    )

    merge_start = time.time()

    final_summary = merge_summaries(summaries)

    merge_time = time.time() - merge_start

    if not final_summary.strip():

        logger.error("Merged summary is EMPTY.")
        return ""

    logger.info(
        "Merge completed in %.2f sec.",
        merge_time
    )

    logger.info(
        "Final summary length: %d characters.",
        len(final_summary)
    )

    logger.info(
        "Total summarization time: %.2f sec.",
        time.time() - total_start
    )

    logger.info("=" * 60)
    logger.info("Summary generation completed.")
    logger.info("=" * 60)

    return final_summary