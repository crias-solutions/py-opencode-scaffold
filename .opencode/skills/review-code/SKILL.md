---
name: review-code
description: Review the current git diff for bugs, edge cases, and correctness in a fresh subagent context
---

## What I do

Review code changes (the current git diff) for bugs, edge cases, security issues, and correctness. I run in a fresh subagent context so I evaluate the result on its own terms, not biased by how it was produced.

## When to use me

Use this when:
- You've finished implementing a feature and want an independent review
- You want a second opinion on a complex change
- Before committing, to catch issues you might have missed

## Workflow

1. Run `git diff` to get the current changes
2. Review changes for:
   - **Correctness** — does the code do what it's supposed to?
   - **Edge cases** — null inputs, empty states, error paths
   - **Security** — injection, auth, secrets exposure
   - **Consistency** — follows existing patterns in the codebase
3. Report findings with specific `file:line` references
4. Flag only gaps that affect correctness or stated requirements, not style preferences
