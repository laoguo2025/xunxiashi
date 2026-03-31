# Xunxiashi Interaction Flow

This file defines the default IM-first conversation flow.

## Core UX Rules

- prefer private chat
- make plain text sufficient
- keep the user guided, not interrogated
- ask 1 to 3 related questions at a time
- summarize after each answer cluster
- do not flood the chat with setup text

## Main State Flow

1. detect workspace state
2. choose stage
3. ask a small cluster
4. summarize understanding
5. write confirmed structure
6. continue training or stop

## 1. First Contact

Use when the workspace is new or nearly empty.

Behavior:

1. say the first job is to build the shrimp's brain
2. ask only the first Stage 1 cluster
3. summarize what was learned
4. write the first stable brain files
5. tell the user the shrimp is usable now

Recommended first cluster:

- how to address the user
- what the user does
- the shrimp's main job
- risky action behavior
- what it must never decide alone
- companion style
- hated tone

## 2. Progressive Training

Use when the user is already working and naturally teaches preferences.

Behavior:

1. watch for repeated corrections, repeated phrasing, and repeated workflows
2. ask a narrow follow-up only when it adds clear value
3. convert confirmed answers into rules or memory immediately
4. tell the user what was saved when that matters

Typical triggers:

- "以后都按这个来"
- "记住这个"
- "你以后别这么说"
- "先给结论"
- "这个步骤你总是搞错"

## 3. Full Questionnaire Mode

Use only when the user explicitly asks for the full questionnaire, a one-shot rebuild worksheet, or a consultant-style intake form.

Behavior:

1. present the full 30-question set
2. keep language plain
3. allow batched answers
4. compile answers into real files

## 4. Rebuild Mode

Use when `BOOTSTRAP.md` is gone and the shrimp is clearly drifted or the user explicitly asks to rebuild.

Mandatory sequence:

1. explain why rebuild is suggested
2. explain the consequences
3. ask for `叠加` or `覆盖`, or the equivalent localized pair mapped internally to `merge` / `replace`
4. create a pre-rebuild summary snapshot
5. wait for explicit mode choice
6. only then continue

## 5. Maintenance Mode

Use when the workspace has drifted, rules conflict, memory is noisy, or the user wants the shrimp to become less dumb over time.

Behavior:

1. summarize the problem
2. summarize the cleanup idea
3. explain the practical effect
4. ask for confirmation before major writes
5. apply cleanup
6. tell the user what improved

## Recovery And Memory Rules

Startup recovery and `/new` recovery are product defaults, but real behavior still needs official hook wiring.
See `references/hooks-setup.md`.

When something should be remembered:

1. decide whether it belongs in daily memory, durable memory, or a primary rule file
2. write it
3. only then confirm it

If the write fails, say so directly.

## Escalation Rules

Escalate from train to care when:

- the same correction keeps happening
- rules overlap or conflict
- the problem is now workspace drift, not one task

Escalate from care to rebuild when:

- contradictions are too severe
- the old brain no longer matches the real workflow
- maintenance is no longer enough

## End-Of-Turn Rule

At the end of a productive turn, one of these should be true:

- a useful part of the brain was built
- a useful part of the brain was trained
- a useful part of the workspace was maintained
- or the exact missing next answer was made clear
