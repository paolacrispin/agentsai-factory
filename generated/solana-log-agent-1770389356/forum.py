import os
import requests

API_BASE = "https://agents.colosseum.com/api"

def create_forum_post(title: str, body: str, tags=None):
    api_key = os.environ["COLOSSEUM_API_KEY"]

    res = requests.post(
        f"{API_BASE}/forum/posts",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "title": title,
            "body": body,
            "tags": tags or ["ai", "infra", "progress-update"],
        },
        timeout=15,
    )

    res.raise_for_status()
    return res.json()
