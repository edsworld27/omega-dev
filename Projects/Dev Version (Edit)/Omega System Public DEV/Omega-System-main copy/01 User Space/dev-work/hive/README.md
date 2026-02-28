# Hive — AI Communication Layer

This directory enables AI-to-AI and AI-to-human communication via Omega Claw.

## Directory Structure

```
hive/
├── ai_inbox/      ← Jobs/requests FROM users TO Claude
├── ai_outbox/     ← Reports/responses FROM Claude TO users
├── ai_state/      ← Current agent status
├── blockers/      ← When Claude needs user input
└── progress/      ← Detailed progress logs
```

## How It Works

1. **User sends message** via Telegram
2. **Omega Claw** writes job to `ai_inbox/`
3. **Claude** reads inbox on startup, picks up job
4. **Claude** writes progress to `ai_outbox/`
5. **Omega Claw** reads outbox, sends to Telegram
6. **User** gets update on phone

## Files

- `AGENT_STATUS.md` — Current Claude agent state
- `JOB-*.md` — Incoming job requests
- `REPORT-*.md` — Outgoing progress reports
- `BLOCKED-*.md` — Claude needs user input
- `ANSWER-*.md` — User responses to blockers

## Protocol

See `CONSTITUTION/AI_PROTOCOL.xml` for full specification.

---
*Created by Omega Claw installation*
