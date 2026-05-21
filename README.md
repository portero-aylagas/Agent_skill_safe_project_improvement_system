# Safe Project Improvement System

Reusable rules, references, and templates for improving Python and
AI-integrated software safely with one lead agent.

The default workflow is:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

`references/protocol.md` is the canonical workflow. This README is a quick
start; if the two ever disagree, update the README to match the protocol.

## Quick Start

Run a review before changing code:

```text
Use the safe project improvement system in review mode.
Inspect this repository, characterize current behavior, run all relevant audits, and produce a prioritized backlog.
Do not edit files.
```

Then apply one safe patch at a time:

```text
Use the safe project improvement system in local safe refactor mode.
Create or confirm characterization and verification first.
Then apply only the first small safe patch and run verification.
Stop after one patch.
```

Repository verification should normally be:

```text
make verify
```

For this repository, `make verify` compiles local scripts, runs Ruff, and checks
that the core docs still point back to the canonical protocol.

## Core Rules

- Inspect before editing.
- Characterize current behavior before medium/high-risk changes.
- Keep patches focused and small.
- Verify locally after each patch.
- Avoid live API keys, network calls, and paid services in normal tests.
- Do not push, install hooks, or add strict CI without explicit approval.

Default code style:

```text
Beginner/intermediate-friendly, PEP8, Google-style docstrings, type hints at
boundaries, clear inline workflow comments, small maintainable changes, Ruff
with pydocstyle for public docstrings.
```

## Characterization Tests

Characterization tests, also known as Golden Master or Snapshot tests, capture
the exact current behavior of existing software before refactoring. Michael
Feathers coined the term in *Working Effectively with Legacy Code*.

Their purpose is not to prove the behavior is correct. Their purpose is to
freeze observable legacy behavior so refactors can be made safely. If a change
breaks current output, side effects, errors, or other observable behavior, the
test fails before the change reaches production.

See `references/characterization.md` and `references/testing-strategy.md` for
the full policy.

## Modes

- **Review Mode**: inspect, characterize, audit, and produce a prioritized
  backlog. Do not edit code.
- **Local Safe Refactor Mode**: confirm verification and characterization,
  apply one small patch, run verification, then stop.
- **Full Automation Mode**: branch, verify, patch, commit, push, and wait for CI
  only after explicit user approval.

## Adoption Modes

Use the smallest mode that fits the target repository:

- **External Reference Mode**: keep this folder available in the workspace and
  tell the agent to use it.
- **Repo-Local Guidance Mode**: copy only the needed templates, such as
  `AGENTS.md`, `Makefile`, or `verify.sh`.
- **Vendored Skill Mode**: copy the full skill bundle into the target repo,
  usually under `skills/safe_project_improvement_system/`.
- **Hybrid Mode**: keep the full skill external while adding lightweight local
  repo instructions.

Vendoring this folder does not automatically register a native skill in every
coding tool. The practical requirements are that the files are present, local
instructions point to `SKILL.md`, and the prompt explicitly says to use the
system.

Do not blindly overwrite an existing `AGENTS.md`, `Makefile`, `verify.sh`, or
`pyproject.toml`. Merge or adapt templates carefully.

See `references/integration-into-other-repos.md` for details.

## Using With Codex Or Claude Code

If Codex can read this workspace, call the system by name in the prompt. Claude
Code can use the same workflow by being pointed at this folder or a vendored
copy.

Useful prompts:

```text
Use the safe project improvement system to add a minimal verification setup.
Prefer make verify.
Do not require live API calls.
Add characterization tests before risky refactors.
```

```text
Use the vendored safe project improvement system under skills/safe_project_improvement_system/.
Treat it as a development/support skill, not as a runtime component of this application.
Do not replace existing local instruction files; merge or adapt carefully.
```

## Key Files

- `SKILL.md`: skill entry point and mode selection guidance.
- `references/protocol.md`: canonical workflow and required rules.
- `references/characterization.md`: characterization policy and examples.
- `references/testing-strategy.md`: verification and test roles.
- `references/patch-policy.md`: patch size, risk, and split criteria.
- `references/integration-into-other-repos.md`: adoption modes and boundaries.
- `assets/`: templates for target repositories.
- `examples/`: copy-paste prompts and expected response shapes.

## Templates

- Start with `assets/AGENTS.template.md` when a project needs local agent rules.
- Start with `assets/Makefile.template` and `assets/verify.sh.template` when a
  project has no verification entry point.
- Use `assets/development-skill-note.template.md` when a target repository needs
  a short note explaining that this system is a development/support skill.
- Use `assets/behavior-inventory-template.md` before risky changes.
- Use `assets/patch-backlog-template.md` to keep review findings actionable.
- Use `assets/run-report-template.md` when a review, full automation run,
  medium/high-risk patch, failed verification, or persistent backlog needs an
  audit trail.
- Use hook and CI templates only after explicit user approval.

## Test Dependencies

Templates assume the target project declares the dependencies needed by its
normal verification command. If tests use `pytest`, prefer adding `pytest` to
the target repo's existing dev/test dependency location, such as
`pyproject.toml`, `requirements-dev.txt`, or a test extra. For very small
beginner repos without a dependency convention, adding
`python -m pip install pytest` to CI is acceptable as a temporary fallback.
