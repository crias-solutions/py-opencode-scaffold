# AGENTS.md

> Context for OpenCode and AI coding assistants.

---

## Project Overview

**Name:** py-opencode-scaffold — Python development environment template for GitHub Codespaces with OpenCode AI pre-configured

**Type:** Python Application / Template Repository

---

## Tech Stack

Python 3.12, pip, pytest/pytest-cov, Ruff (lint/format), mypy (type check)
Key libs: numpy, pandas, scipy, matplotlib, requests

---

## Project Structure

```
py-opencode-scaffold/
├── src/                  # Source code
├── tests/                # Test files
├── .devcontainer/        # Codespaces config
├── AGENTS.md             # This file
├── README.md
├── requirements.txt
└── WRITING.md            # Documentation standards
```

---

## Commands

### Dependencies

```bash
pip install -r requirements.txt       # Install
pip install <package> && pip freeze > requirements.txt  # Add dependency
```

### Tests

```bash
pytest                                 # All tests
pytest tests/test_file.py::test_name   # Single test
pytest --cov=src --cov-report=term-missing  # With coverage
```

### Code Quality

```bash
ruff check .    # Lint
ruff format .   # Format
mypy src/       # Type check
```

### AI Workflows

**spec-kit** (spec-first): `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`, `/speckit.clarify`, `/speckit.analyze`
**GSD** (multi-step tasks): `/gsd:new-project`, `/gsd:plan-phase N`, `/gsd:execute-phase N`, `/gsd:verify-work N`, `/gsd:quick`

Use spec-kit for defining features/plans, GSD for complex multi-step execution, direct prompts for quick questions.

---

## Coding Standards

### Style

- PEP 8, max 88 chars/line
- Type hints on all functions
- Google-style docstrings for public functions/classes
- Prefer f-strings over .format() or % formatting

### Naming

| Type | Convention | Example |
|------|------------|---------|
| Variables/Functions | snake_case | `get_user()` |
| Classes | PascalCase | `UserManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES` |
| Private | `_prefix` | `_internal_method()` |
| Type aliases | PascalCase | `UserId = str` |

### Imports

Three groups separated by blank lines: stdlib → third-party → local.
Use absolute imports, one per line.

```python
import os
import requests
from src.utils import helper
```

### Types

- Use `typing` module for complex types (`List`, `Dict`, `Optional`)
- Prefer `collections.abc` (`Sequence`, `Mapping`) when read-only
- Use `TypeVar` for generics
- Never use bare `except`

### Error Handling

- Raise specific exceptions (`ValueError`, `TypeError`, `RuntimeError`)
- Custom exceptions inherit from `Exception`
- Use context managers (`with`) for resource cleanup
- Log before raising; never swallow exceptions silently
- Use `raise ... from ...` for exception chaining

---

## Testing

- Files: `test_<module>.py`
- Functions: `test_<function>_<scenario>()` (e.g., `test_login_fails_with_invalid_password`)
- Use `pytest.fixture` for shared setup, `parametrize` for multiple cases
- Mock external services with `unittest.mock` or `pytest-mock`

---

## AI Guidelines

**Do:** Type hints, docstrings, unit tests, follow patterns, reference WRITING.md for docs
**Don't:** Remove tests without reason, change style mid-project, add unjustified deps, leave commented code, hardcode secrets

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Anthropic API key | No |
| `OPENAI_API_KEY` | OpenAI API key | No |

---

## Notes

- Template repo — update name/description when creating new project
- WRITING.md enforces Diátaxis, Golden Circle, Rule of Three for docs
- No Cursor rules (.cursor/rules/) or Copilot instructions (.github/copilot-instructions.md)
