# OpenAI to OCI GenAI with Codex

Use Codex to migrate an existing application built with the OpenAI SDK to work with OCI Generative AI through OCI's OpenAI-compatible API.

The goal is a **small, understandable migration** rather than rewriting or redeploying the application.

## What This Demo Shows

```text
Existing OpenAI SDK App
          ↓
        Codex
          ↓
   Minimal Migration
          ↓
OCI OpenAI-Compatible API
          ↓
    OCI Generative AI
```

# Demo

## Step 1 — Clone the Repository

```bash
git clone https://github.com/yansunca/openai-to-oci-with-codex.git
cd openai-to-oci-with-codex
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Step 2 — Understand the Starting Application

Open `app.py`. It represents an application already built using the OpenAI Python SDK.

The goal is **not** to rewrite the application. Let Codex determine the smallest reasonable change needed to work with OCI Generative AI through OCI's OpenAI-compatible API.

## Step 3 — Ask Codex to Migrate the Application

Start Codex from the repository and use the **[Codex Migration Prompt](prompts/migrate-to-oci.md)**.

Key requirements:

- preserve the OpenAI SDK and application behavior
- make the smallest reasonable change
- move provider-specific settings to environment variables
- never print or commit credentials

Codex should also create `verify_oci.py` as a real OCI connectivity check and update `.env.example` with OCI placeholders.

After Codex finishes:

```bash
git diff
```

Reviewing this minimal diff is an important part of the demo.

## Step 4 — Configure OCI GenAI

Now configure the OCI Generative AI service that the migrated application will consume.

👉 **[OCI GenAI Setup Guide — START_HERE.md](START_HERE.md)**

The guide walks through obtaining:

```text
OCI_GENAI_API_KEY
OCI_OPENAI_BASE_URL
OCI_MODEL
```

Then:

```bash
cp .env.example .env
```

Add your OCI values to `.env`.

> **Never commit `.env`, API keys, tokens, or other credentials to GitHub.**

## Step 5 — Verify the Real OCI Connection

Codex creates `verify_oci.py` during Step 3. Run the generated script:

```bash
python verify_oci.py
```

This makes a **real inference request**:

```text
verify_oci.py
      ↓
OpenAI Python SDK
      ↓
OCI OpenAI-Compatible API
      ↓
OCI Generative AI
      ↓
Configured Model
```

A successful response confirms real OCI GenAI connectivity. Normal OCI GenAI usage and charges may apply.

## Step 6 — Run the Migrated Application

```bash
python app.py
```

```text
Local Application
       ↓
OpenAI SDK
       ↓
OCI OpenAI-Compatible API
       ↓
OCI Generative AI
       ↓
Selected Model
```

The application remains local. **After migration, OCI Generative AI provides the model inference service.**

## Testing

```bash
pytest
```

Unit tests use mocks and **do not contact OCI, OpenAI, or any external model service**. They require no OCI credentials and generate no OCI GenAI usage.

`pytest` verifies application behavior. The Codex-generated `python verify_oci.py` verifies **real OCI GenAI connectivity**.

## Demo in One Line

**Clone → Codex → Review Diff → Configure OCI → Verify OCI → Run**

## Security

Never commit `.env`, OCI GenAI API keys, OpenAI API keys, OCI private keys, access tokens, or session credentials.

## Why This Matters

Many applications already use the OpenAI SDK. OCI's OpenAI-compatible API provides a familiar programming interface, while Codex can help automate migration work.

**Existing OpenAI application + Codex migration + OCI Generative AI.**
