# Integration Into Other Repositories

Use this note when deciding how to apply the safe project improvement system to
another repository.

## Modes

### External Reference Mode

Use the skill from its original repository when the agent can read both
repositories in the same workspace.

### Repo-Local Guidance Mode

Copy only a small subset of templates such as `AGENTS.md`, `Makefile`, and
`verify.sh`.

This mode provides local guidance, not the full skill bundle.

### Vendored Skill Mode

Copy the full skill bundle into the target repository, typically under:

```text
skills/safe_project_improvement_system/
```

Use this when the target repository needs traceability or local availability for
future agent sessions.

### Hybrid Mode

Keep the full skill external while also adding small repo-local instructions in
the target repository.

## Native Skill Boundary

Vendoring this folder into another repository does not automatically register it
as a native skill in every coding tool.

The practical requirement is simpler:

- the files must be present
- local instructions should point to `SKILL.md`
- prompts should explicitly say to use the skill

## Existing File Safety

Do not blindly overwrite these files in the target repository:

- `AGENTS.md`
- `Makefile`
- `verify.sh`
- `pyproject.toml`

Merge or adapt carefully.

## Recommended Target-Repo Wording

When this system is used only to help develop another project, describe it as:

```text
development/support skill
```

Do not describe it as a runtime/project skill unless the target repository
explicitly integrates it into application behavior.
