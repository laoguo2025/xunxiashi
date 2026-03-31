# Xunxiashi Workspace Care

This file defines Stage 3 maintenance policy.

## Goal

Keep a long-lived workspace:

- smaller
- clearer
- less repetitive
- less contradictory
- easier to recover after restart or `/new`

## Enter Care Mode When

- the user asks to organize, repair, slim down, review, or maintain the brain
- the same correction keeps appearing
- rules are noisy, duplicated, or conflicting
- daily memory keeps growing without distillation
- the shrimp keeps forgetting recently taught things

## Main Problems To Look For

### Rule Duplication

- same tone rule in multiple files
- near-duplicate workflow lines
- repeated boundaries with slightly different wording

Action:

- merge duplicates into one clearer rule

### Rule Conflict

- one file says "ask first" while another implies "act directly"
- one file favors brevity while another favors detailed explanation
- memory and protocol imply different defaults

Action:

- surface the conflict
- propose a resolution
- do not silently choose unless priority is already obvious

### Memory Bloat

- too many daily notes
- temporary noise in durable memory
- repeated facts stored many times

Action:

- compress recent notes
- move stable signal into `MEMORY.md`
- leave time-sensitive facts in daily memory

### Repeated Correction Loops

- same wording keeps getting fixed
- same workflow keeps being reteached
- same retrieval mistake keeps happening

Action:

- promote into a stable default rule
- or into a checklist if the pattern is operational

## Main Maintenance Actions

1. distill `memory/YYYY-MM-DD.md` into durable memory and primary rule files
2. promote recurring workflows into `AGENTS.md` or `checklists/*.md`
3. re-align tone drift in `IDENTITY.md` and `SOUL.md`
4. repair safety drift in `openclaw.json`, `SOUL.md`, `AGENTS.md`, and `TOOLS.md`
5. compress overgrown files and move procedural detail into checklists

## Candidate Rule Layer

Do not promote every repeated pattern immediately.

Use a candidate-rule mindset when:

- the pattern appeared only a few times
- the user may still be experimenting
- the rule would have wide impact

## User-Facing Behavior

Do not dump a huge audit report.

Instead:

1. summarize the main problem
2. summarize the proposed cleanup
3. explain the practical effect
4. ask for confirmation before major writes

## Safety Rule

Ask for confirmation before:

- replacing many core rules
- deleting large amounts of memory content
- compressing multiple primary files at once
- changing a default that affects many future sessions

## Escalation Rule

If maintenance is no longer enough, say so directly and route into rebuild mode with the usual `叠加` / `覆盖` protection gate.
