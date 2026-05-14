# Patch Policy

Make one small verified patch at a time.

## Risk Levels

```text
Low risk: docs, comments, README, minor hygiene.
Medium risk: validation, prompts, error handling, API wrappers, config.
High risk: architecture, module moves, schemas, public interfaces, RAG retrieval,
async, provider behavior.
```

## One-Patch Rule

A patch must have one primary purpose. Do not combine:

- refactor
- feature change
- dependency change
- UI change
- cleanup
- test infrastructure change beyond what the patch needs

If verification setup is missing, add minimal verification first as its own patch
or as the clearly bounded setup step before the requested safe refactor.

## Before Editing

Confirm:

- files likely affected
- risk level
- characterization requirement
- verification command
- unrelated local changes that must not be touched

## During Editing

- Prefer local patterns.
- Avoid broad formatting churn.
- Keep public behavior stable unless the patch intentionally changes it.
- Preserve existing user changes.
- Do not remove tests to make verification pass.

## After Editing

Run verification. Stop if it fails. Do not continue into another patch without
user direction.

Report:

- what changed
- why it is one patch
- characterization used
- verification result
- remaining backlog item to consider next
