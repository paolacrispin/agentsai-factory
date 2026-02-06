from fastapi import APIRouter
from agent.run_factory import spawn_agent
from agent.store import list_agents

router = APIRouter()

@router.get("/agents")
def get_agents():
    return list_agents()

@router.post("/agents/spawn")
def spawn():
    return spawn_agent()
