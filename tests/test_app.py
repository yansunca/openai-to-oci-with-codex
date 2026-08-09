import types

import app as demo_app


class FakeResponses:
    def __init__(self):
        self.calls = []

    def create(self, *, model, input):
        self.calls.append({"model": model, "input": input})
        return types.SimpleNamespace(output_text="hello from mock")


class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()


def test_ask_uses_openai_responses_api(monkeypatch):
    fake_client = FakeClient()
    monkeypatch.setattr(demo_app, "get_client", lambda: fake_client)
    monkeypatch.setenv("OPENAI_MODEL", "demo-model")

    result = demo_app.ask("hello")

    assert result == "hello from mock"
    assert fake_client.responses.calls == [
        {"model": "demo-model", "input": "hello"}
    ]
