# Safe Project Improvement System

Reusable rules, references, and templates for improving Python and AI-integrated
software safely with one lead agent.

The default workflow is:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

`references/protocol.md` is the canonical workflow. This README is a quick
start; if the two ever disagree, update the README to match the protocol.

Default code style:

```text
Beginner/intermediate-friendly, PEP8, Google-style docstrings, type hints at
boundaries, clear inline workflow comments, small maintainable changes.
```

## How To Use

You can use this system in two ways:

### Option 1: Use it directly from an agent session

Use this when Codex or Claude Code can already read this
`safe_project_improvement_system/` folder from the workspace.

You do not need to copy the whole folder into the target repository. Instead,
tell the agent to use the system and name the mode you want.

Example prompt for Codex or Claude Code:

```text
Use the safe project improvement system in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

Example safe refactor prompt:

```text
Use the safe project improvement system in local safe refactor mode.
Create or confirm characterization and verification first.
Then apply only the first small safe patch and run verification.
Stop after one patch.
```

### Option 2: Install repo-local files

Use this when you want the target repository to keep its own local rules,
verification templates, and onboarding files.

In that case, copy and adapt only the files you need:

- `assets/AGENTS.template.md` -> `AGENTS.md`
- `assets/Makefile.template` -> `Makefile`
- `assets/verify.sh.template` -> `verify.sh`
- `assets/behavior-inventory-template.md` -> optional working document
- `assets/patch-backlog-template.md` -> optional working document
- hook and CI templates only when explicitly desired

After that, ask the agent to install or adapt those files for the current repo.

Example prompt:

```text
Use the safe project improvement system to install project-local agent rules.
Adapt AGENTS.template.md to this repository.
Do not change application code.
```

## Using With Codex

If Codex has access to this workspace, call the system by name in the prompt.

Typical sequence:

1. Run `review mode` first.
2. Review the backlog.
3. Run `local safe refactor mode` for one patch.
4. Repeat one patch at a time.

Example prompts:

```text
Use the safe project improvement system in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

```text
Use the safe project improvement system in local safe refactor mode.
Create or confirm characterization and verification first.
Then apply only the first small safe patch and run verification.
Stop after one patch.
```

```text
Use the safe project improvement system to add a minimal verification setup.
Prefer make verify.
Do not require live API calls.
Add characterization tests before risky refactors.
```

## Using With Claude Code

Claude Code can use the same workflow even if it does not support Codex skills in
the same native way. The practical method is:

1. Keep this folder available in the workspace, or copy the needed templates into
   the target repo.
2. Paste one of the prompts from this README.
3. Tell Claude Code to follow the rules from `safe_project_improvement_system/`.

Example prompt:

```text
Use the rules and workflow from safe_project_improvement_system/.
Work in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

If you want the target repo to be self-contained for Claude Code, install
`AGENTS.md` and the verification files in the repo root first.

## Contents

```text
safe_project_improvement_system/
-> Makefile
-> README.md
-> SKILL.md
-> .github/workflows/verify.yml
-> agents/openai.yaml
-> scripts/
   -> check_consistency.py
-> examples/
   -> review-mode.md
   -> local-safe-refactor.md
   -> install-verification.md
-> references/
   -> protocol.md
   -> coding-standards.md
   -> characterization.md
   -> audit-matrix.md
   -> patch-policy.md
   -> testing-strategy.md
   -> ai-integration-quality.md
   -> branching-ci-hooks.md
-> assets/
   -> AGENTS.template.md
   -> Makefile.template
   -> verify.sh.template
   -> pyproject.template.toml
   -> pre-commit-config.template.yaml
   -> github-actions-verify.template.yaml
   -> behavior-inventory-template.md
   -> patch-backlog-template.md
```

## Modes

- **Review Mode**: inspect, characterize, audit, and produce a prioritized
  backlog. Do not edit code.
- **Local Safe Refactor Mode**: confirm verification and characterization, apply
  one small patch, run verification, then stop.
- **Full Automation Mode**: branch, verify, patch, commit, push, and wait for CI
  only after explicit user approval.

## Required Rules

Follow `references/protocol.md` for the complete required rules. The shortest
version is: inspect first, characterize before medium/high-risk changes, make
one focused patch, verify it locally, avoid live API keys by default, and do not
push, install hooks, or add strict CI without explicit approval.

## Repository Verification

This repository verifies itself with:

```text
make verify
```

The root verification compiles local scripts and checks that the key docs still
point back to the canonical protocol.

## Patch Risk Policy

```text
Low risk: docs, comments, README, minor hygiene.
Medium risk: validation, prompts, error handling, API wrappers, config.
High risk: architecture, module moves, schemas, public interfaces, RAG retrieval,
async, provider behavior.
```

Characterization is mandatory before medium/high-risk changes. It can be
automated tests, smoke scripts, or a repeatable manual checklist. Manual
characterization is temporary and should become automated when practical.

## Copy-Paste Prompts

### Audit only

```text
Use the safe project improvement system in review mode.
Inspect this project, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

### Safe refactor

```text
Use the safe project improvement system in local safe refactor mode.
Create or confirm characterization and verification first.
Then apply only the first small safe patch and run verification.
Stop after one patch.
```

### Install project rules

```text
Use the safe project improvement system to install project-local agent rules.
Adapt AGENTS.template.md to this repository.
Do not change application code.
```

### Install verification

```text
Use the safe project improvement system to add a minimal verification setup.
Prefer make verify.
Do not require live API calls.
Add characterization tests before risky refactors.
```

## Using the Templates

- Start with `assets/AGENTS.template.md` when a project needs local agent rules.
- Start with `assets/Makefile.template` and `assets/verify.sh.template` when a
  project has no verification entry point.
- Use `assets/behavior-inventory-template.md` before risky changes.
- Use `assets/patch-backlog-template.md` to keep review findings actionable.
- Use hook and CI templates only after explicit user approval.
- Use `examples/` for copy-paste prompts and expected response shapes.

## Test Dependencies

Templates assume the target project declares the dependencies needed by its
normal verification command. If tests use `pytest`, prefer adding `pytest` to the
target repo's existing dev/test dependency location, such as `pyproject.toml`,
`requirements-dev.txt`, or a test extra. For very small beginner repos without a
dependency convention, adding `python -m pip install pytest` to CI is acceptable
as a temporary fallback.
