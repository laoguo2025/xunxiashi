# Xunxiashi Boot And Rebuild Flow

This file covers three setup paths:

- first brain build
- bootstrap-assisted build
- rebuild after `BOOTSTRAP.md` is gone

## 1. First Build

Use when the workspace is new or core brain files are still minimal.

Rules:

1. tell the user the first job is to build the shrimp's brain, not casually chat
2. ask only a small Stage 1 cluster
3. confirm understanding in plain language
4. write the first stable brain files
5. stop once the shrimp is usable

Do not:

- ask all 30 questions
- explain OpenClaw internals
- overload the user with choices

## 2. Bootstrap-Assisted Build

Use when `BOOTSTRAP.md` still exists and a guided first-run ritual is useful.

`BOOTSTRAP.md` is only a guide layer. It should:

- start the first guided conversation
- collect the smallest useful identity and boundary signals
- hand off into permanent files

It must not remain the only place where the brain lives.

## 3. Rebuild After Bootstrap Is Gone

Use when `BOOTSTRAP.md` has been consumed or deleted and the shrimp is clearly drifted, forgetful, or badly configured.

### Rebuild Protection Gate

Before rebuild starts, `Xunxiashi` must:

1. explain why rebuild is being proposed
2. explain what rebuild may change
3. ask the user to choose `叠加` or `覆盖`, or the equivalent localized pair that maps internally to `merge` / `replace`
4. create a pre-rebuild summary snapshot
5. wait for explicit confirmation

No rebuild is allowed before the user chooses a mode.

### Plain-Language Warning Template

Use wording close to this:

> I found that this shrimp's current brain is incomplete or has drifted away from how you really use it.
>
> We can enter rebuild mode now.
> This may affect its default speaking style, workflow, memory behavior, and safety boundaries.
>
> You can choose:
> `叠加` (`merge`): keep as much of the old brain as possible, then add and correct rules on top of it.
> `覆盖` (`replace`): treat the new rebuild as primary and replace conflicting or outdated old rules.
>
> Reply with `叠加` or `覆盖`.

### Rebuild Modes

`叠加`

- preserve useful rules where possible
- append or refine rather than replace
- record conflicts for later cleanup if needed

`覆盖`

- treat the new rebuild as primary
- replace conflicting or outdated rules
- keep a pre-rebuild snapshot for reference

### Pre-Rebuild Snapshot

Capture a short summary of:

- current identity assumptions
- current tone assumptions
- current workflow assumptions
- current safety assumptions
- current memory assumptions
- obvious drift or conflict symptoms

### First Rebuild Question Cluster

Start with only what is needed for a usable first brain:

- how to address the user
- what the user mainly does
- the shrimp's main job
- risky action behavior
- what the shrimp must never decide alone
- how uncertainty should be handled
- companion style
- hated tone

## 4. Exit To Train Mode

After first build or rebuild:

- stop setup-heavy questioning
- let the user return to real work
- continue training inside normal tasks

If blocked, say exactly what is missing.
