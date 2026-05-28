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
- Exactly two main findings tables. Example rows are shown below; a real review
  includes every known audit area in the relevant table:

## Engineering Audits Table

| Audit Area | Checked? | Severity | Finding | Evidence / Location | Recommended Action | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| General Software Architecture | Yes | Medium | Finding with impact and minimal fix. | Exact file/function. | Minimal action. | Verification command or check. |
| Security And Secrets | Yes | High | Finding with impact and minimal fix. | Exact file/function. | Minimal action. | Verification command or check. |
| Repository Hygiene | Yes | Low | Finding with impact and minimal fix. | Exact file/path. | Minimal action. | Verification command or check. |
| CI Maturity | No | None | Not checked because the repository has no CI files. | N/A | Add CI only if requested or appropriate. | N/A |

## AI System Audits Table

| Audit Area | Checked? | Severity | Finding | Evidence / Location | Recommended Action | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| AI Software Architecture | Yes | Medium | Finding with impact and minimal fix. | Exact file/function. | Minimal action. | Fake-client test or smoke check. |
| Prompt Quality | Yes | Medium | Finding with impact and minimal fix. | Exact file/function. | Minimal action. | Prompt fixture or review check. |
| Workflow Automation | Yes | None | No material findings. | Inspected workflow entry points. | None. | Existing verification. |
| Speech Pipelines | No | None | Not checked because the repository has no speech pipeline. | N/A | None. | N/A |

- Backlog: small patch candidates with audit family, audit area, severity, likely
  files, risk level, characterization need, and verification command.
- Review result: mode used, files changed, verification command/result if run,
  and stopped work requiring explicit approval.
