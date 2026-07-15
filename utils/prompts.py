def summary_prompt(text, length, style):
    return f"""
You are AI StudyMate, an expert educational assistant.

Analyze the study material below.

Generate a {length.lower()} summary using a {style.lower()} writing style.

Return your response using the following format exactly.

# 📖 Summary
Write a clear and accurate summary.

# 🔑 Key Takeaways
Provide 5 concise bullet points.

# 📚 Important Terms
List important terms with a short explanation for each.

# ❓ Practice Questions
Generate 5 practice questions based on the material.

# 💡 Study Tip
Provide one useful study tip to help the student remember the content.

Study Material:

{text}
"""


def quiz_prompt(text, number, difficulty, question_type):
    return f"""
You are AI StudyMate.

Create exactly {number} {difficulty.lower()} {question_type.lower()} questions.

Instructions:
- Number every question.
- If Multiple Choice, provide four options (A, B, C and D).
- After every question, provide the correct answer.
- Use only the information from the study material.

Study Material:

{text}
"""


def flashcard_prompt(text, number):
    return f"""
You are AI StudyMate.

Generate exactly {number} study flashcards.

Format every flashcard exactly like this:

### Flashcard 1

Question:
...

Answer:
...

### Flashcard 2

Question:
...

Answer:
...

Use only information from the study material.

Study Material:

{text}
"""


def key_terms_prompt(text):
    return f"""
You are AI StudyMate.

Extract the most important terms from the study material.

For each term provide:

• The Term
• A simple definition
• Why it is important

Study Material:

{text}
"""


def study_plan_prompt(text, days):
    return f"""
You are AI StudyMate.

Create a realistic {days}-day study plan.

For each day include:
- Topics to study
- Estimated study time
- Practice task
- Revision task

Study Material:

{text}
"""


def tutor_prompt(text, question):
    return f"""
You are AI StudyMate.

Use ONLY the study material below to answer the student's question.

Study Material:

{text}

Student Question:

{question}

Provide a clear, beginner-friendly explanation.
"""