def summary_prompt(text, length, style):
    return f"""
You are AI StudyMate, an expert educational assistant.

Analyze the study material below.

Generate a {length.lower()} summary using a {style.lower()} writing style.

Return your response using EXACTLY the following format.

# 📖 Summary
Write a clear, accurate and well-structured summary.

# 🔑 Key Takeaways
Provide 5 concise bullet points highlighting the most important ideas.

# 📚 Important Terms
List the important terms and provide a short explanation for each.

# ❓ Practice Questions
Generate 5 practice questions based on the study material.

# 💡 Study Tip
Provide one useful study tip to help the student remember the content.

Study Material:

{text}
"""


def quiz_prompt(text, number, difficulty, question_type):
    return f"""
You are AI StudyMate.

Generate exactly {number} {difficulty.lower()} {question_type.lower()} questions.

Instructions:
- Number every question.
- If the question type is Multiple Choice, provide four options (A, B, C and D).
- If the question type is True/False, provide the correct answer.
- If the question type is Short Answer, include the answer after each question.
- Use ONLY the information from the study material.

Study Material:

{text}
"""


def flashcard_prompt(text, number):
    return f"""
You are AI StudyMate.

Create exactly {number} study flashcards.

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

Continue until all flashcards are created.

Use ONLY information from the study material.

Study Material:

{text}
"""


def key_terms_prompt(text):
    return f"""
You are AI StudyMate.

Extract the most important terms from the study material.

For each term include:

• Term
• Definition
• Why it is important

Return at least 10 important terms whenever possible.

Study Material:

{text}
"""


def tutor_prompt(text, question):
    return f"""
You are AI StudyMate.

Answer the student's question using ONLY the study material below.

Study Material:

{text}

Student Question:

{question}

Instructions:
- Explain in simple language.
- Use examples where appropriate.
- If the answer is not found in the study material, clearly state that.
"""


def study_plan_prompt(subject, days, hours, goal):
    return f"""
You are AI StudyMate, an expert study coach.

Create a personalized study plan.

Subject:
{subject}

Duration:
{days} days

Study Hours Per Day:
{hours}

Goal:
{goal}

Return your response using EXACTLY this format.

# 📅 Study Plan

## Overview
Write a short overview of the study plan.

## Daily Schedule

Day 1
- Topics
- Activities
- Practice

Day 2
- Topics
- Activities
- Practice

Continue until Day {days}.

## Revision Tips
Provide 5 revision tips.

## Motivation
End with one motivational message.
"""


def notes_prompt(topic):
    return f"""
You are AI StudyMate.

Write comprehensive study notes about:

{topic}

Include:

# Introduction

# Main Concepts

# Important Facts

# Examples

# Summary

# Practice Questions
"""


def explain_prompt(topic):
    return f"""
You are AI StudyMate.

Explain the following topic in simple language suitable for a university student.

Topic:

{topic}

Include:
- Definition
- Explanation
- Real-life example
- Key points
- Quick recap
"""