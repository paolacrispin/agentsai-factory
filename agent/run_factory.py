from agent.factory import AgentSpec, generate_agent

def main():
    spec = AgentSpec(
        name="solana-log-agent",
        description="Logs Solana devnet activity periodically",
        goal="Monitor Solana devnet blocks and log activity"
    )

    generate_agent(spec)

if __name__ == "__main__":
    main()
