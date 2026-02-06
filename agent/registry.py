import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE = os.getenv("COLOSSEUM_API_BASE")
API_KEY = os.getenv("COLOSSEUM_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def register_agent(agent_name: str):
    """
    Registers a new agent in Colosseum.
    Returns agent metadata + apiKey (DO NOT STORE apiKey).
    """
    print("COLOSSEUM_API_BASE =", repr(API_BASE))
    print("COLOSSEUM_API_KEY =", "SET" if API_KEY else "MISSING")

    r = requests.post(
        f"{API_BASE}/agents",
        headers=HEADERS,
        json={"name": agent_name},
        timeout=20
    )
    r.raise_for_status()
    return r.json()
