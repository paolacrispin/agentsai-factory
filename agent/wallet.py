import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE = os.getenv("AGENTWALLET_API_BASE")
USERNAME = os.getenv("AGENTWALLET_USERNAME")
TOKEN = os.getenv("AGENTWALLET_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def get_wallet():
    r = requests.get(
        f"{BASE}/wallets/{USERNAME}",
        headers=HEADERS,
        timeout=20
    )
    r.raise_for_status()
    return r.json()

def get_balances():
    # NOTA: este endpoint no refleja SOL devnet (limitación conocida)
    r = requests.get(
        f"{BASE}/wallets/{USERNAME}/balances",
        headers=HEADERS,
        timeout=20
    )
    r.raise_for_status()
    return r.json()

def transfer_sol_devnet(to: str, lamports: int):
    """
    Ejecuta una transferencia mínima en Solana devnet usando AgentWallet.
    amount debe ir en lamports (string).
    """
    r = requests.post(
        f"{BASE}/wallets/{USERNAME}/actions/transfer-solana",
        headers=HEADERS,
        json={
            "to": to,
            "amount": str(lamports),
            "asset": "sol",
            "network": "devnet"
        },
        timeout=20
    )
    r.raise_for_status()
    return r.json()
