MCQ_PROMPT = """
You are an expert educator.

Using ONLY the context below, generate exactly {num_questions}
multiple-choice questions.

Difficulty: {difficulty}

Rules:

Rules:

- Generate exactly {num_questions} MCQs.
- Use ONLY the provided context.
- Do not hallucinate or invent information.
- Each question must have four options.
- Store the correct option letter in the field "answer" (A, B, C or D).
- Store the full text of the correct answer in the field "correct_option".
- Include a brief explanation based only on the context.

Context:

{context}
"""