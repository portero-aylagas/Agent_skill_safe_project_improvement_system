# AI System Audits

Use this reference for deeper review of prompts, model integrations, RAG,
agent/tool workflows, speech pipelines, and orchestrated automations. Keep
recommendations proportional to the project.

`AI Software Architecture` is the cross-cutting structure audit for AI systems.
Use it to decide whether AI-specific parts have clear ownership and boundaries.
Route detailed prompt, provider, retrieval, tool, workflow, speech, cost, and
evaluation findings to the focused areas below.

`Workflow Automation` is one audit area inside AI System Audits. It covers
multi-step AI/tool execution, retries, state transitions, approval points, logs,
run IDs, recovery paths, and cost controls.

Use each section heading below as a known `AI System Audits` area when filling
the AI System Audits Table. If an area is not relevant or not checked, keep it
in the table with `Checked?` set to `No` and explain why.

## AI Software Architecture

Check:

- provider adapters, prompt storage/wiring, and model-call boundaries have clear
  ownership
- deterministic business logic is separated from model-dependent behavior
- RAG, agent, tool, and workflow components compose through understandable
  interfaces
- dependency boundaries allow fake clients or fixtures without live services
- AI-specific structure can grow without scattering provider, prompt, or runtime
  concerns across unrelated code

Do not use this area for prompt wording, prompt variables, schemas/parsing,
provider settings, retries, timeouts, retrieval quality, tool contracts,
workflow recovery, budgets, or evaluation details. Route those findings to the
focused AI System audit areas.

Return:

- AI architecture summary
- component boundary problems
- model-dependent behavior that should be isolated
- minimal structure changes worth doing now
- focused audit areas that should own deeper follow-up

## Prompt Quality

Check:

- each prompt has a clear task, audience, constraints, and output format
- prompt inputs are explicit and separated from instructions
- zero-shot, one-shot, few-shot, or structured output is appropriate for the task
- prompt text is inspectable and not hidden inside unrelated application logic
- temperature, model choice, and determinism match the task

Return:

- prompt inventory
- current technique
- weaknesses
- minimal improved prompt examples
- what not to change

## Dynamic Prompting

Check:

- variables injected into prompts
- user input boundaries and injection risk
- duplicated prompt construction
- missing inputs and error handling
- whether prompt templates would improve maintainability

Return:

- current dynamic prompting pattern
- variables injected
- risks
- minimal improvements
- example template when useful

## Structured Output

Check:

- free text versus JSON-like text versus validated schema
- downstream dependencies on exact fields
- required and optional fields
- malformed JSON and validation error handling
- whether raw model output and parsed output are stored appropriately

Return:

- current output format
- where structured output is needed
- schema weaknesses
- minimal validation improvements
- test cases for malformed or missing fields

## LLM/API Integration

Check:

- credentials loaded from environment or secrets manager
- model names, temperature, timeout, retry policy, and token limits
- provider response parsing
- rate limits, timeouts, empty responses, and malformed responses
- whether adding a provider would require broad code changes
- whether existing abstraction is too thin, too broad, or unnecessary

Return:

- integration assessment
- provider boundary problems
- minimal improvements
- optional future improvements
- tests with fake clients

## RAG And Retrieval

Check:

- document loading, cleaning, and deterministic file discovery
- chunk size, overlap, and boundary quality
- embeddings, vector store paths, rebuild commands, and cache invalidation
- top-k, filters, ranking, empty corpus, and no-match behavior
- whether retrieved context actually answers representative questions
- whether deterministic context assembly is enough instead of vector RAG

Return:

- current RAG/context pipeline
- chunking and retrieval risks
- fixture corpus and test questions
- minimal improvements
- what would be over-engineering

## AI Evaluation Scaffolding

Check:

- representative fixtures exist where AI output quality matters
- expected output properties are documented
- malformed, empty, and edge cases are tested where appropriate
- live evaluation is separate from normal verification
- subjective output quality has manual review notes or lightweight criteria
  where needed
- evaluation expectations are proportional to the project and do not require a
  heavy platform by default

Return:

- current fixture and evaluation coverage
- expected output properties or quality criteria
- missing edge cases
- normal verification versus live evaluation boundary
- smallest useful evaluation smoke test or manual review checklist

## Agents And Tools

Check:

- whether an agent is justified instead of a simpler chain or direct call
- tool names, descriptions, input types, and output usefulness
- prompt/tool/runtime separation
- final answer extraction
- debuggability of tool calls and model calls
- tool failures and recovery behavior

Return:

- agent architecture summary
- tool inventory
- problems by file/function
- minimal improvements
- whether to keep the agent design

## Workflow Automation

Check:

- trigger conditions, idempotency, retries, and failure branches
- explicit state, node responsibilities, and conditional routing
- deterministic business rules separated from model calls
- human approval points for high-risk actions
- active run, session, and concurrent workflow behavior
- stop, restart, and recovery behavior
- workflow path tracking, logs, run IDs, and reports
- setup, credentials, and validation prompts or commands

Return:

- workflow summary
- state or node issues
- reliability and traceability risks
- concurrency and recovery risks
- evidence gaps
- minimal improvements

## Speech Pipelines

Check:

- audio loading, recording, conversion, and cleanup
- long-audio chunking and timestamp handling
- prompted versus unprompted transcription where domain vocabulary matters
- generated audio validation before merging
- transcript and audio alignment
- safe output naming

Return:

- speech pipeline summary
- STT/TTS risks
- chunking and timestamp risks
- minimal improvements
- practical evaluation checks

## Cost And Usage

Check:

- whether the app makes enough model calls to justify usage tracking
- direct provider usage versus estimates
- stale hardcoded pricing
- total requests, tokens, cost, and visible budget warnings
- whether usage tracking is mixed into business logic
- max retries, max steps, timeouts, token limits, or equivalent caps for paid or
  looping AI workflows
- high-cost modes require explicit opt-in
- configured limits are visible enough for review and debugging
- invalid config values do not silently fall back to dangerous high limits
- cost and usage tracking are proportional to the project

Return:

- current usage tracking summary
- whether tracking is necessary
- inaccuracies or missing visibility
- missing execution caps or risky defaults
- minimal improvements
- what would be unnecessary for a small project
