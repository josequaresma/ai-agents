from agents.analyst import run_analyst
from agents.advocate import run_advocate
from agents.strategist import run_strategist
from agents.critic import run_critic
from agents.synthesizer import run_synthesizer

context = open("prompts/context.txt").read()

analyst_output = run_analyst(context)
advocate_output = run_advocate(context)
strategist_output = run_strategist(context)
critic_output = run_critic(context)

final_decision = run_synthesizer(
    context,
    analyst_output,
    advocate_output,
    strategist_output,
    critic_output
)

print("FINAL DECISION:\n", final_decision)