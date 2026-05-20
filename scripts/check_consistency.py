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
    "references/engineering-audits.md",
    "references/ai-workflow-audits.md",
    "references/patch-policy.md",
    "references/testing-strategy.md",
    "references/ai-integration-quality.md",
    "assets/AGENTS.template.md",
    "assets/Makefile.template",
    "assets/verify.sh.template",
    "assets/run-report-template.md",
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
    "assets/AGENTS.template.md",
]

AGENTS_TEMPLATE_REQUIREMENTS = [
    "Default to beginner/intermediate-friendly code unless this repository already",
    "Use `references/patch-policy.md` for patch-size thresholds and split criteria.",
    "Public modules, classes, and functions should have concise Google-style",
]

PROTOCOL_REQUIREMENTS = [
    "Do not make code changes during inspection.",
    "Characterization is mandatory before medium/high-risk changes",
    "Normal verification must not require live API keys",
    "Do not push, install hooks, or add strict CI unless explicitly authorized",
    "Use fake clients/mocks for AI/API tests.",
    "When reviewing software engineering quality, assess conformance to",
    "`references/coding-standards.md`",
]

CODING_STANDARDS_REQUIREMENTS = [
    "Use these standards when reviewing, editing, refactoring, or installing",
    "Implementation work should be beginner/intermediate-friendly",
    "Use comments as a comprehension tool, not decoration.",
    "Include public module, class, and function docstrings in software engineering",
]

PATCH_POLICY_REQUIREMENTS = [
    "It touches more than 5 files.",
    "It changes more than 250 non-generated lines.",
    "It changes dependencies, lockfiles, packaging, or runtime versions.",
    "It changes a public API, CLI contract, schema, prompt contract, or persisted",
]

TESTING_STRATEGY_REQUIREMENTS = [
    "Characterization tests protect existing behavior before medium/high-risk",
    "Patch tests prove the intended new behavior introduced by the current patch.",
    "Full verification runs the repository's normal checks after the patch",
    "intentional behavior change that needs a deliberate test update",
]

RUN_ARTIFACT_REQUIREMENTS = [
    "Use `assets/run-report-template.md` when a run needs a durable audit trail.",
    "the mode is full automation",
    "verification fails",
    "For low-risk local patches, the final chat report is usually enough.",
]

DEEP_AUDIT_REQUIREMENTS = [
    "references/engineering-audits.md",
    "references/ai-workflow-audits.md",
    "references/coding-standards.md",
    "Review mode always loads `references/protocol.md`",
    "Deep audit references are optional. In review mode, load",
    "AI/workflow references only when the repository",
    "except where the protocol requires one for the",
    "audit references during local safe refactor mode unless the patch directly",
    "Prompt technique: zero-shot, few-shot, or structured output chosen deliberately.",
    "UI/backend separation: callbacks validate inputs and call clean backend",
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


def check_coding_standards_requirements() -> list[str]:
    coding_standards = read_text("references/coding-standards.md")
    errors = []
    for requirement in CODING_STANDARDS_REQUIREMENTS:
        if requirement not in coding_standards:
            errors.append(f"coding standards missing requirement: {requirement}")
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


def check_testing_strategy_requirements() -> list[str]:
    testing_strategy = read_text("references/testing-strategy.md")
    errors = []
    for requirement in TESTING_STRATEGY_REQUIREMENTS:
        if requirement not in testing_strategy:
            errors.append(f"testing strategy missing requirement: {requirement}")
    return errors


def check_run_artifact_requirements() -> list[str]:
    protocol = read_text("references/protocol.md")
    report_template = read_text("assets/run-report-template.md")
    errors = []
    for requirement in RUN_ARTIFACT_REQUIREMENTS:
        if requirement not in protocol:
            errors.append(f"protocol missing run artifact requirement: {requirement}")
    if "## Metadata" not in report_template or "## Verification" not in report_template:
        errors.append("run report template missing required sections")
    return errors


def check_deep_audit_requirements() -> list[str]:
    skill = read_text("SKILL.md")
    audit_matrix = read_text("references/audit-matrix.md")
    engineering = read_text("references/engineering-audits.md")
    ai_workflow = read_text("references/ai-workflow-audits.md")
    errors = []
    for requirement in DEEP_AUDIT_REQUIREMENTS:
        if requirement not in skill and requirement not in audit_matrix:
            errors.append(f"missing deep audit requirement: {requirement}")
    if "## Error Handling" not in engineering or "## Testability" not in engineering:
        errors.append("engineering audits missing core sections")
    if "## Prompt Quality" not in ai_workflow or "## RAG And Retrieval" not in ai_workflow:
        errors.append("AI workflow audits missing core sections")
    return errors


def check_agents_template_requirements() -> list[str]:
    agents_template = read_text("assets/AGENTS.template.md")
    errors = []
    for requirement in AGENTS_TEMPLATE_REQUIREMENTS:
        if requirement not in agents_template:
            errors.append(f"AGENTS template missing requirement: {requirement}")
    return errors


def main() -> int:
    errors = []
    errors.extend(check_required_paths())
    errors.extend(check_workflow_phrase())
    errors.extend(check_canonical_pointers())
    errors.extend(check_protocol_requirements())
    errors.extend(check_coding_standards_requirements())
    errors.extend(check_patch_policy_requirements())
    errors.extend(check_testing_strategy_requirements())
    errors.extend(check_run_artifact_requirements())
    errors.extend(check_deep_audit_requirements())
    errors.extend(check_agent_policy())
    errors.extend(check_agents_template_requirements())

    if errors:
        print("Consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
