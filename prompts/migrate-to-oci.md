# Codex migration prompt

Review this OpenAI SDK application and make it OCI-ready with the smallest reasonable set of changes.

Requirements:
- Preserve the OpenAI SDK usage pattern.
- Switch provider-specific configuration to OCI environment variables.
- Keep application behavior unchanged.
- Add or update tests if necessary.
- Do not add infrastructure, deployment, or networking code.
- Summarize the minimal diff and explain how to run the app against OCI.

Target environment variables:
- `OCI_GENAI_API_KEY`
- `OCI_OPENAI_BASE_URL`
- `OCI_MODEL`
- `OCI_TIMEOUT_SECONDS` (optional)
