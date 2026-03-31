# Xunxiashi Hook Setup

This file explains how the recovery-related defaults in `Xunxiashi` become real OpenClaw behavior.

`Xunxiashi` may describe some behaviors as product defaults, but OpenClaw only performs them when the correct official hooks and workspace files are wired.

## Principle

Do not treat custom prose or custom JSON keys as enough.

Use official OpenClaw mechanisms:

- `boot-md` for startup-time recovery work
- `session-memory` for cross-session continuity around `/new`
- normal workspace file writes for durable rules and memory

## 1. Startup Recovery

Goal:

- notice that the gateway has started or restarted
- recover a short-term context summary
- optionally send a short IM notice

Recommended wiring:

1. enable the official `boot-md` hook
2. provide a `BOOT.md` file in the workspace
3. make `BOOT.md` read the latest short-term memory summary before composing any notice

What `BOOT.md` should usually do:

- recognize this is a startup context
- read the latest daily memory or recovery summary
- produce a short "I am back" notice only if the user's preference allows it
- avoid noisy long dumps

## 2. `/new` Recovery

Goal:

- preserve enough short-term continuity when the user starts a fresh conversation

Recommended wiring:

1. enable the official `session-memory` hook
2. write recent session summaries into daily memory
3. on the new session, restore only the recent useful summary instead of replaying raw long chat history

Recommended recovery source order:

1. latest recovery summary
2. latest daily memory
3. durable memory only when needed

## 3. Write-Before-Remember

This is not mainly a hook problem.

This is a skill discipline problem:

1. decide whether the content belongs in a primary rule file, `MEMORY.md`, or `memory/YYYY-MM-DD.md`
2. write successfully
3. only then tell the user it was remembered

Never say:

- "remembered"
- "saved"
- "I will follow that next time"

before the write succeeds.

## 4. Suggested Installation Note

If publishing this skill, document the following clearly:

- startup recovery requires `boot-md`
- `/new` recovery requires `session-memory`
- durable behavior changes require actual file writes

## 5. Example Assets

The example case in `docs/examples/xunxiashi-vertical-short-drama/workspace/` should include:

- `BOOT.md`
- `memory/YYYY-MM-DD.md`

so readers can see where recovery-related information actually lives.
