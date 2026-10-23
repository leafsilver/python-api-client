import requests


API_URL = "https://api.github.com/repos/python/cpython"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def get_repository():
    response = requests.get(
        API_URL,
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status()
    return response.json()