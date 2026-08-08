# OCI GenAI Setup Guide

Complete this setup **after Codex performs the migration in Step 3 of the [main README](README.md)**.

You need:

```text
OCI_GENAI_API_KEY=...
OCI_OPENAI_BASE_URL=...
OCI_MODEL=...
```

Never commit the real API key or `.env`.

## 1. Get `OCI_GENAI_API_KEY`

In the OCI Console:

1. Open **Generative AI**.
2. Go to **API Keys**.
3. Create an API key in the compartment used for the demo.
4. Select the appropriate model/scope access.
5. Copy the generated secret immediately and store it securely.

This is an OCI Generative AI API key, not a normal OCI API signing private key.

## 2. Get `OCI_OPENAI_BASE_URL`

The endpoint follows:

```text
https://inference.generativeai.<region>.oci.oraclecloud.com/openai/v1
```

Example:

```text
https://inference.generativeai.us-chicago-1.oci.oraclecloud.com/openai/v1
```

Use the region where your selected Generative AI model is available.

## 3. Get `OCI_MODEL`

In OCI Generative AI, choose a model available in your selected region. If your project/setup has a **How to use** example, copy the exact model identifier shown there.

## 4. Create `.env`

```bash
cp .env.example .env
```

Edit it:

```text
OCI_GENAI_API_KEY=<your-secret-api-key>
OCI_OPENAI_BASE_URL=https://inference.generativeai.<your-region>.oci.oraclecloud.com/openai/v1
OCI_MODEL=<your-model-id>
```

Check that `.env` is ignored:

```bash
git status --ignored
```

## Next Step

Return to the **[main README](README.md)** and continue with **Step 5 — Verify the Real OCI Connection**.
