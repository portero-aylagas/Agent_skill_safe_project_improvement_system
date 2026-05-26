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

## Characterization

- Existing tests or checks used:
- New characterization added:
- Manual checklist, if used:

## Findings By Audit Family

```text
Engineering Audits
- Audit Area
  - Severity
    - Finding

AI System Audits
- Audit Area
  - Severity
    - Finding
```

Selected areas with no issues should say `No material findings`.

## Backlog

| Priority | Audit Family | Audit Area | Severity | Risk | Finding | Proposed Patch | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

## Patch Applied

- Summary:
- Why this is one patch:
- Behavior changed:
- Public API, schema, prompt, or dependency changed:

## Verification

- Command:
- Result:
- Failure summary, if any:
- CI result, if applicable:

## Follow-Up

- Stopped work:
- Approval needed:
- Next smallest useful patch:
