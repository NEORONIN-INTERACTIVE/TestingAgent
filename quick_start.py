"""
Quick start example - run your TestingAgent against the SimpleAgent baseline.
"""

from testing_agent import TestingAgent
from w4a import TridentIslandMultiAgentEnv, SimpleAgent
from SimulationInterface import Faction

# Create environment and agents
env = TridentIslandMultiAgentEnv()
my_agent = TestingAgent(Faction.LEGACY, env.config)
opponent = SimpleAgent(Faction.DYNASTY, env.config)
env.set_agents(my_agent, opponent)

# Run episode
obs, info = env.reset()
print(f"Episode started. Running up to 1000 steps...")

for step in range(1000):
    actions = {
        "legacy": my_agent.select_action(obs["legacy"]),
        "dynasty": opponent.select_action(obs["dynasty"])
    }
    obs, rewards, terminated, truncated, info = env.step(actions)
    
    if step % 100 == 0:
        print(f"Step {step}: rewards = {rewards}")
    
    if terminated["legacy"]:
        print(f"Episode ended at step {step}")
        break

print("Quick start completed!")

