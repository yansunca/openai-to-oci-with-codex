from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from openai import OpenAI


@dataclass(frozen=True)
class AppConfig:
    api_key: str
    model: str


def load_config() -> AppConfig:
    import os

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("OPENAI_MODEL", "").strip()

    missing = [
        name
        for name, value in [
            ("OPENAI_API_KEY", api_key),
            ("OPENAI_MODEL", model),
        ]
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing)
        )

    return AppConfig(api_key=api_key, model=model)


def build_client(config: AppConfig) -> Any:
    return OpenAI(api_key=config.api_key)


def ask(question: str, *, config: Optional[AppConfig] = None) -> str:
    cfg = config or load_config()
    client = build_client(cfg)

    response = client.chat.completions.create(
        model=cfg.model,
        messages=[
            {"role": "user", "content": question},
        ],
    )

    choice = response.choices[0]
    message = getattr(choice, "message", None)
    content = getattr(message, "content", None)
    if content is None:
        raise RuntimeError("No content returned from model")
    return content


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python app.py <question>")
        return 1

    question = " ".join(argv[1:])
    answer = ask(question)
    print(answer)
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv))
