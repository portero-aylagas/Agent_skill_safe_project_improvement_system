# Project Agent Rules

Use these rules when modifying this repository.

## Default Code Style

- Write beginner/intermediate-friendly code.
- Follow PEP8.
- Use Google-style docstrings for public modules, classes, and functions.
- Add type hints at public boundaries and important data structures.
- Keep inline workflow comments clear and rare.
- Prefer small maintainable changes over broad rewrites.

## Safe Improvement Workflow

Use this loop:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Do not start by refactoring. Inspect the current project structure, behavior,
tests, configuration, and entry points first.

## One-Patch Policy

Make one focused patch at a time. Do not combine:

- refactor
- feature change
- dependency change
- UI change
- cleanup

Stop after the patch and verification unless the user asks for the next patch.

## Characterization

Before medium/high-risk changes, create or identify characterization:

- automated tests
- smoke scripts
- golden input/output fixtures
- repeatable manual checklist

Manual characterization is temporary and should become automated when practical.

## Verification

Every code-changing patch needs verification. Prefer:

```text
make verify
```

Normal verification must not require live API keys, network access, or paid
services. Use fake clients/mocks for AI/API tests.

If verification fails, stop and report the command, failure summary, and smallest
next diagnostic step.

## Authorization Boundary

Do not push, install hooks, add strict CI, or make live API calls unless the user
explicitly authorizes that action.
