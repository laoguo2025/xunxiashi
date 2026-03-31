## Xunxiashi Skill Design

### Goal

`Xunxiashi` is a single OpenClaw-oriented training skill that helps non-technical users turn a "dumb shrimp" into a durable agent through three stages:

1. Build the brain
2. Train the brain
3. Maintain the brain

The skill must work for IM-first users who only know how to:

1. install OpenClaw
2. connect IM channels
3. chat

The user should not need to understand `openclaw.json`, workspace files, hooks, cron, sandbox, or memory providers.

### Naming

The public skill name is `Xunxiashi`.

- Chinese brand meaning: `训虾师`
- Canonical repo and package identifier: `Xunxiashi`

This avoids collisions with generic names such as `clawtrainer` or `openclawtrainer`.

### Product Positioning

`Xunxiashi` is not a generic writing skill. It is a workspace-training orchestrator for OpenClaw.

Its public promise is:

- first help me build the brain
- then help me train the brain while I use it
- later help me maintain the brain so it does not become bloated, forgetful, or inconsistent

### Core Principles

1. User-facing language is always plain language, never OpenClaw internals.
2. All "I remembered it" claims must be backed by a disk write.
3. Default behavior is interactive and progressive, not a one-shot questionnaire dump.
4. Official OpenClaw files are the source of truth; methodology-only files are intermediate artifacts.
5. Safety defaults beat convenience defaults.
6. Workspace maintenance is part of the product, not an afterthought.
7. Rebuilding a brain is a protected action, not a silent action.

### Non-Goals

- Do not require users to manually edit JSON or markdown files.
- Do not expose low-level routing, sandbox, or model pricing questions to novice users.
- Do not rely on long freeform prompt pastes as the primary flow.
- Do not keep important behavior only inside chat history.

## System Model

### One Skill, Three Internal Modes

Externally there is only one skill: `Xunxiashi`.

Internally it operates in three modes:

1. `BrainBuildMode`
2. `BrainTrainMode`
3. `BrainCareMode`

The mode is chosen from workspace state, recent conversation state, and explicit user intent.

### Workspace State Detection

`Xunxiashi` should inspect the OpenClaw workspace and classify it into one of four states:

1. `fresh`
   - `BOOTSTRAP.md` exists
   - primary brain files are missing or minimal
2. `partial`
   - `BOOTSTRAP.md` missing or consumed
   - some primary brain files exist but are incomplete
3. `active`
   - primary files exist
   - memory and training are functioning
4. `degraded`
   - conflicts, bloat, stale memory, missing summaries, repeated user corrections, or integrity drift

### Primary Files

`Xunxiashi` ultimately writes to OpenClaw-native files:

