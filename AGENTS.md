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
```
