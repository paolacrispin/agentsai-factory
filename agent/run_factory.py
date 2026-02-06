from agent.factory import AgentSpec, generate_agent, register_and_run_child
from agent.store import save_agent
from datetime import datetime
import time


def spawn_agent():
    spec = AgentSpec(
        name=f"solana-log-agent-{int(time.time())}",
        description="Logs Solana devnet activity",
        goal="Monitor Solana devnet blocks"
    )

    # 1. Genera estructura y código del hijo
    generate_agent(spec)

    # 2. Registra el hijo y lo ejecuta
    child = register_and_run_child(spec)

    # 3. Persistencia mínima
    agent_record = {
        "name": child["name"],
        "agentId": child["agentId"],
        "forumPostId": child.get("forumPostId"),  # ✅ nombre correcto
        "createdAt": datetime.utcnow().isoformat(),
    }

    save_agent(agent_record)

    return agent_record


if __name__ == "__main__":
    result = spawn_agent()
    print("[Factory] Spawned:", result)
