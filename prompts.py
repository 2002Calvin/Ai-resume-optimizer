def get_resume_prompt(resume_text):
    return f"""Please enhance the following resume for clarity, formatting, and professionalism.
Keep it suitable for Applicant Tracking Systems.
Resume:
\"\"\"
{resume_text}
\"\"\""""
