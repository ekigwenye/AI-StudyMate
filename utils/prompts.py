def summary_prompt(text, length, style):
    return f"""
You are an expert educational assistant.

Summarize the following study material.

Summary Length:
{length}

Summary Style:
{style}

Please organize your response using these headings:

# Summary

# Key Takeaways
- Bullet points

# Important Terms
- Term: Definition

# Practice Questions
1.
2.
3.

# Study Tip

Study Material:

{text}
"""

