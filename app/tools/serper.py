import os
import requests
import json

SERPER_URL = "https://google.serper.dev/search"

def serper_search(query: str, k: int = 5) -> list[str]:
    payload = json.dumps({"q": query, "num": k})
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    response = requests.post(SERPER_URL, headers=headers, data=payload, timeout=10)
    response.raise_for_status()

    results = response.json().get("organic", [])
    return [r["snippet"] for r in results]
