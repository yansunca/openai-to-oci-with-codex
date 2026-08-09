# OpenAI to OCI GenAI with Codex

Use Codex to adapt an existing OpenAI SDK application to OCI Generative AI through OCI's OpenAI-compatible API.

The starting application contains no OCI-specific application code. Codex performs the OCI-specific changes while preserving the OpenAI SDK and Responses API.

## Demo Flow

```text
Existing OpenAI SDK App
          ↓
     Codex in VS Code
          ↓
     Review Git Diff
          ↓
 OCI IAM + GenAI Setup
          ↓
     Verify and Run
```

## Step 1 — Clone the Repository

```bash
git clone https://github.com/yansunca/openai-to-oci-with-codex.git
cd openai-to-oci-with-codex
```

Open the repository folder in **Visual Studio Code**.

## Step 2 — Understand the Starting Application

Open `app.py`. It is intentionally a standard OpenAI Python SDK application.

## Step 3 — Migrate with Codex in VS Code

Open Codex in VS Code and ask:

> Read `prompts/migrate-to-oci.md` and perform the migration described there.

See the full **[Codex Migration Prompt](prompts/migrate-to-oci.md)**.

Codex should preserve the OpenAI SDK and Responses API, add OCI IAM request signing, add OCI Project/endpoint/model configuration, update `.env.example`, generate `verify_oci_iam.py`, update dependencies, and keep unit tests mocked.

Review the changes:

```bash
git diff
```

## Step 4 — Set Up the Migrated Application

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Dependencies are installed after migration because Codex may update `requirements.txt`.

## Step 5 — Configure OCI

This POC uses **OCI IAM user-principal authentication** with your standard OCI CLI profile.

👉 **[Configure OCI IAM, endpoint, Project and model — START_HERE.md](START_HERE.md)**

The migrated application uses:

```text
OCI_OPENAI_BASE_URL
OCI_GENAI_PROJECT_ID
OCI_MODEL
OCI_CONFIG_PROFILE
```

Authentication comes from `~/.oci/config`; OCI credentials and private keys stay outside this repository. The profile name is read from `OCI_CONFIG_PROFILE` and defaults to `DEFAULT`.

After creating `.env`:

```bash
set -a
source .env
set +a
```

Set `OCI_CONFIG_PROFILE` in `.env` if you want to use a profile other than `DEFAULT`.

## Step 6 — Verify the Real OCI Connection

Codex generates `verify_oci_iam.py` during migration.

```bash
python verify_oci_iam.py
```

The real request path is:

```text
OpenAI Python SDK
       ↓
OCI IAM request signing
       ↓
OCI OpenAI-Compatible API
       ↓
OCI Generative AI
```

A successful response confirms the migrated OpenAI SDK configuration can reach OCI Generative AI using your OCI IAM identity.

## Step 7 — Run the Migrated Application

```bash
python app.py "Why does API compatibility matter?"
```

## Testing

```bash
python -m pytest
```

Unit tests use mocks and do not contact OCI, OpenAI, or any external model service.

## Demo in One Line

**Clone → VS Code → Codex → Review Diff → Install → Configure OCI IAM → Verify → Run**

## Security

Never commit `.env`, `~/.oci/config`, OCI private keys, API keys, access tokens, or session credentials.

## Why This Matters

Many applications already use the OpenAI SDK. OCI's OpenAI-compatible API provides a familiar programming interface, while Codex can help automate the migration work.

**Existing OpenAI application + Codex-assisted migration + OCI Generative AI.**
