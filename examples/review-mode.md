# Review Mode Example

## Prompt

```text
Use the safe project improvement system in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

## Expected Output Shape

- Mode used: review mode.
- Files changed: none.
- Current behavior summary: entry points, verification, tests, config, live-service boundaries.
- Audit findings: prioritized by risk and user-visible impact, including coding
  standards conformance for software engineering quality reviews.
- Backlog: small patch candidates with likely files, risk level, characterization need, and verification command.
- Stopped work: any changes that require explicit approval.
