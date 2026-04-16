import os
BASE_URL = "https://api.github.com"

TOKEN = os.getenv("TOKEN") or os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}