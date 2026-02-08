from agent.factory import AgentSpec, generate_agent, register_and_run_child
from agent.store import save_agent
import time


def spawn_agent(parent_agent="AgentSai", root_agent="AgentSai", role="logger"):
    spec = AgentSpec(
        name=f"solana-log-agent-{int(time.time())}",
        description="Logs Solana devnet activity",
        goal="Monitor Solana devnet blocks",
        role=role,
    )

    # 1. Genera estructura del hijo
    generate_agent(spec)

    # 2. Registra + ejecuta el hijo (fuente de verdad)
    child = register_and_run_child(spec, parent_agent=parent_agent, root_agent=root_agent,)

    # 3. Persistencia directa, sin mutar el objeto
    save_agent(child)

    return child
