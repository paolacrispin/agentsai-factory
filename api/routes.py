from fastapi import APIRouter, Query
from agent.run_factory import spawn_agent
from agent.store import list_agents, build_agent_tree, list_agents_with_reputation
from datetime import datetime, timezone

router = APIRouter()

@router.get("/agents")
def get_agents():
    return list_agents()

@router.post("/agents/spawn")
def spawn(
    parent: str = Query(default="AgentSai"),
    role: str = Query(default="logger"),
):
    agent = spawn_agent(
        parent_agent=parent,
        root_agent="AgentSai",
        role=role,
    )

    agent["createdAt"] = datetime.fromtimestamp(
        agent["createdAt"], tz=timezone.utc
    ).isoformat()

    return agent

@router.get("/agents/tree")
def get_agent_tree():
    return build_agent_tree()

@router.get("/agents/reputation")
def get_agents_with_reputation():
    return list_agents_with_reputation()
