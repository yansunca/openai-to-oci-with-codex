# Codex Migration Task: OpenAI SDK → OCI Generative AI

This repository starts with a standard application using the OpenAI Python SDK.

Migrate it to work with **OCI Generative AI through OCI's OpenAI-compatible API** while keeping the application-code diff as small as reasonably possible.

## Must keep
- the `openai` Python SDK
- the Responses API (`client.responses.create(...)`)
- the application's behavior

## OCI configuration
Determine and implement all OCI-specific configuration required for the OCI OpenAI-compatible Responses API.

Use environment variables for:
- `OCI_GENAI_API_KEY`
- `OCI_OPENAI_BASE_URL`
- `OCI_GENAI_PROJECT_ID`
- `OCI_MODEL`

Configure the OpenAI client with the OCI Generative AI Project so the required project information is sent with Responses API requests.

Do not hard-code API keys, Project OCIDs, endpoints, model IDs, or other customer-specific values. Update `.env.example` with safe placeholders for every required post-migration setting.

Do **not** invent, guess, or select an OCI model ID. Model availability is region-specific. The user must supply `OCI_MODEL` after confirming an available model in their OCI region/Project (for example from the Project's **How to use** sample or Oracle's regional model-availability documentation).

## Verification
Generate `verify_oci.py` that:
- uses the standard OpenAI Python SDK
- uses the Responses API
- loads OCI configuration from environment variables / local `.env`
- includes the OCI Generative AI Project configuration required by the Responses API
- makes one small real OCI request
- prints a clear success message and model response
- never prints credentials

If the verifier requires an additional Python package, add it to `requirements.txt`.

## Tests
Keep unit tests mocked. They must not contact OpenAI, OCI, or any external service. Update tests only as necessary.

## Do not do
- do not replace the OpenAI SDK with the OCI SDK
- do not add Terraform, containers, OKE, Vault, networking, or deployment resources
- do not redesign the application
- do not print, copy, commit, or expose secrets or `.env` contents

## Validation
After migration:
1. install newly required dependencies
2. run the mocked unit tests
3. show the resulting `git diff`
4. summarize files changed or added
5. explain why each change was necessary

If real OCI credentials are unavailable, do not fabricate values or claim live verification succeeded.
