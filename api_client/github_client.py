import logging

import requests


logger = logging.getLogger(__name__)

BASE_URL = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def get_repository(owner, repo, timeout):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    logger.debug("准备请求 GitHub API：%s", url)

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=timeout,
    )

    logger.debug("GitHub API 返回状态码：%s", response.status_code)

    response.raise_for_status()
    return response.json()