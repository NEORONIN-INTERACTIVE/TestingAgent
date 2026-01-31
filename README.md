# TestingAgent

Template repository for the **Wargaming 4 All** competition.

Clone this repo, rename the package with something unique, implement your agent, and submit!

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```

## Usage

```python
from testing_agent import TestingAgent
from w4a import TridentIslandMultiAgentEnv, SimpleAgent, Config
from SimulationInterface import Faction

# Create environment and agents
env = TridentIslandMultiAgentEnv()
my_agent = TestingAgent(Faction.LEGACY, env.config)
opponent = SimpleAgent(Faction.DYNASTY, env.config)
env.set_agents(my_agent, opponent)

# Run episode
obs, info = env.reset()
for _ in range(1000):
    actions = {
        "legacy": my_agent.select_action(obs["legacy"]),
        "dynasty": opponent.select_action(obs["dynasty"])
    }
    obs, rewards, terminated, truncated, info = env.step(actions)
    if terminated["legacy"]:
        break
```

## How to Submit

1. Rename the package with a unique identifier  (`testing_agent/` --> `your_team_name/`)
2. Rename `TestingAgent` class to `YourTeamNameAgent`
3. Implement your logic in `select_action()`
4. Submit your package to the competition server

## Resources

- **Website**: [war.game](https://war.game)
- **Environment Repo**: [github.com/CodeMetalAI/w4a](https://github.com/CodeMetalAI/w4a)
- **Discord**: [Join for updates and questions!](https://discord.gg/wargame)

## Contact

- Sanjna — sanjna@codemetal.ai
- Erwin — erwin.devries@neoronin.co
