import os
import sys

from openai import OpenAI


def get_client() -> OpenAI:
    return OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
    )


def ask(question: str) -> str:
    client = get_client()
    response = client.responses.create(
        model=os.environ["OPENAI_MODEL"],
        input=question,
    )
    return response.output_text


def main(argv: list[str]) -> int:
    question = " ".join(argv[1:]) or "Why does API compatibility matter?"
    print(ask(question))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
