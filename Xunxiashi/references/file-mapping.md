# Xunxiashi File Mapping

This is the internal routing map from user answers to real OpenClaw files.

## Source Of Truth

Important behavior must end in real files, not only in:

- chat history
- temporary summaries
- verbal promises

## File Responsibility Map

| File | Main responsibility | Typical inputs |
| --- | --- | --- |
| `openclaw.json` | safety and execution defaults | who the shrimp serves, what needs confirmation, high-risk policy |
| `USER.md` | user background and work context | preferred name, role, daily work, jargon, stable personal defaults |
| `IDENTITY.md` | outer speaking style | companion feel, tone, reply density, disliked wording |
| `SOUL.md` | inner temperament and boundaries | uncertainty handling, mistake style, hard no-go zones, interesting inner spirit |
| `AGENTS.md` | task protocol and delivery structure | first step, middle checkpoint, final check, delivery shape, ask-first boundary |
| `TOOLS.md` | source and tool-use preference | search-first vs ask-first, trusted sources, avoided sources, proof-of-write style |
| `HEARTBEAT.md` | proactive and recovery behavior | startup notice style, `/new` recovery style, rule promotion style, too-proactive line |
| `MEMORY.md` | durable knowledge and long-term defaults | stable preferences, durable facts, cross-session rules |
| `memory/YYYY-MM-DD.md` | daily and short-term context | fresh notes, unresolved follow-ups, recent working context, recovery summaries |
| `checklists/*.md` | recurring operational flows | stable step sequences repeated often enough to become SOP-like |

## Question To File Map

### Stage 1

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q1-Q3 | `USER.md` | who the user is and what the shrimp mainly helps with |
| Q4-Q6 | `openclaw.json` | access, approval, and high-risk defaults |
| Q7-Q9 | `SOUL.md` | boundaries, uncertainty handling, inner companion style |
| Q10 | `IDENTITY.md` | hated tone, wording, or visible reply feel |

### Stage 2

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q11-Q13 | `USER.md` | daily work shape, burden, domain shorthand |
| Q14-Q20 | `AGENTS.md` | task order, checkpoints, final checks, delivery rules, ask-first boundaries |

### Stage 3

| Questions | Usually write to | Meaning |
| --- | --- | --- |
| Q21-Q26 | `TOOLS.md` | search behavior, source trust, memory read/write preference, proof-of-save |
| Q27-Q30 | `HEARTBEAT.md` | restart notice style, `/new` recovery style, rule promotion, proactivity ceiling |

## Memory Routing Rules

### Write To Daily Memory First When

- the information is new
- the user just said it
- the information may still evolve
- it mainly supports short-term continuity

### Write To Durable Memory When

- the same fact or preference appears repeatedly
- the rule is clearly long-term
- the information should survive restarts and many future sessions

### Upgrade To Primary Rule Files When

- the information changes the shrimp's default behavior
- the information affects safety
- the information affects protocol, tone, or user-facing defaults

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

## Rebuild Mapping Rules

`叠加`

- prefer merge, annotate, preserve, append
- use when the old brain still contains useful signal

`覆盖`

- rebuild from the new source of truth
- replace conflicting rules
- keep a pre-rebuild snapshot summary for reference

User-facing choice labels may be localized.
In Chinese, use `叠加` and `覆盖`.
Internally they may map to `merge` and `replace`.

## Maintenance Mapping Rules

In maintenance mode:

- merge duplicate rules in `AGENTS.md`, `SOUL.md`, and `TOOLS.md`
- remove or demote stale preferences
- distill daily memory into `MEMORY.md`
- promote repeated operational patterns into `checklists/*.md`

Always summarize major maintenance effects before applying them.
