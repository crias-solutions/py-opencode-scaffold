# AGENTS.md — py-opencode-scaffold

## Template lifecycle

- **MUST** update project name and description in this file when creating a new project from this template.
- Resolve the black/ruff formatter conflict: Ruff is the VS Code default formatter (`charliermarsh.ruff`); `black` in `requirements.txt` is redundant and should be removed.
- Add a `pyproject.toml` if your project needs one — the template ships without package configuration by design.

## Starting point

- `src/` and `tests/` directories do not exist — create them as you add code.
- No `pyproject.toml`, `setup.py`, or `setup.cfg` — configure your tooling (mypy, pytest, ruff) as you go.
- OpenCode reads this file automatically on every session; keep it current.

## Pre-installed tooling

- `opencode` CLI (global npm, installed via `postCreateCommand`)
- `uv` (installed via `astral.sh/uv/install.sh`)
- `specify-cli` (via `uv tool install specify-cli`)
- `get-shit-done-cc` (global npm)
- `find-skills` skill (installed via `npx skills add` in `postCreateCommand`)
- `design-md` skill (`.opencode/skills/design-md/SKILL.md`) — scaffold a DESIGN.md using the Google Stitch format
- `review-code` skill (`.opencode/skills/review-code/SKILL.md`) — review the current diff for bugs, edge cases, and correctness in a fresh subagent context

## Essential commands

### Dependencies

```bash
pip install <package> && pip freeze > requirements.txt
```

### Testing

```bash
pytest                                            # all tests
pytest tests/test_file.py::function_name           # single test
pytest --cov=src --cov-report=term-missing         # with coverage
```

### Code quality

```bash
ruff check .      # lint
ruff format .     # format
mypy src/         # type check
```

### AI workflows (pre-installed)

```bash
/speckit.specify        # Start feature specification
/speckit.plan           # Create implementation plan
/speckit.tasks          # Break plan into tasks
/speckit.implement      # Implement tasks
/gsd:new-project        # Start GSD workflow
/gsd:execute-phase N    # Execute phase N

## Context management

OpenCode's context window fills up with conversation, file reads, and command output. Performance degrades as it fills. Manage it actively.

- **Run `/clear` between unrelated tasks** to reset the context window entirely. A clean session with a better prompt almost always outperforms a long session with accumulated corrections.
- **Use subagents for investigation.** When you need to explore the codebase, delegate to a subagent via the `task` tool. The subagent reads files in its own context and reports back summaries, keeping your main conversation clean.
- **Name sessions** with `/rename` and treat them like branches — each workstream gets its own persistent context.
- **`/compact`** to manually trigger context compaction with specific instructions (e.g., `Focus on the API changes`).

## Verification-first

Give OpenCode a check it can run: tests, lint, typecheck, a build step. Without it, the only signal OpenCode has that work is done is "looks done."

```bash
# Good — give a verification command in your prompt
"Implement X. Run pytest tests/test_x.py after and fix any failures."

# Better — close the loop in one prompt
"Fix the bug in src/auth.py. Reproduce it with a failing test first,
then fix until the test passes."
```

When the check exists, OpenCode does the work, runs the check, reads the result, and iterates until it passes — without you watching.

Review the evidence (test output, lint results) rather than taking "done" at face value.

## Explore → Plan → Implement

Separate research and planning from implementation to avoid solving the wrong problem.

1. **Explore** — Search the codebase and understand existing patterns before proposing changes. Use subagents for heavy research.
2. **Plan** — Use `/speckit.plan` or `/speckit.specify` to create a detailed plan. Review it before proceeding.
3. **Implement** — Execute the plan. Run verification checks after each step.
4. **Verify** — Run tests, lint, typecheck. Use the `review-code` skill for an independent review.

This maps cleanly to the pre-installed spec-kit and GSD workflows:
- `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`
- `/gsd:new-project` → `/gsd:execute-phase N`

For small, obvious changes (typo fix, rename, single-file edit) skip the planning — if you could describe the diff in one sentence, just do it directly.

### Writer/Reviewer pattern

For complex changes, use two sessions:

| Session A (Writer) | Session B (Reviewer) |
|---|---|
| Implement the feature | Review the diff with `review-code` skill in a fresh context |
| Address findings | Report gaps — edge cases, correctness, security |

The reviewer runs in a fresh context so it evaluates the result on its own terms, not biased by how it was produced. Feed findings back to Session A, iterate, re-review.

## Prompting tips

The more precise your instructions, the fewer corrections needed.

| Strategy | Instead of | Try |
|---|---|---|
| **Scope the task** | "add tests for foo.py" | "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." |
| **Reference existing patterns** | "add a calendar widget" | "look at how existing widgets are implemented in `src/components/`. follow the pattern to implement a calendar widget." |
| **Describe the symptom** | "fix the login bug" | "login fails after session timeout. check the auth flow in `src/auth/`, especially token refresh. write a failing test that reproduces it, then fix." |
| **Give a verification command** | "implement X" | "implement X, then run `pytest tests/test_x.py` and fix failures until green." |
| **Reference files with `@`** | "the function in utils" | "read `@src/utils/helpers.py` and explain the `parse_date` function." |

### Let OpenCode interview you

For larger features, start with a brief description and ask OpenCode to interview you using the `question` tool. It will ask about technical implementation, UX, edge cases, and tradeoffs you might not have considered.

```bash
"I want to build [description]. Interview me using the question tool.
Cover implementation, UI/UX, edge cases, and tradeoffs."
```

Once the spec is complete, start a fresh session to implement it.

## Hooks

OpenCode supports stop hooks — scripts that run after every file edit. Configure them in `~/.config/opencode/hooks/`.

### Example: auto-format on write

```bash
# ~/.config/opencode/hooks/stop
ruff format "$1" 2>/dev/null
```

This runs `ruff format` on every file after OpenCode edits it, keeping formatting consistent without manual steps.

### Example: block edits to sensitive paths

```bash
# ~/.config/opencode/hooks/pre-start
case "$1" in
  .env|config/secrets*) exit 1 ;;  # block edits to secret files
esac
```

Install hooks by creating executable scripts in the hooks directory:

```bash
mkdir -p ~/.config/opencode/hooks
chmod +x ~/.config/opencode/hooks/stop
```

## Avoid common failure patterns

| Pattern | Fix |
|---|---|
| **Kitchen sink session** — multiple unrelated tasks in one session. Context full of irrelevant info. | `/clear` between unrelated tasks. |
| **Over-correcting** — Claude does something wrong, you correct it, still wrong, you correct again. Context polluted with failed approaches. | After 2 failed corrections, `/clear` and write a better initial prompt incorporating what you learned. |
| **Trust-then-verify gap** — plausible-looking implementation that misses edge cases. | Always provide a verification check (test, lint, typecheck). Run the `review-code` skill before shipping. |
| **Infinite exploration** — "investigate X" without scope. Reads hundreds of files, fills context. | Scope investigations narrowly or use a subagent so exploration doesn't consume main context. |
```
