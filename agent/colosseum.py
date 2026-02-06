import os
import requests
from dotenv import load_dotenv

load_dotenv()


API_BASE = os.getenv("COLOSSEUM_API_BASE")
API_KEY = os.getenv("COLOSSEUM_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def get_status():
    r = requests.get(f"{API_BASE}/agents/status", headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()

def get_heartbeat():
    r = requests.get("https://colosseum.com/heartbeat.md", timeout=20)
    r.raise_for_status()
    return r.text
