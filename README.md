# OpenAI to OCI with Codex

A small Python demo that shows how an existing OpenAI SDK application can be migrated to OCI's OpenAI-compatible API with minimal code changes.

## What this repo demonstrates

- A tiny app built around the OpenAI Python SDK
- A Codex migration prompt that updates the app for OCI
- A clean config swap from OpenAI to OCI
- A smoke test that proves the app wiring works

## Repo shape

```text
app.py
requirements.txt
.env.example
.gitignore
AGENTS.md
prompts/migrate-to-oci.md
tests/test_app.py
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` with your OCI values:

```bash
OCI_GENAI_API_KEY=...
OCI_OPENAI_BASE_URL=...
OCI_MODEL=...
```

Then run the app:

```bash
python app.py "Hello from OCI"
```

## How the demo works

1. Start with a normal OpenAI SDK app.
2. Ask Codex to migrate the repo with the smallest possible diff.
3. Update the environment variables for OCI.
4. Run the same app against OCI's OpenAI-compatible endpoint.

## Codex prompt

See `prompts/migrate-to-oci.md`.

## Notes

- Secrets are never committed.
- The app reads its configuration from environment variables.
- The tests use mocks so they do not call any external service.

## Testing vs. Real OCI Verification

### Unit tests

Run:

```bash
pytest
```

The unit tests use mocks. They **do not call OpenAI, OCI Generative AI, or any other external service**.

This means:

- no OCI credentials are required
- no model tokens are consumed
- no OCI GenAI usage is generated
- the tests are safe to run locally or in GitHub Actions

### Real OCI GenAI verification

After configuring your OCI GenAI credentials and settings, run:

```bash
python verify_oci.py
```

Unlike the unit tests, this command makes a **real API request**:

```text
Local verify_oci.py
        |
        v
OpenAI Python SDK
        |
        v
OCI OpenAI-compatible API
        |
        v
OCI Generative AI
        |
        v
Configured model
```

A successful response confirms that the application can consume OCI Generative AI through its OpenAI-compatible API.

Because this is a real inference request, normal OCI Generative AI usage and charges may apply.

Never commit your real `OCI_GENAI_API_KEY` or `.env` file to GitHub.
