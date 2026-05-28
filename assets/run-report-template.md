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

Engineering Audits: repeat the finding block for checked Engineering areas with
findings, or the compact block for checked Engineering areas with no material
findings.

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

## Skipped Engineering Areas

- <Audit Area>: <reason>

AI System Audits: repeat the finding block for checked AI System areas with
findings, or the compact block for checked AI System areas with no material
findings.

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

## Skipped AI System Areas

- <Audit Area>: <reason>

When this report includes audit findings, do not omit checked areas. Do not
include the old checked marker, none-severity placeholder, or empty
recommended-action placeholder.
Skipped areas do not need full blocks and must appear only under the relevant
skipped-area section. Tables may only be used for short metadata summaries, not
detailed findings.

## Backlog

### P001

- Priority:
- Audit Family:
- Audit Area:
- Severity:
- Risk:
- Finding:
- Proposed Patch:
- Verification:

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
