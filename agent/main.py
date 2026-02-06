from agent.colosseum import get_status, get_heartbeat
from agent.wallet import get_wallet, get_balances, transfer_sol_devnet

def main():
    status = get_status()
    print("=== STATUS ===")
    print(status)

    heartbeat = get_heartbeat()
    print("\n=== HEARTBEAT (preview) ===")
    print(heartbeat[:600])

    wallet = get_wallet()
    print("\n=== AGENT WALLET ===")
    print(wallet)

    balances = get_balances()
    print("\n=== BALANCES ===")
    print(balances)

    # === FASE 3: ON-CHAIN EVIDENCE (DEVNET) ===
    # Self-transfer a la propia wallet (válido en Solana)
    tx = transfer_sol_devnet(
        to="rUpqFfLWLWCNEiHqbUkSx8rrVqdP1S2YXRMxiRbM24G",
        lamports=1_000_000  # 0.001 SOL
    )

    print("\n=== DEVNET TX ===")
    print(tx)


if __name__ == "__main__":
    main()
