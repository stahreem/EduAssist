QUIZ_PROMPT = """
You are an AI teacher.

Read the following educational summary and generate exactly 5 multiple-choice questions.

Rules:

- Each question must have four options.
- Only one option should be correct.
- Questions should test understanding, not memorization.
- Do not ask duplicate questions.

Return ONLY the following format.

Question: ...

A. ...

B. ...

C. ...

D. ...

Answer: A

Return ONLY the option letter (A, B, C, or D).

Do NOT write:
Answer: Paris
Answer: Option A
Answer: A. Paris

Summary:

{text}
"""