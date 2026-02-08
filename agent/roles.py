AGENT_ROLES = {
    "logger": {
        "description": "Observes and logs on-chain or off-chain activity",
        "base_reputation": 10,
    },
    "monitor": {
        "description": "Monitors systems and emits alerts",
        "base_reputation": 15,
    },
    "executor": {
        "description": "Executes actions on-chain or off-chain",
        "base_reputation": 20,
    },
    "generic": {
        "description": "Generic agent with no special role",
        "base_reputation": 0,
    },
}
