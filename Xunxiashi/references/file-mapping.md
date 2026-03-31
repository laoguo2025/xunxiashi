# Xunxiashi File Mapping

This is the internal routing map from the 20 build questions and 5 post-build prompts into real OpenClaw files.

## Source Of Truth

Important behavior must end in real files, not only in:

- chat history
- temporary summaries
- verbal promises

## Build Question Mapping

### A. Let The Shrimp Understand You

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q1-Q5 | `USER.md` | user identity, basic profile, role, needs, and work context |

### B. What Kind Of Shrimp Life I Will Have

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q6-Q10 | `IDENTITY.md` and `SOUL.md` | shrimp persona, companion style, visible tone, mistake style, disliked tone |

### C. How I Should Work

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q11-Q15 | `AGENTS.md` | first step, ambiguity handling, sync style, obstacle handling, delivery format |

### D. How Much Authority I Have

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q16-Q20 | `openclaw.json`, `TOOLS.md`, `SOUL.md` | file permissions, critical config permissions, skill-install judgment, confirmation gates, secrecy boundaries |

## Post-Build Follow-Up Mapping

| Item | Usually write to | Meaning |
| --- | --- | --- |
| Follow-Up 1 | `MEMORY.md`, `AGENTS.md` | write-before-remember discipline |
| Follow-Up 2 | `AGENTS.md`, `TOOLS.md` | file/link intake must ask whether to learn |
| Follow-Up 3 | `HEARTBEAT.md`, `BOOT.md`, hook config | startup recovery with `boot-md` |
| Follow-Up 4 | `HEARTBEAT.md`, daily memory, hook config | `/new` recovery with `session-memory` |
| Follow-Up 5 | `HEARTBEAT.md`, cron or heartbeat config | daily workspace inspection and evolution |

## Memory Routing Rules

### Write To Daily Memory First When

- the information is new
- the user just said it
- it mainly supports short-term continuity
- it may still evolve

### Write To Durable Memory When

- the same preference appears repeatedly
- the rule is clearly long-term
- the information should survive restarts and future sessions

### Upgrade To Primary Rule Files When

- the information changes default behavior
- the information affects safety
- the information affects protocol, tone, or tool-use defaults

## "Remembered" Claim Rule

Never say the equivalent of:

- remembered
- saved
- will follow this next time

unless at least one of these is already true:

- a write to daily memory succeeded
- a write to durable memory succeeded
- a write to a primary rule file succeeded

If writing fails, say so directly and state what did not persist.

## Resume State Requirements

To support interruption and resume, state tracking must remember:

- selected mode: `叠加` or `覆盖`
- last completed build question
- last completed follow-up prompt
- files already written
- whether the sequence is in `build_brain`, `post_build_config`, `train_brain`, or `maintain_brain`
