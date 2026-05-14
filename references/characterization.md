# Characterization

Characterization captures what the project currently does before changing it.

## Rule

Characterization is mandatory before medium/high-risk changes.

It can be:

- automated tests
- smoke scripts
- golden input/output fixtures
- snapshots of stable structured outputs
- a repeatable manual checklist

Manual characterization is temporary and should become automated when practical.

## When It Is Required

Required before changing:

- validation behavior
- prompts or model parameters
- API wrappers and provider adapters
- configuration loading
- schemas or public interfaces
- RAG retrieval, chunking, embeddings, or ranking
- async/concurrency behavior
- architecture or module boundaries

Usually not required for:

- docs-only edits
- comments
- typo fixes
- formatting of isolated code with existing tests

## How to Characterize

1. Identify 2-5 important user workflows or API calls.
2. Capture representative inputs, including at least one edge case.
3. Record expected outputs, side effects, logs, files, or errors.
4. Prefer fake clients for external systems.
5. Add a verification command that can be run locally.

## AI/API Examples

Use fake clients that return deterministic responses:

```python
class FakeChatClient:
    def complete(self, prompt: str) -> str:
        return "fixed test response"
```

Avoid tests that need real credentials, network access, or paid services.

## Manual Checklist Template

```text
Behavior:
Input:
Expected output:
Expected side effects:
How to run:
Known limitations:
Date characterized:
```
