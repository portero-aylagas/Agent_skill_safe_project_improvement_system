# Audit Matrix

Use this matrix to choose relevant audits. Do not run every audit blindly. Deep
audit references are optional; load at most one by default, and load both only
when the repository clearly combines software architecture risks with
AI/workflow-specific risks.

## Python Scripts and Packages

- Entry points: scripts, modules, CLI commands, notebooks converted to scripts.
- Imports: missing dependencies, circular imports, import-time side effects.
- Configuration: environment variables, defaults, `.env.example`.
- Errors: clear exceptions, no swallowed failures, useful messages.
- Data handling: schemas, file paths, encoding, input validation.
- Verification: compile/import checks, pytest, smoke tests.
- Documentation: clear run command, sample input, expected output, limitations,
  and fallback behavior when needed for review or demo.

## AI Integration Projects

- Provider boundary: one place for model/API calls.
- Credentials: no required live keys for tests, no secrets committed.
- Prompt quality: named prompts, versionable text, clear inputs/outputs.
- Prompt technique: zero-shot, few-shot, or structured output chosen deliberately.
- Determinism: configurable temperature, stable fake-client tests.
- Failure modes: rate limits, timeouts, empty responses, malformed JSON.
- Cost and safety: token limits, retries, logging without sensitive data.

## RAG Projects

- Corpus loading: deterministic file discovery and encodings.
- Chunking: documented size/overlap strategy.
- Embeddings: provider/config separated from retrieval logic.
- Retrieval: top-k, filtering, ranking, empty-result behavior.
- Evaluation: small fixture corpus with expected retrievals.
- Persistence: vector store paths, rebuild commands, cache invalidation.

## API Services

- Request validation and response schemas.
- Error status codes and error bodies.
- Dependency injection for clients and databases.
- Startup behavior without live optional services.
- Contract tests for public endpoints.
- Health checks that do not leak secrets.

## UI Projects

- Main user workflows and state transitions.
- UI/backend separation: callbacks validate inputs and call clean backend
  functions.
- Form validation and error display.
- Accessibility basics: labels, keyboard paths, contrast.
- Responsive layout for important views.
- API failure and loading states.
- Build or smoke verification.

## Workflow and Automation Projects

- Trigger conditions and idempotency.
- Error handling, retries, and dead-letter paths.
- Credential isolation.
- Dry-run or fake-service mode.
- Observability: logs, run IDs, summaries.
- Rollback or manual recovery notes.

## Backlog Prioritization

Rank findings by:

- user impact
- risk of regression
- ease of verification
- isolation of patch
- dependency on approvals or live services
