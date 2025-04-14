from openai import OpenAI

client = OpenAI()

def run_synthesizer(context, analyst, advocate, strategist, critic):
    prompt = open("prompts/synthesis_prompt.txt").read()
    inputs = f"ANALYST:\n{analyst}\n\nADVOCATE:\n{advocate}\n\nSTRATEGIST:\n{strategist}\n\nCRITIC:\n{critic}"
    response = client.chat.completions.create(model="gpt-4.1",
    messages=[{"role": "user", "content": f"{context}\n\n{prompt}\n\n{inputs}"}],
    temperature=0.3)
    return response.choices[0].message.content