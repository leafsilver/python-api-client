# Python GitHub API Client

一个用于学习 Python 工程实践的命令行 API 客户端。程序通过 GitHub REST API 查询公开仓库信息。

## 功能

- 根据仓库所有者和仓库名称查询 GitHub 仓库
- 显示仓库描述、主要语言、星标数量和默认分支
- 支持设置请求超时时间
- 支持显示详细调试日志
- 处理网络连接、请求超时、HTTP 状态码和 JSON 解析异常
- 使用 pytest 进行基础自动化测试

## 项目结构

```text
python-api-client/
├── api_client/
│   ├── __init__.py
│   └── github_client.py
├── tests/
│   └── test_github_client.py
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

- `main.py`：命令行程序入口和异常处理
- `api_client/github_client.py`：GitHub API 请求逻辑
- `tests/`：自动化测试
- `requirements.txt`：程序运行依赖
- `requirements-dev.txt`：开发和测试依赖

## 环境要求

- Python 3.12
- Git
- Linux 或 WSL

## 获取项目

```bash
git clone git@github.com:leafsilver/python-api-client.git
cd python-api-client
```

## 创建虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 安装依赖

只运行程序：

```bash
python -m pip install -r requirements.txt
```

进行开发和测试：

```bash
python -m pip install -r requirements-dev.txt
```

## 使用方法

查看帮助：

```bash
python main.py --help
```

查询仓库：

```bash
python main.py python cpython
```

设置请求超时时间：

```bash
python main.py python cpython --timeout 20
```

显示详细日志：

```bash
python main.py python cpython --verbose
```

组合使用：

```bash
python main.py python cpython --timeout 20 --verbose
```

## 运行测试

```bash
python -m pytest -v
```

## 参数说明

| 参数 | 作用 | 是否必填 |
| --- | --- | --- |
| `owner` | GitHub 仓库所有者 | 是 |
| `repo` | GitHub 仓库名称 | 是 |
| `--timeout` | 请求超时秒数，默认值为 10 | 否 |
| `--verbose` | 显示详细调试日志 | 否 |

## 注意事项

程序访问 GitHub 的公开 API，不需要登录。GitHub 会限制未认证请求的调用频率，短时间内反复请求可能收到 HTTP 403 响应。