"""Check that the skill repository's docs stay internally consistent."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = "inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify"

REQUIRED_PATHS = [
    "Makefile",
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
    "scripts/check_consistency.py",
    "references/protocol.md",
    "references/patch-policy.md",
    "references/testing-strategy.md",
    "references/ai-integration-quality.md",
    "assets/AGENTS.template.md",
    "assets/Makefile.template",
    "assets/verify.sh.template",
    "examples/review-mode.md",
    "examples/local-safe-refactor.md",
    "examples/install-verification.md",
]

WORKFLOW_DOCS = [
    "README.md",
    "SKILL.md",
    "references/protocol.md",
    "assets/AGENTS.template.md",
]

CANONICAL_POINTER_DOCS = [
    "README.md",
    "SKILL.md",
]

PROTOCOL_REQUIREMENTS = [
    "Do not make code changes during inspection.",
    "Characterization is mandatory before medium/high-risk changes",
    "Normal verification must not require live API keys",
    "Do not push, install hooks, or add strict CI unless explicitly authorized",
    "Use fake clients/mocks for AI/API tests.",
]

PATCH_POLICY_REQUIREMENTS = [
    "It touches more than 5 files.",
    "It changes more than 250 non-generated lines.",
    "It changes dependencies, lockfiles, packaging, or runtime versions.",
    "It changes a public API, CLI contract, schema, prompt contract, or persisted",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def check_required_paths() -> list[str]:
    errors = []
    for relative_path in REQUIRED_PATHS:
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")
    return errors


def check_workflow_phrase() -> list[str]:
    errors = []
    for relative_path in WORKFLOW_DOCS:
        if WORKFLOW not in read_text(relative_path):
            errors.append(f"missing canonical workflow phrase: {relative_path}")
    return errors


def check_canonical_pointers() -> list[str]:
    errors = []
    for relative_path in CANONICAL_POINTER_DOCS:
        text = read_text(relative_path)
        if "references/protocol.md" not in text:
            errors.append(f"missing protocol pointer: {relative_path}")
    return errors


def check_protocol_requirements() -> list[str]:
    protocol = read_text("references/protocol.md")
    errors = []
    for requirement in PROTOCOL_REQUIREMENTS:
        if requirement not in protocol:
            errors.append(f"protocol missing requirement: {requirement}")
    return errors


def check_patch_policy_requirements() -> list[str]:
    patch_policy = read_text("references/patch-policy.md")
    errors = []
    for requirement in PATCH_POLICY_REQUIREMENTS:
        if requirement not in patch_policy:
            errors.append(f"patch policy missing threshold: {requirement}")
    return errors


def check_agent_policy() -> list[str]:
    agent_config = read_text("agents/openai.yaml")
    if "allow_implicit_invocation: false" not in agent_config:
        return ["agents/openai.yaml must keep allow_implicit_invocation: false"]
    return []


def main() -> int:
    errors = []
    errors.extend(check_required_paths())
    errors.extend(check_workflow_phrase())
    errors.extend(check_canonical_pointers())
    errors.extend(check_protocol_requirements())
    errors.extend(check_patch_policy_requirements())
    errors.extend(check_agent_policy())

    if errors:
        print("Consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
