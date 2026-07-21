from config.config import CHUNK_SIZE


def split_into_chunks(text, chunk_size=CHUNK_SIZE):
    """
    Split text into chunks of approximately chunk_size words.
    Optimized for local 1-2B models.
    """

    if not text.strip():
        return []

    if chunk_size <= 0:
        raise ValueError(
            "chunk_size must be greater than zero."
        )

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks