import requests


API_URL = "https://api.github.com/repos/python/cpython"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def main():
    try:
        response = requests.get(
            API_URL,
            headers=HEADERS,
            timeout=10,
        )

        response.raise_for_status()
        repository = response.json()

    except requests.exceptions.Timeout:
        print("请求超时，请稍后重试。")

    except requests.exceptions.ConnectionError:
        print("网络连接失败，请检查网络。")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP 请求失败：{error}")

    except requests.exceptions.JSONDecodeError:
        print("服务器返回的内容不是有效的 JSON。")

    except requests.exceptions.RequestException as error:
        print(f"请求失败：{error}")

    else:
        print(f"HTTP 状态码：{response.status_code}")
        print(f"仓库名称：{repository['full_name']}")
        print(f"项目描述：{repository['description']}")
        print(f"主要语言：{repository['language']}")
        print(f"星标数量：{repository['stargazers_count']}")
        print(f"默认分支：{repository['default_branch']}")


if __name__ == "__main__":
    main()