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
