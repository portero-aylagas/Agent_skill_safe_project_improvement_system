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

## Patch Size Thresholds

Treat a patch as too large and split it when it crosses any of these thresholds:

- It touches more than 5 files.
- It changes more than 250 non-generated lines.
- It changes dependencies, lockfiles, packaging, or runtime versions.
- It changes a public API, CLI contract, schema, prompt contract, or persisted
  data shape.
- It moves modules, renames entry points, or changes import paths.
- It mixes behavior changes with cleanup, formatting, or broad renames.
- It needs live credentials, network services, or paid APIs to verify.

These thresholds are guides, not permission to stretch risk. A smaller patch is
required whenever failure would be hard to understand or revert manually.

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
