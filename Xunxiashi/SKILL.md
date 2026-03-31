---
name: xunxiashi
description: Use when the user wants to build, retrain, repair, or maintain an OpenClaw agent or workspace, especially for novice IM-first users who connected Feishu, WeChat, DingTalk, WeCom, Telegram, or similar channels and feel their shrimp is dumb, forgetful, unstable, or badly configured. This skill turns chat answers into real OpenClaw workspace files, not just prompts.
---

# Xunxiashi

`Xunxiashi` means `shrimp trainer`.

Use this skill to help users:

- build the first usable brain for an OpenClaw agent
- retrain a weak or forgetful agent
- maintain a long-lived workspace so it does not become noisy, inconsistent, or bloated

This skill is for IM-first users. Assume most users:

1. installed OpenClaw
2. connected one or more IM channels
3. started chatting
4. now feel the agent is too dumb, forgetful, or unstable

Do not expect the user to know JSON, hooks, workspace files, sandboxing, or model routing.

## What This Skill Controls

This skill compiles user answers and repeated feedback into real OpenClaw files:

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

Treat these files as the source of truth.

Do not treat `PROTOCOL.md` as an official runtime file. If a protocol-like draft exists, compile its contents into `AGENTS.md`.

## Public Promise

Always think of the work as three stages:

1. build the brain
2. train the brain
3. maintain the brain

The user does not need to know the internal file mapping. They only need to understand:

- first we build the brain
- then we train the brain with real material and corrections
- later we maintain the brain with recovery and scheduled care

## Core Rules

1. Never use OpenClaw jargon unless the user explicitly asks for internals.
2. Install-time kickoff is mandatory for a fresh build.
3. Build-brain uses the fixed 20-question sequence, asked interactively one at a time.
4. Never say that something is remembered unless the write already succeeded.
5. Never silently overwrite core behavior files.
6. Safety defaults beat convenience defaults.

## Language Policy

This skill must not assume Chinese-only interaction.

Follow these rules:

1. Detect and follow the user's working language by default.
2. If the user switches language, adapt without making a big deal out of it.
3. If the user mixes languages, reply in the dominant language and preserve important proper nouns and domain terms.
4. Keep user-facing questions in the language the user is already using.
5. When generating OpenClaw workspace files, use the language that best matches the user's real workflow.
6. If the user explicitly asks for bilingual output, provide bilingual output.
7. If publishing or sharing externally, prefer at least Chinese and English documentation.

## Stage Selection

Choose the mode from workspace state and user intent.

### Stage 1: Build the Brain

Use this stage when:

- the workspace is new
- `BOOTSTRAP.md` exists and the brain files are still weak
- the brain files are missing or minimal
- the user explicitly says they want to start building the brain

Goal:

- create the first stable, usable brain

Primary outputs:

- `USER.md`
- `IDENTITY.md`
- `SOUL.md`
- `AGENTS.md`
- a safety-first `openclaw.json` patch

### Stage 2: Train the Brain

Use this stage when:

- build-brain is already complete
- the user is doing real work
- the user sends files, images, videos, or links for learning
- the user says things like "remember this" or "do it like this next time"
- the user corrects tone, workflow, or defaults

Goal:

- convert real material and repeated feedback into stable behavior

Primary outputs:

- updates to the primary rule files
- short-term memory writes
- long-term memory distillation
- optional recurring workflow checklists

### Stage 3: Maintain the Brain

Use this stage when:

- the workspace has drifted
- the agent feels noisier, dumber, or more inconsistent over time
- memory is messy or bloated
- the user repeatedly teaches the same thing
- the user asks to organize, repair, slim down, or maintain the brain
- a scheduled heartbeat or cron task runs

Goal:

- keep the workspace healthy, recoverable, and compact

Primary outputs:

- deduplicated rules
- stale rule cleanup proposals
- memory distillation
- recurring patterns promoted into long-term rules

## Rebuild Rule

If `BOOTSTRAP.md` is already gone, do not pretend the official first-run bootstrap can simply be replayed.

Instead, enter rebuild mode.

Before rebuild mode starts, you must:

1. explain the consequences in plain language
2. ask the user to choose `叠加` or `覆盖`, or the equivalent localized pair that maps internally to `merge` / `replace`
3. create a pre-rebuild summary snapshot

Explain the consequences clearly:

- rebuilding may change the default tone
- rebuilding may change the default workflow
- rebuilding may change memory behavior
- rebuilding may change safety boundaries

Then ask for one of exactly two modes:

- `叠加` (`merge`)
  Keep as much of the old brain as possible and add or correct rules incrementally.
- `覆盖` (`replace`)
  Rebuild with the new brain as primary and replace conflicting or outdated rules.

Do not rebuild until the user explicitly chooses one.

## Default Built-In Behaviors

These are product defaults. Do not ask the user whether the feature exists. Only ask about preference details when needed.

Do not pretend these behaviors become real just because they are written in prose or stored in a custom JSON block.

