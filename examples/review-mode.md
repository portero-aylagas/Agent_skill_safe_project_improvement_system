# Review Mode Example

## Prompt

```text
Use the safe project improvement system in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

## Expected Output Shape

- Requirements Ledger: short table with must/should requirements, planned
  evidence or verification, and status/deferral.
- Audit scope: selected audit families and areas, with why each selected area
  applies. Skipped-area details appear only in the skipped-area sections.
- Current behavior summary: entry points, verification, tests, config,
  live-service boundaries.
- Readable audit-area blocks. Example blocks are shown below; a real review
  includes every checked `Engineering Audits` and `AI System Audits` area, even
  when there are no material findings:

Required block shape:

```markdown
## <Audit Area>

- Severity: High | Medium | Low | Info
- Finding: <finding>
- Evidence / Location: <files, functions, commands>
- Recommended Action: <action>
- Verification: <test, command, review method>

## <Audit Area>

No material findings.

Evidence:

- <brief evidence, if useful>

Verification:

- <brief verification, if useful>
```

## General Software Architecture

- Severity: Medium
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Verification command or check.

## Security And Secrets

- Severity: High
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Verification command or check.

## Repository Hygiene

- Severity: Low
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/path.
- Recommended Action: Minimal action.
- Verification: Verification command or check.

## Skipped Engineering Areas

- CI Maturity: Not checked because the repository has no CI files.

## AI Software Architecture

- Severity: Medium
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Fake-client test or smoke check.

## Prompt Quality

- Severity: Medium
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Prompt fixture or review check.

## Workflow Automation

No material findings.

Evidence:

- Inspected workflow entry points.

Verification:

- Existing verification.

## Skipped AI System Areas

- Speech Pipelines: Not checked because the repository has no speech pipeline.

- Backlog: small patch candidates with audit family, audit area, severity, likely
  files, risk level, characterization need, and verification command.
- Review result: mode used, files changed, verification command/result if run,
  and stopped work requiring explicit approval.