- `openclaw.json`
- `BOOTSTRAP.md`
- `AGENTS.md`
- `USER.md`
- `IDENTITY.md`
- `SOUL.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `MEMORY.md`
- `memory/YYYY-MM-DD.md`
- optional `checklists/*.md`

### Methodology Mapping

The training methodology is mapped into real OpenClaw files like this:

- `JSON bus` -> `openclaw.json`
- `USER` -> `USER.md`
- `PROTOCOL` -> `AGENTS.md`
- `IDENTITY` -> `IDENTITY.md`
- `SOUL` -> `SOUL.md`
- `TOOLS` -> `TOOLS.md` plus `openclaw.json` policies
- `HEARTBEAT` -> `HEARTBEAT.md`
- `feeding and memory` -> `MEMORY.md` and `memory/*.md`

`PROTOCOL.md` is never treated as an official runtime file. If used at all, it is an internal draft artifact that must be compiled into `AGENTS.md`.

## Three-Stage Architecture

### Stage 1: Build the Brain

#### Purpose

Create the first stable brain for a new or underconfigured OpenClaw workspace.

#### Trigger

Enter Stage 1 when any of these are true:

- user explicitly asks to start brain building
- workspace is `fresh`
- workspace is `partial`
- `BOOTSTRAP.md` has been consumed or deleted, but the brain files are still weak

#### Important Rule

If `BOOTSTRAP.md` is missing, do not attempt to re-run official first-run bootstrap.
Instead, enter rebuild mode and rebuild the brain through `Xunxiashi` itself.

#### Rebuild Protection Gate

Before rebuild mode starts, `Xunxiashi` must do all of the following:

1. explain the consequences in plain language
2. ask the user to choose `叠加` or `覆盖`
3. create a pre-rebuild summary snapshot of the current brain state

The user-facing explanation must make these consequences explicit:

- rebuilding may change the default tone, workflow, memory behavior, and safety boundaries
- `叠加` means keep as much of the old brain as possible and add or correct rules incrementally
- `覆盖` means rebuild with the new brain as primary and replace conflicting or outdated rules

No rebuild is allowed until the user explicitly chooses one mode.

#### Merge Mode

Use `叠加` when:

- the user wants to keep the current flavor
- the current brain is partially useful
- the goal is correction, not replacement

Expected behavior:

- preserve as much existing intent as possible
- append or refine rules incrementally
- surface conflicts for later care mode cleanup when needed

#### Replace Mode

Use `覆盖` when:

- the current brain is badly drifted
- the user wants a hard reset
- the workspace behavior is too inconsistent to trust

Expected behavior:

- rebuild the main rule files with the new brain as primary
- replace conflicting or outdated rules
- keep a pre-rebuild summary snapshot for traceability

#### Inputs

- Stage 1 subset of the 30 questions
- existing workspace files if present
- recent conversations if available
- user corrections during the session

#### Outputs

- initial `USER.md`
- initial `IDENTITY.md`
- initial `SOUL.md`
- initial `AGENTS.md`
- initial `TOOLS.md`
- initial `HEARTBEAT.md`
- safety-first `openclaw.json` patch
- optional custom `BOOTSTRAP.md` for first-run guided ritual

#### UX Model

Interactive only.

- ask 1 to 3 tightly related questions at a time
- summarize back what was learned
- write immediately after each confirmed chunk
- stop once the first usable brain exists

### Stage 2: Train the Brain

#### Purpose

Turn repeated feedback, user habits, domain language, and task patterns into stable behavior.

#### Trigger

Enter Stage 2 when:

- the brain is usable but incomplete
- the user is doing real tasks
- repeated corrections appear
- the user says things like "remember this" or "do it like this next time"
- there are unanswered items from the 30-question set

#### Inputs

- remaining 30-question items
- live task context
- user corrections
- documents, links, notes, transcripts, and reference material

#### Outputs

- updates to `AGENTS.md`
- updates to `USER.md`
- updates to `IDENTITY.md`
- updates to `SOUL.md`
- updates to `TOOLS.md`
- updates to `HEARTBEAT.md`
- short-term writes to `memory/YYYY-MM-DD.md`
- distilled long-term writes to `MEMORY.md`
- optional `checklists/*.md` for recurring workflows

#### Training Behavior

`Xunxiashi` should not ask all questions upfront.
It should opportunistically ask follow-up questions inside real work.

Examples:

- "You corrected my tone three times. Should I make that a default rule?"
- "You asked me to always give the conclusion first. Should that apply to all reports or just client-facing ones?"

### Stage 3: Maintain the Brain

#### Purpose

Maintain workspace health so the agent does not become noisy, inconsistent, bloated, or forgetful.

#### Trigger

Enter Stage 3 when:

- the user explicitly asks to organize, maintain, slim down, review, or repair the brain
- periodic maintenance runs
- repeated contradiction is detected
- memory files are growing without distillation
- the user repeatedly re-teaches the same thing
- the workspace is classified as `degraded`

#### Design Source

This stage absorbs the maintenance logic inspired by `win4r/openclaw-workspace`, but remains part of the single `Xunxiashi` skill.

#### Outputs

- deduplicated rules
- stale rule cleanup proposals
- `memory/*.md` distilled into `MEMORY.md`
- recurring patterns promoted into `AGENTS.md` or `checklists/*.md`
- workspace health summaries
- safe patch suggestions before major rewrites

## Default Built-In Behaviors

These are product defaults, not user questionnaire items.

1. Gateway restart recovery
   - on startup, restore short-term context summary
   - optionally send a lightweight IM recovery notice
2. `/new` conversation recovery
   - recover recent short-term context summary by default
3. Write-before-remember discipline
   - never say "记住了" until the write succeeds
4. Short-term before long-term memory
   - new facts go to daily memory first unless clearly long-term
5. Rule promotion discipline
   - repeated corrections create candidate rules before promotion

## Question Architecture

The 30-question framework is split by stage:

- Stage 1: identity, safety, authority, baseline style
- Stage 2: work patterns, output rules, repeated corrections, task flow
- Stage 3: retrieval, retention, restart recovery style, candidate rule promotion

Questions are user-facing.
Mapping to actual files is internal to the skill.

## Memory Architecture

### Memory Tiers

1. `Short-term working memory`
   - recent context summaries
   - per-day memory notes
2. `Long-term durable memory`
   - stable rules, user preferences, domain facts
3. `Candidate rule layer`
   - repeated but not yet promoted behaviors

### Memory Write Policy

Every memory-style user instruction must end in one of these outcomes:

- written to `memory/YYYY-MM-DD.md`
- written to `MEMORY.md`
- written to a primary rule file
- rejected with a reason

Never return a fake success message.

### Memory Confirmation Style

When writing succeeds, confirm in plain language, for example:

- saved to today's notes
- saved to long-term memory
- updated as a default rule

## Interaction Design

### Default User Flows

#### Flow A: First Install

1. OpenClaw is installed
2. IM channel is connected
3. user invokes `Xunxiashi`
4. Stage 1 builds the initial brain
5. Stage 2 continues during daily use

#### Flow B: Existing Dumb Shrimp

1. user already uses OpenClaw
2. `BOOTSTRAP.md` is gone
3. user complains that the agent is forgetful or dumb
4. `Xunxiashi` proposes rebuild mode
5. user chooses `叠加` or `覆盖`
6. Stage 1 rebuilds the brain from current reality

#### Flow C: Drifted Workspace

1. user has a long-lived workspace
2. rules conflict or memory is messy
3. `Xunxiashi` enters Stage 3
4. workspace is distilled, cleaned, and repaired

### Public Commands

The skill should recognize user intents such as:

- start brain build
- rebuild the brain
- continue training
- full questionnaire
- remember this
- do it like this next time
- organize the brain
- maintain the brain
- repair the brain

## Safety Model

### Safety Defaults

- novice-friendly defaults
- conservative action approval
- authority-first source preference
- never silently overwrite critical behavior files without a summary

### High-Risk Actions

These should require explicit confirmation unless already covered by a trusted rule:

- external sending
- destructive file edits
- irreversible actions
- money or commitment actions
- policy changes affecting channel behavior

## Channel Assumptions

`Xunxiashi` is designed for IM-first usage.

Primary assumption:

- the interaction happens in a private chat

Secondary assumption:

- richer channels may support better formatting, but the core experience must succeed in plain text

## Future Implementation Structure

Recommended skill package layout:

```text
Xunxiashi/
├── SKILL.md
├── references/
│   ├── architecture.md
│   ├── file-mapping.md
│   ├── question-set.md
│   ├── boot-rebuild.md
│   └── workspace-care.md
├── assets/
│   └── templates/
│       ├── bootstrap.template.md
│       ├── agents.template.md
│       ├── user.template.md
│       ├── identity.template.md
│       ├── soul.template.md
│       ├── tools.template.md
│       ├── heartbeat.template.md
│       └── memory.template.md
└── agents/
    └── openai.yaml
```

## Next Decisions

The next design pass should define:

1. the final `SKILL.md` workflow
2. the exact stage-to-question mapping
3. the file write strategy per answer type
4. the startup and `/new` recovery behavior in more detail
5. the workspace-care policy thresholds
