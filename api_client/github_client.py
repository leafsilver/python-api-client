import requests


BASE_URL = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def get_repository(owner, repo, timeout):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=timeout,
    )

    response.raise_for_status()
    return response.json()