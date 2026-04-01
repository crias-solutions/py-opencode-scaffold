# AGENTS.md

> This file provides context to OpenCode and other AI coding assistants about your project.

---

## Project Overview

**Name:** [Your Project Name]

**Description:** [One-sentence description of what this project does]

**Type:** Python Application

---

## Tech Stack

- **Language:** Python 3.12
- **Package Manager:** pip
- **Testing:** pytest, pytest-cov
- **Linting:** Ruff
- **Formatting:** Ruff / Black
- **Type Checking:** mypy

---

## Project Structure

```
project-root/
├── src/                  # Source code
│   ├── __init__.py
│   └── main.py
├── tests/                # Test files
│   └── test_main.py
├── .devcontainer/        # Codespaces config
├── AGENTS.md             # This file
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Commands

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add New Dependency

```bash
pip install <package>
pip freeze > requirements.txt
```

### Run All Tests

```bash
pytest
```

### Run a Single Test

```bash
pytest tests/test_file.py::test_function_name
```

### Run Tests with Coverage

```bash
pytest --cov=src --cov-report=term-missing
```

### Run Linter

```bash
ruff check .
```

### Format Code

```bash
ruff format .
```

### Type Check

```bash
mypy src/
```

---

## GSD (Get Shit Done)

Pre-installed context engineering system for OpenCode. Provides structured workflows for complex development tasks.

### When to Use Each Approach

| Use spec-kit When | Use GSD When | Use Direct Prompts When |
|-------------------|--------------|------------------------|
| Defining new features or requirements | Planning complex multi-step tasks | Answering quick questions |
| Creating technical implementation plans | Breaking down large tasks into subtasks | Fixing small bugs |
| Generating task lists from specifications | Executing plans with parallel waves | Explaining existing code |
| Ensuring spec-to-code traceability | Verifying completed work | Simple refactoring |

### spec-kit Commands

| Command | Purpose |
|---------|---------|
| `/speckit.constitution` | Create project governing principles |
| `/speckit.specify` | Define requirements and user stories |
| `/speckit.plan` | Create technical implementation plans |
| `/speckit.tasks` | Generate actionable task lists |
| `/speckit.implement` | Execute all tasks to build the feature |
| `/speckit.clarify` | Clarify underspecified areas |
| `/speckit.analyze` | Cross-artifact consistency analysis |
| `/speckit.checklist` | Generate custom quality checklists |

### spec-kit Usage Notes

- spec-kit provides structured specification-first development
- Use `specify init . --ai opencode` to bootstrap in existing projects
- spec-kit is developed by [GitHub](https://github.com/github/spec-kit) under the MIT License

### Available Commands

| Command | Purpose |
|---------|---------|
| `/gsd-help` | Show all available GSD commands |
| `/gsd:new-project` | Initialize project (research → requirements → roadmap) |
| `/gsd:discuss-phase N` | Capture implementation decisions |
| `/gsd:plan-phase N` | Research, plan, and verify a task |
| `/gsd:execute-phase N` | Execute plans in parallel waves |
| `/gsd:verify-work N` | User acceptance testing |
| `/gsd:quick` | Fast ad-hoc tasks |
| `/gsd:next` | Auto-detect and run next step |

### Usage Notes

- GSD uses specialized subagents (planner, executor, verifier) for complex workflows
- Use `inherit` model profile — follows OpenCode's configured model selection
- GSD is developed by [TACHES](https://github.com/gsd-build/get-shit-done) under the MIT License

---

## Coding Standards

### Style

- Follow PEP 8
- Use type hints for all functions and method signatures
- Maximum line length: 88 characters
- Use docstrings for public functions and classes (Google style)
- Prefer f-strings over .format() or % formatting

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Variables | snake_case | `user_name` |
| Functions | snake_case | `get_user()` |
| Classes | PascalCase | `UserManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES` |
| Private | _prefix | `_internal_method()` |
| Type aliases | PascalCase | `UserId = str` |

### Imports

Order imports in three groups, separated by blank lines:

```python
# Standard library
import os
import sys

# Third-party
import requests
import pandas as pd

# Local
from src.utils import helper
```

- Use absolute imports over relative imports
- One import per line (no `from x import a, b`)

### Types

- Use `typing` module for complex types (`List`, `Dict`, `Optional`, `Union`)
- Prefer `collections.abc` types (`Sequence`, `Mapping`) when only reading
- Use `TypeVar` for generic functions
- Never use bare `except` — always specify exception type

### Error Handling

- Raise specific exceptions (`ValueError`, `TypeError`, `RuntimeError`)
- Create custom exceptions inheriting from `Exception` for domain errors
- Use context managers (`with`) for resource cleanup
- Log errors before raising; never silently swallow exceptions
- Use `raise ... from ...` for exception chaining

---

## Testing

### Naming

- Files: `test_<module>.py`
- Functions: `test_<function>_<scenario>()`

### Structure

- Use `pytest.fixture` for shared setup
- Use `parametrize` for multiple input cases
- Mock external services with `unittest.mock` or `pytest-mock`
- Test names should describe the scenario, e.g. `test_login_fails_with_invalid_password`

---

## AI Assistant Guidelines

### Do

- Write clean, readable code
- Include type hints on all functions
- Add docstrings to public functions and classes
- Write unit tests for new features
- Follow existing patterns in the codebase
- Reference WRITING.md when creating or updating documentation

### Don't

- Remove existing tests without explanation
- Change coding style mid-project
- Add dependencies without justification
- Leave commented-out code
- Hardcode secrets, API keys, or credentials

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Anthropic API key | No |
| `OPENAI_API_KEY` | OpenAI API key | No |

---

## Notes

[Add project-specific notes, gotchas, or context here]
