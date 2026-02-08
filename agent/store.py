import json
from pathlib import Path
from typing import Dict, List
from agent.roles import AGENT_ROLES

STORE = Path("state/agents.json")
STORE.parent.mkdir(exist_ok=True)


def list_agents() -> List[Dict]:
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text())


def save_agent(agent: Dict):
    """
    Persist a spawned agent.
    Enforces uniqueness by agentId.
    """
    agents = list_agents()

    if any(a["agentId"] == agent["agentId"] for a in agents):
        return  # already stored

    agents.append({
        "name": agent["name"],
        "agentId": agent["agentId"],
        "role": agent.get("role"),
        "parentAgent": agent.get("parentAgent"),
        "rootAgent": agent.get("rootAgent"),
        "forumPostId": agent.get("forumPostId"),
        "forumPostUrl": agent.get("forumPostUrl"),
        "createdAt": agent.get("createdAt"),
    })

    STORE.write_text(json.dumps(agents, indent=2))

def build_agent_tree():
    """
    Builds a parent -> children tree from stored agents.
    """
    agents = list_agents()

    by_id = {a["agentId"]: {**a, "children": []} for a in agents}
    roots = []

    for agent in by_id.values():
        parent = agent.get("parentAgent")

        if parent and parent != agent["name"]:
            # Parent is a logical name (AgentSai or future agent)
            # Attach only if parent exists as agentId later
            found_parent = next(
                (a for a in by_id.values() if a["name"] == parent),
                None
            )
            if found_parent:
                found_parent["children"].append(agent)
            else:
                roots.append(agent)
        else:
            roots.append(agent)

    return roots

def calculate_reputation(agent, all_agents):
    score = 0
    reasons = []

    # 1️⃣ Spawned (existence)
    score += 20
    reasons.append("spawned")

    # 2️⃣ Forum evidence
    if agent.get("forumPostId"):
        score += 20
        reasons.append("forum_post")

    # 3️⃣ Children propagation
    children = [
        a for a in all_agents
        if a.get("parentAgent") == agent["name"]
    ]

    if children:
        child_bonus = min(len(children) * 15, 45)
        score += child_bonus
        reasons.append(f"spawned {len(children)} agents")

    # 4️⃣ Root bonus (small, symbolic)
    if agent.get("rootAgent") == agent["name"]:
        score += 10
        reasons.append("root_agent")

    # 5️⃣ Role bonus
    role = agent.get("role", "generic")
    role_bonus = AGENT_ROLES.get(role, {}).get("base_reputation", 0)

    if role_bonus:
        score += role_bonus
        reasons.append(f"role:{role}")

    return {
        "score": min(score, 100),
        "signals": reasons
    }



def list_agents_with_reputation():
    agents = list_agents()
    enriched = []

    for agent in agents:
        rep = calculate_reputation(agent, agents)
        enriched.append({
            **agent,
            "reputation": rep
        })

    return enriched
