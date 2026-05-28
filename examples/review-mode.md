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
- Audit scope: selected and skipped audit families and areas, with why each
  selected area applies.
- Current behavior summary: entry points, verification, tests, config,
  live-service boundaries.
- Readable audit-area blocks. Example blocks are shown below; a real review
  includes every checked `Engineering Audits` and `AI System Audits` area, even
  when there are no material findings:

Required block shape:

```markdown
## <Audit Area>

- Checked: Yes
- Severity: High | Medium | Low | Info | None
- Finding: <finding or "No material findings">
- Evidence / Location: <files, functions, commands, or "N/A">
- Recommended Action: <action or "None">
- Verification: <test, command, review method, or "N/A">
```

## General Software Architecture

- Checked: Yes
- Severity: Medium
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Verification command or check.

## Security And Secrets

- Checked: Yes
- Severity: High
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Verification command or check.

## Repository Hygiene

- Checked: Yes
- Severity: Low
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/path.
- Recommended Action: Minimal action.
- Verification: Verification command or check.

## Skipped Engineering Areas

- CI Maturity: Not checked because the repository has no CI files.

## AI Software Architecture

- Checked: Yes
- Severity: Medium
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Fake-client test or smoke check.

## Prompt Quality

- Checked: Yes
- Severity: Medium
- Finding: Finding with impact and minimal fix.
- Evidence / Location: Exact file/function.
- Recommended Action: Minimal action.
- Verification: Prompt fixture or review check.

## Workflow Automation

- Checked: Yes
- Severity: None
- Finding: No material findings
- Evidence / Location: Inspected workflow entry points.
- Recommended Action: None
- Verification: Existing verification.

## Skipped AI System Areas

- Speech Pipelines: Not checked because the repository has no speech pipeline.

- Backlog: small patch candidates with audit family, audit area, severity, likely
  files, risk level, characterization need, and verification command.
- Review result: mode used, files changed, verification command/result if run,
  and stopped work requiring explicit approval.
