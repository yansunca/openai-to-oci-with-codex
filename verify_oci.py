"""Make one real OCI GenAI request through the OpenAI-compatible API."""
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).with_name(".env"))

required = ["OCI_GENAI_API_KEY", "OCI_OPENAI_BASE_URL", "OCI_MODEL"]
missing = [k for k in required if not os.getenv(k)]
if missing:
    raise SystemExit("Missing: " + ", ".join(missing) + ". See START_HERE.md.")

client = OpenAI(
    api_key=os.environ["OCI_GENAI_API_KEY"],
    base_url=os.environ["OCI_OPENAI_BASE_URL"],
)

response = client.responses.create(
    model=os.environ["OCI_MODEL"],
    input="Reply with exactly: OCI connection successful",
)
print(response.output_text)
