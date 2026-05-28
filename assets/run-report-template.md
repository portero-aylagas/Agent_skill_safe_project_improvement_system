# Safe Improvement Run Report

Use this template when a run needs a durable audit trail. Keep it short for
small patches.

## Metadata

- Date:
- Mode:
- Repository:
- Branch:
- Commit before:
- Commit after:
- Agent:
- User approval:

## Scope

- User request:
- Audit families and areas selected:
- Audit families and areas skipped:
- Scope selection reason:
- Files inspected:
- Files changed:
- Out of scope:

## Requirements Ledger

Keep this short. Include rows that affected scope, approval, backlog selection,
Full Automation, deferrals, conflicts, or explicit requirements/status
reporting.

| Requirement | Source | Must/Should | Planned Evidence Or Verification | Status Or Deferral |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Characterization

- Existing tests or checks used:
- New characterization added:
- Manual checklist, if used:

## Engineering Audits Table

| Audit Area | Checked? | Severity | Finding | Evidence / Location | Recommended Action | Verification |
| --- | --- | --- | --- | --- | --- | --- |
|  | Yes/No | High/Medium/Low/Info/None |  |  |  |  |

## AI System Audits Table

| Audit Area | Checked? | Severity | Finding | Evidence / Location | Recommended Action | Verification |
| --- | --- | --- | --- | --- | --- | --- |
|  | Yes/No | High/Medium/Low/Info/None |  |  |  |  |

When this report includes audit findings, every known audit area should appear
in the relevant table. Areas with no issues should say `No material findings`.
Areas not checked should use `Checked? = No` and explain why. Use `N/A` only
when the run report does not include audit findings.

## Backlog

| Priority | Audit Family | Audit Area | Severity | Risk | Finding | Proposed Patch | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

## Patch Applied

- Summary:
- Why this is one patch:
- Behavior changed:
- Public API, schema, prompt, or dependency changed:
- Findings remediated:
- Findings deferred and why:

## Pre-Publish Gate

Complete this section for Full Automation or other commit/push/pull request
work. Use `N/A` when no publish action is in scope.

- Selected findings mapped to code, tests, docs, or deferral:
- Requirements Ledger must-have items satisfied or deferred:
- Run report required and present:
- Commit strategy:
- Patch size/scope thresholds respected or justified:
- Pull request body has real summary and verification:
- No fake issue references or placeholder metadata:
- CI result checked after push:
- Final handoff after process artifacts complete:

## Verification

- Command:
- Result:
- Failure summary, if any:
- CI result, if applicable:

## Follow-Up

- Stopped work:
- Approval needed:
- Next smallest useful patch:
