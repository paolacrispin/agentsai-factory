from fastapi import APIRouter
from agent.run_factory import spawn_agent
from agent.store import list_agents, save_agent
from datetime import datetime

router = APIRouter()

@router.get("/agents")
def get_agents():
    return list_agents()

@router.post("/agents/spawn")
def spawn():
    child = spawn_agent()

    save_agent({
        "name": child["name"],
        "agentId": child["agentId"],
        "createdAt": datetime.utcnow().isoformat()
    })

    return {"ok": True, "agent": child}
