# Start Here

This repo shows how to move a small OpenAI SDK app to OCI's OpenAI-compatible API with the smallest possible code change.

Read order:
1. `README.md`
2. `prompts/migrate-to-oci.md`
3. `START_HERE.md`

## What to know

- **OpenAI SDK**: the client library used by the app.
- **Base URL**: the endpoint the SDK sends requests to.
- **API key**: the secret used to authenticate.
- **Model**: the LLM name the app calls.

## What you need

- Python 3.10+
- an OCI compartment
- an OCI GenAI API key
- an OCI OpenAI-compatible base URL
- a valid OCI model name

## What not to do

- Do not commit secrets.
- Do not paste API keys into GitHub.
- Do not rewrite the app if a config change is enough.

## Goal

Run the app once before migration, ask Codex to update the repo, then run it again against OCI.
