# Engineering Audits

Use this reference when `audit-matrix.md` shows that a deeper engineering review
is useful. Do not run every audit blindly.

## General Software Architecture

Check:

- each file has a clear purpose
- orchestration is separated from business logic
- UI, file I/O, external service calls, config, and utilities have clear
  boundaries
- imports do not create avoidable coupling or circular dependencies
- the current structure can grow without hiding important behavior
- AI-specific code connects to the application through clear module boundaries

This audit checks general software structure. Provider adapters, prompt
storage/wiring, and model-dependent architecture belong under
`AI Software Architecture`. Prompt content quality, prompting technique, and
prompt variables belong under focused `AI System Audits`.

Return:

- current architecture summary
- structural problems by file
- minimal structure changes worth doing now
- changes that would be over-engineering

## Function Responsibility

Check:

- each function has one clear responsibility
- names match behavior
- inputs, outputs, and side effects are understandable
- public functions and classes have concise Google-style docstrings unless they
  are clearly private or internal
- comments explain workflow intent, assumptions, side effects, safety
  constraints, or non-obvious guards where code alone is not enough
- UI, file I/O, API calls, and business logic are not unnecessarily mixed
- functions are not too large, too tiny to be useful, or coupled to global state

Return:

- file/function
- current responsibility
- problem
- recommended action
- priority

## Error Handling

Check:

- broad, swallowed, or silent exceptions
- unclear error messages
- API, file, JSON/parsing, user-input, and environment-variable failures
- crash behavior versus graceful failure
- whether errors explain where and why the failure happened

Return:

- file/function
- failure scenario
- current behavior
- minimal fix
- test or smoke check to add

## Testability

Check:

- logic coupled to UI frameworks, files, environment variables, or live services
- functions that should be pure or easier to call directly
- where fakes, mocks, fixtures, or dependency injection are needed
- missing edge cases and regression checks

Return:

- testability diagnosis
- functions to refactor before testing
- suggested unit tests
- suggested integration or smoke tests
- smallest useful test plan

## Data And JSON Validation

Check:

- where JSON, CSV, API responses, uploaded files, or user-provided structured
  data enter the project
- required fields, types, nulls, malformed data, and unexpected fields
- whether invalid data can silently continue through the pipeline
- whether validation logic is mixed into UI, file I/O, or API calls
- whether simple validation functions are enough before adding schemas

Return:

- data entry points
- current validation approach
- failure scenarios
- minimal validation improvements
- test cases to add

## Repository Hygiene

Check:

- committed generated files, caches, virtual environments, and large temporary
  files
- `.gitignore` coverage
- dependency files and setup instructions
- duplicate, obsolete, or confusing files
- outputs that should be examples versus local artifacts

Return:

- files/folders that should stay
- files/folders to check before removing
- suggested `.gitignore` additions
- minimal cleanup plan

## Documentation And Reviewer Evidence

Check:

- clear project goal, setup, run command, and verification command
- required environment variables with examples, not real secrets
- public module, class, and function docstrings that explain purpose, inputs,
  outputs, side effects, and important assumptions where useful
- inline workflow comments that reduce cognitive load without restating syntax
- project structure and important modules explained where useful
- sample input, expected output, known limitations, and fallback behavior for
  API, file, or input failure when needed for review or demo

Return:

- missing documentation sections
- confusing or outdated instructions
- minimal README improvements
- reviewer/demo clarity gaps that affect engineering verification

## Security And Secrets

Check:

- hardcoded API keys or committed `.env` files
- unsafe file paths or user-controlled paths
- unvalidated uploads or external documents
- prompt injection risks when documents, URLs, or user text affect model calls
- sensitive data in logs, outputs, reports, or committed artifacts

This audit treats prompt injection as an application security boundary. Prompt
wording and model behavior belong under `AI System Audits`.

Return:

- security issue
- severity
- exact location
- minimal fix
- what is acceptable for a local project versus production
