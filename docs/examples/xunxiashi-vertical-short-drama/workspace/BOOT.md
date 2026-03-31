# BOOT

Use this file during gateway startup recovery.

## Startup Intent

- recover the most recent short-term writing context
- avoid pretending the shrimp remembers if nothing was actually written
- keep the startup notice short and useful

## Recovery Source Order

1. read the latest daily memory note
2. extract the most recent still-relevant writing preferences or pending scene work
3. if a startup notice is needed, keep it to one short line plus one useful recovered point

## Notice Style

For this example user:

- do not send a noisy status dump
- send a short "I'm back" line only when startup recovery matters
- if nothing important was recovered, stay quiet
