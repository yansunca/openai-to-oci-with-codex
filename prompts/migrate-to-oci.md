# Codex Migration Task: OpenAI SDK → OCI Generative AI

This repository starts with a standard application using the OpenAI Python SDK.

Migrate it to work with **OCI Generative AI through OCI's OpenAI-compatible API** while keeping the application-code diff as small as reasonably possible.

## Must keep
- the `openai` Python SDK
- the Responses API (`client.responses.create(...)`)
- the application's behavior

## OCI Authentication

Use OCI IAM user-principal authentication.

Configure the OpenAI client to use OCI request signing through `oci-openai`, with the user's OCI CLI profile from `~/.oci/config` and the `DEFAULT` profile unless another profile is explicitly selected.

The migrated application and verifier should use:
- the OpenAI Python SDK
- `httpx`
- `oci-openai`
- OCI request signing via user-principal authentication

Keep the Responses API flow intact and preserve the OpenAI SDK as the client library.

## OCI Configuration

Use environment variables for:
- `OCI_OPENAI_BASE_URL`
- `OCI_GENAI_PROJECT_ID`
- `OCI_MODEL`
- `OCI_CONFIG_PROFILE`

Configure the OpenAI client with the OCI Generative AI Project required by the Responses API.

Do not hard-code Project OCIDs, endpoints, model IDs, OCI config contents, fingerprints, private-key paths, or other customer-specific values.

Model availability is region-specific. Do not invent or guess `OCI_MODEL`; the user supplies a model confirmed for the selected OCI region/Project, preferably from the Project's **How to use** sample.

Update `.env.example` with safe placeholders for the required post-migration configuration.

## Dependencies

Add the dependencies required by the generated migration to `requirements.txt`, while preserving the OpenAI SDK dependency.

## Verification

Generate `verify_oci_iam.py` that:
- uses the standard OpenAI Python SDK
- uses OCI IAM user-principal authentication
- uses the configured OCI CLI profile
- reads endpoint, Project OCID, and model from normal process environment variables
- uses the Responses API
- makes one small real request
- prints a clear success message and model response
- never prints OCI credentials, signing-key material, or OCI config contents

The application and verifier should read normal process environment variables. They should not parse `.env` directly; the shell exports `.env` values before execution.

## Tests

Keep unit tests mocked and free of external API calls. Update tests only as necessary.

## Do not do
- do not replace the OpenAI SDK with the OCI SDK as the model client
- do not add Terraform, containers, OKE, Vault, networking, or deployment resources
- do not redesign the application
- do not expose `~/.oci/config`, OCI private keys, API keys, tokens, `.env` contents, or other credentials

## Validation

After migration:
1. install final dependencies
2. run mocked unit tests
3. show `git diff`
4. summarize files changed or added
5. explain why each change was necessary

If valid OCI IAM credentials are unavailable, do not fabricate values or claim live verification succeeded.
