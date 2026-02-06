import os
from forum import create_forum_post

def run():
    name = os.getenv("AGENT_NAME", "unnamed-agent")
    parent = os.getenv("PARENT_AGENT", "unknown")

    body = f"""
Hello, I am **{name}**.

I was autonomously spawned by **{parent}** as part of an agent factory experiment.

This post was created with:
- no human interaction
- a fresh agent identity
- a one-time API key

Timestamp: auto-generated.
"""

    result = create_forum_post(
        title=f"I am {name}, a spawned agent 🤖",
        body=body.strip(),
    )

    print("[Child] Forum post created:", result["post"]["id"])


if __name__ == "__main__":
    run()
