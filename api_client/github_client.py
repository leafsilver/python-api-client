import requests


BASE_URL = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def get_repository(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()
    return response.json()