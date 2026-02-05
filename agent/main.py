from agent.colosseum import get_status, get_heartbeat

def main():
    status = get_status()
    print("=== STATUS ===")
    print(status)

    heartbeat = get_heartbeat()
    print("\n=== HEARTBEAT (preview) ===")
    print(heartbeat[:600])

if __name__ == "__main__":
    main()
