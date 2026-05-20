---
name: safe-project-improvement-system
description: >-
  Use this skill when asked to safely review, audit, refactor, improve, install
  project-local agent rules, add verification, or automate changes in Python or
  AI-integrated software. It enforces inspect, characterize, verify setup,
  audit, backlog, one patch, and verify; one lead editing agent; fake clients
  for AI/API tests, no live API keys by default, and no push/hooks/strict CI
  without explicit approval.
---

# Safe Project Improvement System

Use this skill to improve a Python or AI-integrated project safely. The operating
loop is:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

`references/protocol.md` is the authoritative workflow for this skill. The
sections below are a compact operating summary for agent use.

Do not begin with refactoring. First understand the project, current behavior,
verification surface, and risks.

## Adoption Context

This skill may be used from a shared external repository, from a small repo-local
guidance install, or from a vendored full copy under a target repository such as
`skills/safe_project_improvement_system/`.

Installing a few templates is not the same as vendoring the full skill bundle.

If the target repository already has `AGENTS.md`, `Makefile`, `verify.sh`, or
similar local files, merge carefully instead of overwriting them.

When the skill is vendored into another repository for traceability, it is
usually a `development/support skill`, not a runtime/project skill, unless that
repository explicitly integrates it into runtime behavior.

## Mode Selection

- **Review Mode**: inspect, characterize, audit, and produce a prioritized
  backlog. Do not edit files.
- **Local Safe Refactor Mode**: create or confirm characterization and
  verification, apply one small patch, run local verification, then stop. Use
  this by default when the user asks to refactor or improve code.
- **Full Automation Mode**: create a branch, add verification/tests, patch,
  commit, push, wait for CI, and report. Use only after explicit user approval.

If the user says audit, review, or planning only, use Review Mode.

## Non-Negotiable Rules

- Use one lead agent for edits.
- Always inspect the project before changing it.
- Characterization is mandatory before medium/high-risk code changes.
- Every code-changing patch needs verification.
- Do not combine refactor, feature change, dependency change, UI change, and
  cleanup in one patch.
- Do not push, install hooks, or add strict CI unless explicitly authorized.
- Use fake clients/mocks for AI/API tests.
- Normal verification must not require live API keys.
- Stop if verification fails.

## Reference Loading

Load only the references needed for the current task:

Review mode always loads `references/protocol.md`,
`references/audit-matrix.md`, and `references/coding-standards.md`.

Deep audit references are optional. In review mode, load
`references/engineering-audits.md` for software engineering quality reviews. Load
`references/ai-workflow-audits.md` or `references/ai-integration-quality.md` for
AI, API, prompt, RAG, tool, agent, or workflow repositories. Load both
engineering and AI/workflow references only when the repository clearly has both
general software architecture risks and AI/workflow-specific risks. Do not load
deep audit references during local safe refactor mode unless the patch directly
touches that area.

- `references/protocol.md`: read first for the full workflow and mode details.
- `references/coding-standards.md`: read before reviewing, editing,
  refactoring, or installing project-local rules.
- `references/characterization.md`: read before medium/high-risk changes or
  when current behavior is unclear.
- `references/audit-matrix.md`: read for review/audit/backlog work.
- `references/engineering-audits.md`: read when review mode needs deeper
  architecture, error handling, testability, validation, documentation, hygiene,
  UI separation, or security checks.
- `references/ai-workflow-audits.md`: read when review mode needs deeper prompt,
  structured output, RAG, agent/tool, speech, cost, or workflow automation checks.
- `references/patch-policy.md`: read before making code changes.
- `references/testing-strategy.md`: read when adding or repairing verification.
- `references/ai-integration-quality.md`: read for prompts, providers, APIs,
  RAG, tools, agents, or evaluation.
- `references/branching-ci-hooks.md`: read only for explicit branch, hook, CI,
  commit, push, or full automation requests.

## Implementation Definition Of Done

For implementation work, public modules, classes, and functions should have
concise Google-style docstrings unless they are clearly private or internal.

Code should be beginner/intermediate-friendly: clear names, simple control flow,
explicit side effects, understandable module boundaries, and comments where they
reduce the reader's cognitive load.

## Assets

Use `assets/` as project templates, adapting them to the target repository:

- `AGENTS.template.md`: project-local agent rules.
- `development-skill-note.template.md`: local note for repositories that need
  to document this system as a development/support skill.
- `Makefile.template` and `verify.sh.template`: minimal local verification.
- `pyproject.template.toml`: beginner-friendly pytest/ruff defaults.
- `pre-commit-config.template.yaml`: low-risk hooks with optional ruff.
- `github-actions-verify.template.yaml`: CI template that runs `make verify`
  without live secrets.
- `behavior-inventory-template.md`: behavior characterization worksheet.
- `patch-backlog-template.md`: prioritized improvement backlog.
- `run-report-template.md`: optional audit trail for review, full automation,
  medium/high-risk patches, verification failures, or persistent backlogs.

## Default Output

When work is complete, report:

- mode used
- files changed
- characterization added or confirmed
- verification command and result
- any stopped work, failed verification, or approval needed
