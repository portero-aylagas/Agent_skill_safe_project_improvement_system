# Coding Standards

Use these standards when reviewing, editing, refactoring, or installing
project-local agent rules.

## Style

- Write beginner/intermediate-friendly code.
- Prefer simple control flow over clever abstractions.
- Follow PEP8 naming and layout.
- Use Google-style docstrings for public modules, classes, and functions.
- Add type hints at module boundaries, public functions, adapters, and data
  models.
- Keep internal helper annotations practical, not noisy.
- Use clear inline workflow comments only where they reduce cognitive load.
- Preserve existing project conventions when they are reasonable.

## Readability Definition Of Done

Implementation work should be beginner/intermediate-friendly:

- public modules, classes, and functions have concise Google-style docstrings
  unless they are clearly private or internal
- names describe domain behavior instead of hiding it behind generic terms
- control flow is simple enough to scan without tracing every branch
- side effects such as file I/O, network calls, environment reads, mutation, and
  persistence are explicit at the module or function boundary
- module responsibilities are understandable without reverse-engineering the
  whole project
- comments explain intent, workflow, assumptions, side effects, or safety
  constraints when the code alone would make a future reader work too hard

## Design

- Keep changes small and maintainable.
- Prefer existing helpers and patterns over new architecture.
- Avoid broad rewrites unless the user explicitly approves high-risk work.
- Separate refactors from feature changes, dependency changes, UI changes, and
  cleanup.
- Avoid global mutable state for configuration, clients, and credentials.
- Prefer explicit parameters and dependency injection for external services.

## AI/API Code

- Keep provider calls behind narrow wrappers.
- Pass clients or factories into code under test.
- Do not require live API keys for normal tests.
- Store prompt text, model names, and safety limits where they can be reviewed.
- Test behavior with fake clients and deterministic fixtures.

## Documentation

- Treat code documentation as part of engineering quality, not just README
  polish.
- Include public module, class, and function docstrings in software engineering
  quality reviews.
- Prefer Ruff pydocstyle checks for gradual enforcement when the repository can
  adopt them without a large unrelated cleanup.
- Document how to run verification.
- Document required environment variables with examples, not real secrets.
- Keep README updates factual and close to the changed behavior.

## Comments

Use comments as a comprehension tool, not decoration.

Prefer comments when they help a future reader quickly understand:

- what a block is responsible for
- why an approach exists
- what assumptions the code depends on
- what side effects happen
- what must stay true for the code to be safe or correct
- how a workflow step fits into the larger process
- why an edge case, fallback, or guard exists

Avoid comments that merely restate obvious syntax.
