import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE = os.getenv("COLOSSEUM_API_BASE")

HEADERS = {
    "Content-Type": "application/json",
}

def register_agent(agent_name: str):
    """
    Registers a new agent in Colosseum.
    Returns agent metadata + apiKey (DO NOT STORE apiKey).
    """
    r = requests.post(
        f"{API_BASE}/agents",
        headers=HEADERS,
        json={"name": agent_name},
        timeout=20
    )
    r.raise_for_status()
    return r.json()
