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


def main() -> int:
    errors = []
    errors.extend(check_required_paths())
    errors.extend(check_workflow_phrase())
    errors.extend(check_canonical_pointers())
    errors.extend(check_protocol_requirements())

    if errors:
        print("Consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
