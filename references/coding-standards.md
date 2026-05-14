# Coding Standards

Use these standards when editing project code or installing project-local agent
rules.

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

- Document how to run verification.
- Document required environment variables with examples, not real secrets.
- Keep README updates factual and close to the changed behavior.
