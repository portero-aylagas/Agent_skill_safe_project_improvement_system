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

Do not begin with refactoring. First understand the project, current behavior,
verification surface, and risks.

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

- `references/protocol.md`: read first for the full workflow and mode details.
- `references/coding-standards.md`: read before editing code or installing
  project-local rules.
- `references/characterization.md`: read before medium/high-risk changes or
  when current behavior is unclear.
- `references/audit-matrix.md`: read for review/audit/backlog work.
- `references/patch-policy.md`: read before making code changes.
- `references/testing-strategy.md`: read when adding or repairing verification.
- `references/ai-integration-quality.md`: read for prompts, providers, APIs,
  RAG, tools, agents, or evaluation.
- `references/branching-ci-hooks.md`: read only for explicit branch, hook, CI,
  commit, push, or full automation requests.

## Assets

Use `assets/` as project templates, adapting them to the target repository:

- `AGENTS.template.md`: project-local agent rules.
- `Makefile.template` and `verify.sh.template`: minimal local verification.
- `pyproject.template.toml`: beginner-friendly pytest/ruff defaults.
- `pre-commit-config.template.yaml`: low-risk hooks with optional ruff.
- `github-actions-verify.template.yaml`: CI template that runs `make verify`
  without live secrets.
- `behavior-inventory-template.md`: behavior characterization worksheet.
- `patch-backlog-template.md`: prioritized improvement backlog.

## Default Output

When work is complete, report:

- mode used
- files changed
- characterization added or confirmed
- verification command and result
- any stopped work, failed verification, or approval needed
