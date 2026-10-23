import argparse
import logging

import requests

from api_client.github_client import get_repository


logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="查询 GitHub 仓库信息",
    )

    parser.add_argument(
        "owner",
        help="仓库所有者，例如 python",
    )

    parser.add_argument(
        "repo",
        help="仓库名称，例如 cpython",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=10,
        help="请求超时秒数，默认 10",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="显示详细运行日志",
    )

    return parser.parse_args()


def configure_logging(verbose):
    level = logging.DEBUG if verbose else logging.WARNING

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    logging.getLogger("urllib3").setLevel(logging.WARNING)


def main():
    args = parse_arguments()
    configure_logging(args.verbose)

    try:
        repository = get_repository(
            args.owner,
            args.repo,
            args.timeout,
        )

    except requests.exceptions.Timeout:
        logger.error("请求超时，请稍后重试。")

    except requests.exceptions.ConnectionError:
        logger.error("网络连接失败，请检查网络。")

    except requests.exceptions.HTTPError as error:
        logger.error("HTTP 请求失败：%s", error)

    except requests.exceptions.JSONDecodeError:
        logger.error("服务器返回的内容不是有效的 JSON。")

    except requests.exceptions.RequestException as error:
        logger.error("请求失败：%s", error)

    else:
        print(f"仓库名称：{repository['full_name']}")
        print(f"项目描述：{repository['description']}")
        print(f"主要语言：{repository['language']}")
        print(f"星标数量：{repository['stargazers_count']}")
        print(f"默认分支：{repository['default_branch']}")


if __name__ == "__main__":
    main()