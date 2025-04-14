from openai import OpenAI

client = OpenAI()

def run_analyst(context):
    prompt = open("prompts/analyst_prompt.txt").read()
    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": f"{context}\n\n{prompt}"}],
    temperature=0.2)
    return response.choices[0].message.content