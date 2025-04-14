from openai import OpenAI

client = OpenAI()

def run_strategist(context):
    prompt = open("prompts/strategist_prompt.txt").read()
    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": f"{context}\n\n{prompt}"}],
    temperature=0.3)
    return response.choices[0].message.content