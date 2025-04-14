import openai

def run_critic(context):
    prompt = open("prompts/critic_prompt.txt").read()
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{context}\n\n{prompt}"}],
        temperature=0.4
    )
    return response.choices[0].message.content