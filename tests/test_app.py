import types

import app as demo_app


class FakeResponse:
    def __init__(self, content: str):
        self.choices = [
            types.SimpleNamespace(
                message=types.SimpleNamespace(content=content)
            )
        ]


class FakeChatCompletions:
    def __init__(self):
        self.calls = []

    def create(self, *, model, messages):
        self.calls.append({"model": model, "messages": messages})
        return FakeResponse("hello from mock")


class FakeClient:
    def __init__(self):
        self.chat = types.SimpleNamespace(completions=FakeChatCompletions())


def test_load_config(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "key")
    monkeypatch.setenv("OPENAI_MODEL", "demo-model")

    cfg = demo_app.load_config()

    assert cfg.api_key == "key"
    assert cfg.model == "demo-model"


def test_ask_uses_client(monkeypatch):
    cfg = demo_app.AppConfig(
        api_key="key",
        model="demo-model",
    )

    fake_client = FakeClient()

    monkeypatch.setattr(demo_app, "build_client", lambda _: fake_client)

    result = demo_app.ask("hello", config=cfg)

    assert result == "hello from mock"
    assert fake_client.chat.completions.calls[0]["model"] == "demo-model"
    assert fake_client.chat.completions.calls[0]["messages"] == [
        {"role": "user", "content": "hello"}
    ]


def test_load_config_rejects_missing_values(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    try:
        demo_app.load_config()
        assert False, "Expected RuntimeError"
    except RuntimeError as exc:
        assert "Missing required environment variables" in str(exc)
