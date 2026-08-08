from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class AppConfig:
    api_key: str
    base_url: str
    model: str
    timeout_seconds: int = 60


def load_config() -> AppConfig:
    api_key = os.environ.get("OCI_GENAI_API_KEY", "").strip()
    base_url = os.environ.get("OCI_OPENAI_BASE_URL", "").strip()
    model = os.environ.get("OCI_MODEL", "").strip()
    timeout_raw = os.environ.get("OCI_TIMEOUT_SECONDS", "60").strip()

    missing = [
        name
        for name, value in [
            ("OCI_GENAI_API_KEY", api_key),
            ("OCI_OPENAI_BASE_URL", base_url),
            ("OCI_MODEL", model),
        ]
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing)
        )

    try:
        timeout_seconds = int(timeout_raw)
    except ValueError as exc:
        raise RuntimeError("OCI_TIMEOUT_SECONDS must be an integer") from exc

    return AppConfig(
        api_key=api_key,
        base_url=base_url,
        model=model,
        timeout_seconds=timeout_seconds,
    )


def build_client(config: AppConfig) -> Any:
    from openai import OpenAI

    return OpenAI(
        api_key=config.api_key,
        base_url=config.base_url,
        timeout=config.timeout_seconds,
    )


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
        print("Usage: python app.py <question>", file=sys.stderr)
        return 2

    question = " ".join(argv[1:]).strip()
    answer = ask(question)
    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
