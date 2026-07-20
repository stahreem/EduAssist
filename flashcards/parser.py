def parse_flashcards(raw_text):

    flashcards = []

    blocks = raw_text.strip().split("\n\n")

    for block in blocks:

        question = ""
        answer = ""

        for line in block.splitlines():

            line = line.strip()

            if line.startswith("Q:"):
                question = line.replace("Q:", "").strip()

            elif line.startswith("A:"):
                answer = line.replace("A:", "").strip()

        if question and answer:

            flashcards.append({

                "question": question,

                "answer": answer

            })

    return flashcards