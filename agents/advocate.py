from openai import OpenAI

client = OpenAI()

def run_advocate(context):
    prompt = open("prompts/advocate_prompt.txt").read()
    response = client.chat.completions.create(model="gpt-4.0",
    messages=[{"role": "user", "content": f"{context}\n\n{prompt}"}],
    temperature=0.8)
    return response.choices[0].message.content