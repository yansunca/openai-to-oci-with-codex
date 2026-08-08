from __future__ import annotations

import os
import sys
from urllib.parse import urlparse

REQUIRED_VARS = [
    "OCI_GENAI_API_KEY",
    "OCI_OPENAI_BASE_URL",
    "OCI_MODEL",
]


def _redact(value: str, visible: int = 4) -> str:
    if len(value) <= visible:
        return "*" * len(value)
    return value[:visible] + "*" * max(0, len(value) - visible)


def main() -> int:
    missing = [name for name in REQUIRED_VARS if not os.environ.get(name, "").strip()]
    if missing:
        print("Missing required environment variables:")
        for name in missing:
            print(f"- {name}")
        return 2

    api_key = os.environ["OCI_GENAI_API_KEY"].strip()
    base_url = os.environ["OCI_OPENAI_BASE_URL"].strip()
    model = os.environ["OCI_MODEL"].strip()

    parsed = urlparse(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        print("OCI_OPENAI_BASE_URL does not look like a valid URL")
        return 2

    print("OCI settings look ready:")
    print(f"- OCI_GENAI_API_KEY: {_redact(api_key)}")
    print(f"- OCI_OPENAI_BASE_URL: {base_url}")
    print(f"- OCI_MODEL: {model}")
    print("\nNext step: run the app or let Codex migrate it to OCI.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
