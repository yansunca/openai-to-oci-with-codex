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
 Configure OCI GenAI
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
Open `app.py`. It is intentionally a standard OpenAI Python SDK application. The goal is not to preconfigure OCI or rewrite the app.

## Step 3 — Migrate with Codex in VS Code
Open the repository folder in **Visual Studio Code** with Codex enabled.

Ask Codex:

> Read `prompts/migrate-to-oci.md` and perform the migration described there.

See the full **[Codex Migration Prompt](prompts/migrate-to-oci.md)**.

Codex should preserve the OpenAI SDK and Responses API, add the OCI configuration required by the Responses API (including OCI Generative AI Project configuration), update `.env.example`, generate `verify_oci.py`, update dependencies if necessary, and keep unit tests mocked.

After Codex finishes, review the changes in VS Code Source Control or run:

```bash
git diff
```

## Step 4 — Set Up the Migrated Application

After reviewing the Codex-generated changes, create a virtual environment and install the **final migrated dependencies**:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Codex may add migration-specific dependencies to `requirements.txt`, so dependencies are installed **after the migration**.

## Step 5 — Configure OCI Generative AI
👉 **[Configure your OCI GenAI API key, endpoint, Project and model — START_HERE.md](START_HERE.md)**

The migrated configuration uses:

```text
OCI_GENAI_API_KEY
OCI_OPENAI_BASE_URL
OCI_GENAI_PROJECT_ID
OCI_MODEL
```

Keep real credentials in local `.env`; never commit it.

`OCI_MODEL` is region-specific. The setup guide explains how to confirm a supported model for your active OCI region/Project and copy its exact model ID. Codex should not guess the model ID.

## Step 6 — Verify the Real OCI Connection
Codex generates `verify_oci.py` during migration.

```bash
python verify_oci.py
```

This makes a real request through the OpenAI Python SDK to OCI's OpenAI-compatible API. A successful response confirms the migrated configuration can reach OCI Generative AI.

## Step 7 — Run the Migrated Application

```bash
python app.py "Why does API compatibility matter?"
```

The application remains local; OCI Generative AI provides the model service through its OpenAI-compatible API.

## Testing

```bash
python -m pytest
```

Unit tests use mocks and do not contact OCI, OpenAI, or any external model service.

## Demo in One Line
**Clone → VS Code → Codex → Review Diff → Install → Configure OCI → Verify → Run**

## Security
Never commit `.env`, API keys, OCI private keys, access tokens, or session credentials.

## Why This Matters
Many applications already use the OpenAI SDK. OCI's OpenAI-compatible API provides a familiar programming interface, while Codex can help automate the migration work.

**Existing OpenAI application + Codex-assisted migration + OCI Generative AI.**