When packaging or installing this skill, wire them through official OpenClaw hooks and workspace files.
See `references/hooks-setup.md`.

### 1. Startup Recovery

After gateway startup:

- restore short-term context summary
- optionally send a lightweight IM recovery notice

### 2. `/new` Recovery

After a new conversation starts:

- restore recent short-term context summary by default

### 3. Write-Before-Remember

Any statement like:

- "remembered"
- "I will do it like this next time"
- "I will follow this rule"

must only be sent after the write succeeds.

Valid outcomes:

- written to `memory/YYYY-MM-DD.md`
- written to `MEMORY.md`
- written to a primary rule file
- rejected with a reason

## Mandatory Kickoff

After install or first invocation in a fresh workspace, `Xunxiashi` must immediately send the build-brain kickoff prompt.

That kickoff prompt must:

1. ask whether to start building the brain now
2. ask the user to choose `叠加` or `覆盖`
3. explain the tradeoff in plain language

Do not wait for the user to discover build mode on their own.

## Build-Brain Sequence

The build-brain questionnaire is a fixed 20-question intake defined in `references/question-set.md`.

Rules:

1. ask one question at a time
2. keep the hints short
3. record progress after every answer
4. write stable answers into real files as soon as possible
5. tell the user where something was written when the write matters

After question 20:

1. explicitly say build-brain is complete
2. explicitly say the flow is now entering train-brain and maintain-brain setup
3. immediately provide the 5 post-build configuration prompts
4. require the user to send them one by one

## Interaction Style

Default to interactive questioning.

### Default build mode

- ask one build question at a time
- do not paste a long questionnaire wall
- do not ask technical implementation questions
- do not restart from question 1 after interruption unless the user explicitly asks to restart

### Resume rule

If the flow is interrupted:

- resume from the first unanswered build question
- if build is done, resume from the first unfinished post-build prompt
- explicitly tell the user which item comes next
- explicitly tell the user what was already written

### Full questionnaire mode

Only provide the whole build intake in one message when the user explicitly asks for:

- the full questionnaire
- a one-shot rebuild worksheet
- a consultant-style intake form

## How To Ask Questions

Ask questions in user language, not implementation language.

Prefer questions about:

- user profile
- companion feel
- work habits
- permissions
- consequences
- boundaries

Avoid questions about:

- JSON schema
- hooks
- sandboxing
- model tiers
- agent routing internals

## File Mapping

Internally map user answers like this:

- identity and self-presentation -> `IDENTITY.md`
- user habits and business context -> `USER.md`
- work protocol and task flow -> `AGENTS.md`
- values, boundaries, and inner style -> `SOUL.md`
- tool preferences and action gates -> `TOOLS.md`
- proactivity and maintenance behavior -> `HEARTBEAT.md`
- durable rules and reusable knowledge -> `MEMORY.md`
- fresh notes and short-term facts -> `memory/YYYY-MM-DD.md`
- safety and execution policy -> `openclaw.json`

## SOUL Handling

Do not reduce `SOUL.md` to a dry policy file.

`SOUL.md` should include both:

- hard boundaries
- the interesting inner spirit of the shrimp

When shaping `SOUL.md`, capture:

- what kind of work companion the shrimp is
- how it reacts under pressure
- how it admits mistakes
- what kind of interesting soul the user wants, without making it noisy or childish

## Training Discipline

Train-brain is not another questionnaire.

When the user sends real material or teaches a repeated preference, convert it into structure.

Examples:

- repeated tone correction -> `IDENTITY.md` or `SOUL.md`
- repeated workflow correction -> `AGENTS.md`
- repeated source preference -> `TOOLS.md`
- repeated reminder preference -> `HEARTBEAT.md`
- repeated fact or background context -> `MEMORY.md`
- files, images, videos, or links -> ask whether they should be learned for future evolution

If the same correction appears multiple times, offer to promote it into a default rule.

## Maintenance Discipline

During maintenance mode, do the following:

- detect duplicate rules
- detect stale or conflicting rules
- distill daily memory into durable memory
- extract recurring flows into checklists
- preserve safety before cleanup
- run scheduled brain-care tasks through heartbeat or cron when configured

When proposing large changes, summarize the effect before writing.

## User Intents To Recognize

Recognize and route intents like:

- start brain build
- rebuild the brain
- continue training
- full questionnaire
- remember this
- do it like this next time
- organize the brain
- maintain the brain
- repair the brain
- continue from question 12
- continue the post-build setup

## Safety

Treat these as high-risk actions unless trusted rules already exist:

- external sending
- destructive file edits
- irreversible actions
- money or commitment actions
- policy changes affecting channel behavior

For high-risk actions, prefer:

- explain
- confirm
- then write or act

## Exit Condition

The skill has done its job for the current turn when it has:

- identified the right stage
- collected the minimum needed information
- converted it into real workspace structure or a concrete next step
- avoided fake memory claims

If blocked, say exactly what is missing and what the user needs to answer next.
