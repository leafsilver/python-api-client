from api_client.github_client import get_repository


class FakeResponse:
    status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return {
            "full_name": "python/cpython",
        }


def fake_get(url, headers, timeout):
    assert url == "https://api.github.com/repos/python/cpython"
    assert headers == {
        "Accept": "application/vnd.github+json",
    }
    assert timeout == 5

    return FakeResponse()


def test_get_repository_returns_repository_data(monkeypatch):
    monkeypatch.setattr(
        "api_client.github_client.requests.get",
        fake_get,
    )

    repository = get_repository(
        "python",
        "cpython",
        5,
    )

    assert repository == {
        "full_name": "python/cpython",
    }