# Protocol

Use this protocol for safe project improvement with one lead editing agent.

## Default Workflow

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

## Non-Negotiable Rules

- Use one lead agent for edits.
- Always inspect the project before changing it.
- Characterization is mandatory before medium/high-risk changes.
- Every code-changing patch needs verification.
- Do not combine refactor, feature change, dependency change, UI change, and
  cleanup in one patch.
- Do not push, install hooks, or add strict CI unless explicitly authorized.
- Use fake clients/mocks for AI/API tests.
- Normal verification must not require live API keys.
- Stop if verification fails.

## Step 1: Inspect

Identify:

- project type and entry points
- package manager and runtime
- tests, scripts, Makefile targets, CI, hooks, and linting
- environment variables and live-service dependencies
- public interfaces, schemas, prompts, and provider boundaries
- uncommitted or unrelated work that must not be reverted

Do not make code changes during inspection.

## Step 2: Characterize

Before medium/high-risk changes, capture current behavior with one of:

- existing automated tests
- new focused characterization tests
- a smoke script with fake clients
- a repeatable manual checklist

Manual characterization is acceptable temporarily, but prefer automation when
practical.

## Step 3: Verify Setup

Find or add a normal local verification command. Prefer:

```text
make verify
```

Verification should normally include import/compile checks and tests. It must not
require live API keys.

## Audit Scope Gate

Before audit, backlog, or patch selection in any mode, make the audit scope
visible.

First inspect enough project structure to choose relevant audit areas. Then
report:

- selected audit families and areas
- skipped audit families and areas
- what each selected area checks
- why each selected area applies to this repository

Ask the user to choose the scope unless the prompt already gives explicit scope.
If interaction is unavailable, proceed with the recommended relevant scope and
report that default.

Use these user-facing audit families:

- `Engineering Audits`
- `AI System Audits`

`AI System Audits` covers prompts, model/API integrations, RAG, agents, tools,
speech, cost, and multi-step AI/tool automation. `Workflow Automation` is an
audit area inside `AI System Audits`; it means trigger conditions, idempotency,
retries, state transitions, approvals, logs, run IDs, recovery paths, and cost
controls.

## Step 4: Audit

Run only audits relevant to the project. Use `audit-matrix.md` to choose checks.
Record findings as backlog items with risk, expected behavior, and verification.
When reviewing software engineering quality, assess conformance to
`coding-standards.md`; it is the source of truth for code-level standards.

Group findings by audit family, then audit area, then severity. Do not return a
single mixed severity list. Selected areas with no issues should say
`No material findings`.

Use this finding shape:

```text
Findings By Audit Family

Engineering Audits
- Security And Secrets
  - High
    - Finding...

AI System Audits
- Prompt Quality
  - Medium
    - Finding...
```

## Step 5: Backlog

Prioritize small patches. Each backlog item should name:

- audit family
- audit area
- severity
- user-visible value or risk reduction
- files likely affected
- patch risk level
- characterization requirement
- verification command

## Step 6: One Patch

Apply one small patch only. Do not combine unrelated change types. A patch must be
small enough that failure is easy to understand and revert manually.

## Step 7: Verify

Run the agreed verification for the whole relevant repository surface, not only
the new or focused test. Stop if it fails. Report the failure, what changed, and
the smallest next diagnostic step.

## Run Artifacts

Use `assets/run-report-template.md` when a run needs a durable audit trail.
Create a run report when:

- the user asks for an audit log or run artifact
- the mode is full automation
- the patch is medium/high risk
- verification fails
- the run produces a backlog intended to persist

For low-risk local patches, the final chat report is usually enough.

## Modes

### Review Mode

Use when the user asks for audit, review, assessment, backlog, or planning.
Pass through the Audit Scope Gate before producing findings or backlog items.

Always load:

- `references/protocol.md`
- `references/audit-matrix.md`
- `references/coding-standards.md`

For software engineering quality reviews, also load
`references/engineering-audits.md`. For AI System Audits, also load
`references/ai-workflow-audits.md` or
`references/ai-integration-quality.md`.

Allowed:

- inspect files
- run safe read-only commands
- run existing verification when useful
- create a written backlog in the response

Not allowed:

- edit files
- add tests
- install hooks
- create branches
- commit or push

### Local Safe Refactor Mode

Use by default when the user asks to refactor or improve code.
Pass through the Audit Scope Gate before selecting the one patch.

Allowed:

- inspect project
- add or confirm verification
- add characterization before medium/high-risk change
- make one small local patch
- run local verification

Stop after one patch and report. Continue only if the user asks for another
patch.

### Full Automation Mode

Use only with explicit approval.
Pass through the Audit Scope Gate before backlog, patch selection, run report,
or CI follow-up work.

Allowed after approval:

- create a branch
- add verification and characterization
- make one small patch
- commit
- push
- wait for CI
- report CI result

Still required:

- no live API keys in normal verification
- no unrelated cleanup
- stop on verification failure
