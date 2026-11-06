# it_support_bot — IT Support Chatbot (Python)

Lives at: https://github.com/Tometri/it_support_bot

## What it does

Answers common IT support questions — password resets, VPN setup, known error codes — from a curated knowledge base, with cited sources.

## How it works

1. **Retrieval layer** — the user's question is scored against chunks of a curated KB; the best-matching chunk grounds the answer, and the source is cited.
2. **Deterministic fallback** — if no chunk scores high enough, or no LLM key is present, the bot falls back to a safe scripted answer instead of guessing.
3. **Escalation** — out-of-scope and sensitive requests are routed to a human-review / help-desk path.
4. **Interfaces** — a CLI and a lightweight `http.server` web UI on `127.0.0.1:8000`.

## Why it matters

Built for auditability and safe handoff to a help desk: documented limitations, human-review controls, and answers that can be traced back to a source — the same properties a real support tool needs.
