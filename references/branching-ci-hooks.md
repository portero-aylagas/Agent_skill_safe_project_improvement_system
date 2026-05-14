# Branching, CI, and Hooks

Use this reference only when the user explicitly asks for branch, hook, CI,
commit, push, or full automation work.

## Approval Boundary

Do not do these without explicit authorization:

- create or switch branches for automation
- install pre-commit hooks
- add strict CI gates
- commit
- push
- open pull requests

## Branching

Before creating a branch:

- inspect current status
- identify unrelated changes
- avoid overwriting user work
- choose a short descriptive branch name

Keep each branch focused on one improvement.

## Hooks

Start with low-risk hooks only:

- trailing whitespace
- end-of-file fixer
- JSON validity
- YAML validity

Make formatters and strict linters opt-in unless the project already uses them.
Installing hooks changes local developer behavior, so ask first.

## CI

Default CI should run:

```text
make verify
```

CI must not require live secrets for normal checks. Use fake clients and local
fixtures. Live integration checks should be separate, clearly named, and gated by
explicit secrets.

## Full Automation Checklist

1. Confirm explicit approval.
2. Create branch.
3. Add or confirm verification.
4. Add characterization before risky changes.
5. Make one patch.
6. Run local verification.
7. Commit only relevant files.
8. Push.
9. Wait for CI.
10. Report result and next backlog item.
