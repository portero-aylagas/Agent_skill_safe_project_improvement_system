# AI Integration Quality

Use this reference for projects that call models, tool APIs, embedding services,
RAG pipelines, or agent frameworks.

## Provider Boundaries

- Keep external provider calls behind small wrappers.
- Pass clients into business logic rather than constructing them everywhere.
- Centralize model names, timeouts, retry policy, token limits, and temperature.
- Keep provider response parsing close to the provider boundary.
- Return plain project data structures from wrappers.

## Prompts

- Give important prompts stable names.
- Keep prompt inputs explicit.
- Document expected output format.
- Validate structured outputs.
- Characterize current prompt behavior before prompt changes.
- Avoid mixing prompt edits with unrelated refactors.

## Configuration

- Read credentials from environment variables or a secrets manager.
- Provide `.env.example` without real secrets.
- Make local tests pass with fake credentials or no credentials.
- Fail fast with clear messages when live mode needs missing configuration.

## RAG

- Keep loading, chunking, embedding, retrieval, and generation separately testable.
- Use a tiny fixture corpus for retrieval characterization.
- Test empty corpus and no-match behavior.
- Keep chunking parameters visible and documented.
- Avoid changing retrieval behavior and answer-generation prompts in one patch.

## Evaluation

Start with lightweight evaluation:

- 5-20 representative cases
- expected answer properties or retrieved document IDs
- deterministic fake clients where possible
- manual review notes for subjective quality

Use live evaluation only when explicitly authorized and when cost/credentials are
understood.

## Logging

- Log enough to debug provider failures.
- Do not log secrets, full credentials, or sensitive user data.
- Include request IDs or workflow IDs when available.
