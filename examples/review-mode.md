# Review Mode Example

## Prompt

```text
Use the safe project improvement system in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

## Expected Output Shape

- Audit scope:
  - selected audit families and areas
  - skipped audit families and areas
  - what each selected area checks and why it applies
- Current behavior summary: entry points, verification, tests, config,
  live-service boundaries.
- Findings by audit family, audit area, then severity:

```text
Engineering Audits
- General Software Architecture
  - Medium
    - Finding with exact location, impact, and minimal fix.
- Security And Secrets
  - High
    - Finding with exact location, impact, and minimal fix.
- Repository Hygiene
  - Low
    - Finding with exact location, impact, and minimal fix.

AI System Audits
- AI Software Architecture
  - Medium
    - Finding with exact location, impact, and minimal fix.
- Prompt Quality
  - Medium
    - Finding with exact location, impact, and minimal fix.
- Workflow Automation
  - No material findings.
```

- Backlog: small patch candidates with audit family, audit area, severity, likely
  files, risk level, characterization need, and verification command.
- Review result:
  - Mode used: review mode.
  - Files changed: none.
  - Verification command and result, if run.
  - Stopped work: any changes that require explicit approval.
