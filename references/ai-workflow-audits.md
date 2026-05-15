# AI And Workflow Audits

Use this reference for deeper review of prompts, model integrations, RAG,
agent/tool workflows, speech pipelines, and orchestrated automations. Keep
recommendations proportional to the project.

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
- workflow path tracking, logs, run IDs, and reports
- setup, credentials, and validation prompts or commands

Return:

- workflow summary
- state or node issues
- reliability and traceability risks
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

Return:

- current usage tracking summary
- whether tracking is necessary
- inaccuracies or missing visibility
- minimal improvements
- what would be unnecessary for a small project
