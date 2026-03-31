# Xunxiashi Interaction Flow

This file defines the required IM-first flow for install, build, follow-up configuration, and resume.

## Core UX Rules

- default to private chat
- make plain text sufficient
- keep the user guided, not interrogated
- ask one build question at a time
- tell the user what was written after meaningful writes
- never silently restart the build sequence from question 1

## Main State Machine

`Xunxiashi` should move through these states:

1. `kickoff`
2. `build_brain`
3. `post_build_config`
4. `train_brain`
5. `maintain_brain`

## 1. Kickoff

Trigger this immediately after install or first invocation in a fresh workspace.

Mandatory behavior:

1. ask whether to start building the brain now
2. ask for `叠加` or `覆盖`
3. explain the tradeoff clearly
4. wait for the user's explicit reply before question 1 starts

## 2. Build Brain

Once the user replies with a start signal, begin the 20-question build sequence.

Rules:

- ask one question at a time
- keep hints short and scannable
- after each answer, record the answer state
- write to real files as soon as the answer is stable enough
- if the write matters, say where it was written

Question order is fixed by `references/question-set.md`.

## 3. Immediate Post-Build Configuration

As soon as question 20 is answered:

1. explicitly say the build-brain stage is complete
2. explicitly say the flow is now entering train-brain and maintain-brain setup
3. ask the user to send the 5 follow-up prompts one by one
4. do not wait for the user to discover the next stage alone

The 5 follow-up prompts are also defined in `references/question-set.md`.

## 4. Interrupt And Resume

The sequence may be interrupted by:

- the user asking something unrelated
- the user disappearing mid-flow
- a tool or write failure
- a context switch

### Resume Rules

- do not restart from question 1 unless the user explicitly asks to restart
- resume from the first unanswered build question
- if build questions are complete, resume from the first unfinished follow-up prompt
- persist enough state to know:
  - current mode
  - chosen rebuild mode
  - last completed question
  - last completed follow-up item
  - files already written

### Resume Message Shape

When resuming, say something close to:

> We were still in build-brain.
> The next item is question 12.
> Earlier answers have already been written to `USER.md` and `SOUL.md`.

Or:

> Build-brain is already complete.
> We are now in post-build setup.
> The next item is follow-up 3 for startup recovery.

## 5. Train Brain

Train-brain begins only after build-brain and the immediate 5 follow-up prompts are complete, or after the user explicitly skips to normal usage.

Train-brain is not another questionnaire.

It is driven by:

- files
- images
- videos
- links
- SOPs
- examples
- corrections
- "remember this" type commands

## 6. Maintain Brain

Maintain-brain is not another questionnaire.

It is driven by:

- heartbeat
- cron
- restart recovery
- `/new` recovery
- workspace review
- deduplication
- distillation

## Recovery And Memory Rules

Startup recovery and `/new` recovery are product defaults, but real behavior still needs official hook wiring.
See `references/hooks-setup.md`.

When something should be remembered:

1. decide where it belongs
2. write it
3. only then confirm it

If writing fails, say so directly.

## End-Of-Turn Rule

At the end of a productive turn, one of these should be true:

- the kickoff decision was made
- one or more build questions were completed and saved
- the 5 post-build prompts advanced
- train-brain accepted real material
- maintain-brain configuration advanced
- or the exact next unanswered item was made clear
