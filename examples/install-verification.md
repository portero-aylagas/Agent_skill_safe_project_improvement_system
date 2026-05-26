# Install Verification Example

## Prompt

```text
Use the safe project improvement system to add a minimal verification setup.
Prefer make verify.
Do not require live API calls.
Add characterization tests before risky refactors.
```

## Expected Output Shape

- Mode used: local safe refactor mode unless the user asked for review only.
- Audit scope stated before findings, backlog, or patch selection.
- Verification added or confirmed, preferably through `make verify`.
- Normal verification avoids live API keys, network services, and paid APIs.
- Characterization added only when the requested change is medium/high risk.
- Verification command and result.
- Stopped work: hooks, strict CI, branch changes, or pushes that need explicit approval.
