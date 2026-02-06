from agent.factory import AgentSpec, generate_agent, register_child_agent

def main():
    spec = AgentSpec(
        name="solana-log-agent",
        description="Logs Solana devnet activity",
        goal="Monitor Solana devnet blocks"
    )

    generate_agent(spec)
    registration = register_child_agent(spec)

    print("[Factory] Spawn complete:", registration)

if __name__ == "__main__":
    main()
