import openai

def run_strategist(context):
    prompt = open("prompts/strategist_prompt.txt").read()
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{context}\n\n{prompt}"}],
        temperature=0.3
    )
    return response.choices[0].message.content