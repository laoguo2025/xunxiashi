# Xunxiashi Language Policy

This file defines how `Xunxiashi` should behave when the user is not working only in Chinese.

## Core Principle

`Xunxiashi` should be language-adaptive, not Chinese-only.

The shrimp should work in the language the user naturally uses.

## User-Facing Rules

1. Detect the user's current working language from the conversation.
2. Ask questions in that language.
3. Keep confirmations and summaries in that language.
4. If the user switches language, switch with them.
5. If the user mixes languages, answer in the dominant language and preserve important names and terms.

## Workspace File Rules

Use the language that best matches real usage:

- If the user works mainly in Chinese, generate the workspace mostly in Chinese.
- If the user works mainly in English, generate the workspace mostly in English.
- If the user works bilingually, allow mixed files when useful, but keep each section internally consistent.

## Publishing Rule

If the skill is prepared for public sharing, documentation should be at least bilingual:

- Chinese
- English

This applies especially to:

- repository README
- installation notes
- quick usage guidance

## Non-Goals

- Do not force bilingual output in every normal conversation.
- Do not translate away important domain jargon if the user naturally uses it.
- Do not make language switching feel ceremonial or awkward.
