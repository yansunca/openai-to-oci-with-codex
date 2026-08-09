# Codex Migration Task: OpenAI SDK → OCI Generative AI

This repository starts as a normal application using the OpenAI Python SDK.

Migrate it to work with **OCI Generative AI through OCI's OpenAI-compatible API**.

## Requirements

1. Preserve the `openai` Python SDK.
2. Preserve the OpenAI Responses API (`client.responses.create(...)`).
3. Preserve the application's behavior.
4. Make the smallest reasonable application-code diff.
5. Replace provider-specific OpenAI configuration with environment variables for:
   - `OCI_GENAI_API_KEY`
   - `OCI_OPENAI_BASE_URL`
   - `OCI_MODEL`
6. Update `.env.example` with safe OCI placeholders only. Never include real credentials.
7. Add `verify_oci.py` that:
   - uses the OpenAI Python SDK
   - reads the OCI configuration from environment variables / local `.env`
   - makes one small real request through OCI's OpenAI-compatible API
   - prints a clear success response
8. Keep unit tests mocked. Unit tests must not contact OpenAI, OCI, or any external service.
9. Update tests only as necessary to preserve coverage of application behavior.
10. Never print, copy, commit, or expose API keys, tokens, private keys, `.env` contents, or other credentials.

## Validation

After making the changes:

- run the unit tests
- show the resulting `git diff`
- summarize which files changed or were added
- explain why each change was necessary

Do not add OCI infrastructure, Terraform, containers, OKE, Vault, networking, or deployment resources. This POC is only about migrating the application to OCI's OpenAI-compatible API.
