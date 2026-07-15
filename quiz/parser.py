import re


def parse_quiz(raw_quiz):

    """
    Convert Ollama output into a list of dictionaries.
    """

    quizzes = []

    if not raw_quiz:
        return quizzes

    pattern = re.split(r"Question\s*:\s*", raw_quiz)

    for block in pattern:

        if block.strip() == "":
            continue

        lines = [
            line.strip()
            for line in block.split("\n")
            if line.strip()
        ]

        if len(lines) < 6:
            continue

        question = lines[0]

        options = []

        answer = ""

        for line in lines[1:]:

            if line.startswith(("A.", "B.", "C.", "D.")):
                options.append(line)

            elif line.lower().startswith("answer"):
                answer = line.split(":")[-1].strip()

        quizzes.append(
            {
                "question": question,
                "options": options,
                "answer": answer
            }
        )

    return quizzes