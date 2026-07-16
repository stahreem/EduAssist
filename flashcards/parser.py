def parse_flashcards(raw_text):

    """
    Convert Gemma response into flashcard list.
    """

    flashcards = []

    blocks = raw_text.strip().split("\n\n")

    for block in blocks:

        lines = block.strip().split("\n")

        if len(lines) < 2:
            continue

        question = lines[0].replace("Q:", "").strip()
        answer = lines[1].replace("A:", "").strip()

        flashcards.append({

            "question": question,

            "answer": answer

        })

    return flashcards