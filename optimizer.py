import openai
from prompts import get_resume_prompt

def optimize_resume(text, api_key):
    openai.api_key = api_key
    prompt = get_resume_prompt(text)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI resume editor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
