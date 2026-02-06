import json
from pathlib import Path

STORE = Path("state/agents.json")
STORE.parent.mkdir(exist_ok=True)

def list_agents():
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text())

def save_agent(agent):
    agents = list_agents()
    if any(a["agentId"] == agent["agentId"] for a in agents):
        return
    agents.append(agent)
    STORE.write_text(json.dumps(agents, indent=2))
