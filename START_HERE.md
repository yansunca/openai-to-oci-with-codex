# Start Here

This repo shows how to move a small OpenAI SDK app to OCI's OpenAI-compatible API with the smallest possible code change.

Read order:
1. `README.md`
2. `START_HERE.md`
3. `prompts/migrate-to-oci.md`

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

## How to get your OCI GenAI values

You need these environment variables:

```bash
OCI_GENAI_API_KEY=...
OCI_OPENAI_BASE_URL=...
OCI_MODEL=...
```

### 1) Get `OCI_GENAI_API_KEY`

Create an OCI Generative AI API key in the OCI Console.

High-level steps:
1. Sign in to the OCI Console.
2. Open **Generative AI**.
3. Go to **API Keys**.
4. Click **Create API key**.
5. Select the compartment for this demo.
6. Give the key a name.
7. Create it.
8. Copy the secret right away and store it securely.

Do **not** commit the real key to GitHub.

### 2) Get `OCI_OPENAI_BASE_URL`

Use the OpenAI-compatible OCI endpoint for your region. The pattern is:

```text
https://inference.generativeai.<REGION>.oci.oraclecloud.com/openai/v1
```

Example:

```bash
OCI_OPENAI_BASE_URL=https://inference.generativeai.us-chicago-1.oci.oraclecloud.com/openai/v1
```

### 3) Get `OCI_MODEL`

Pick a model that is available in your OCI region. The easiest way is to open your OCI Generative AI project or setup page and copy the model name shown in the generated usage example.

Example shape:

```bash
OCI_MODEL=<model-id-from-your-oci-setup>
```

## Create your local `.env`

Copy the example file:

```bash
cp .env.example .env
```

Then edit `.env` so it looks like this:

```bash
OCI_GENAI_API_KEY=<your-secret-api-key>
OCI_OPENAI_BASE_URL=https://inference.generativeai.<your-region>.oci.oraclecloud.com/openai/v1
OCI_MODEL=<your-model-id>
```

## Verify your settings

Run the verification script before you try the app:

```bash
python verify_oci.py
```

It checks that the required variables are present and prints the values in a safe, redacted form.

## What not to do

- Do not commit secrets.
- Do not paste API keys into GitHub.
- Do not rewrite the app if a config change is enough.

## Goal

Run the app once before migration, ask Codex to update the repo, then run it again against OCI.
