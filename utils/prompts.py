def summary_prompt(text, length, style):
    return f"""
You are an expert study assistant.

Analyze the study material below.

Create a {length.lower()} summary using a {style.lower()} writing style.

Return your response using EXACTLY this format.

## Summary
Write a clear summary.

## Key Takeaways
Provide 5 bullet points.

## Important Terms
List important terms with a short explanation.

## Practice Questions
Generate 5 practice questions.

## Study Tip
Give one useful study tip.

Study Material:

{text}
"""