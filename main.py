import requests


API_URL = "https://api.github.com/repos/python/cpython"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def main():
    response = requests.get(
        API_URL,
        headers=HEADERS,
        timeout=10,
    )

    repository = response.json()

    print(f"HTTP 状态码：{response.status_code}")
    print(f"仓库名称：{repository['full_name']}")
    print(f"项目描述：{repository['description']}")
    print(f"主要语言：{repository['language']}")
    print(f"星标数量：{repository['stargazers_count']}")
    print(f"默认分支：{repository['default_branch']}")


if __name__ == "__main__":
    main()