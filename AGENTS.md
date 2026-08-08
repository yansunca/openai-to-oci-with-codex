# AGENTS.md

This repository is intentionally small.

## Goals

- Preserve the OpenAI SDK usage pattern.
- Make the configuration provider-specific only through environment variables.
- Keep the migration diff as small as possible.
- Do not add infrastructure code unless it is required for the POC.

## Expected Codex behavior

When asked to migrate this repo:

1. Inspect `app.py` first.
2. Update environment variable names if needed.
3. Keep the app behavior unchanged.
4. Update tests if configuration keys change.
5. Summarize the diff clearly at the end.
