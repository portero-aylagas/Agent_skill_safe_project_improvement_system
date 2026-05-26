# Local Safe Refactor Example

## Prompt

```text
Use the safe project improvement system in local safe refactor mode.
Create or confirm characterization and verification first.
Then apply only the first small safe patch and run verification.
Stop after one patch.
```

## Expected Output Shape

- Mode used: local safe refactor mode.
- Audit scope stated before findings, backlog, or patch selection.
- Characterization confirmed or added before the change.
- One patch applied with a single primary purpose.
- Files changed: only the files needed for that patch.
- Verification command and result, normally `make verify`.
- Remaining backlog: next smallest useful patch, if any.
