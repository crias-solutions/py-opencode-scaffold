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
- **Testing:** pytest
- **Linting:** Ruff
- **Formatting:** Ruff / Black

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

## Coding Standards

### Style

- Follow PEP 8
- Use type hints for all functions
- Maximum line length: 88 characters
- Use docstrings for public functions and classes

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Variables | snake_case | `user_name` |
| Functions | snake_case | `get_user()` |
| Classes | PascalCase | `UserManager` |
| Constants | UPPER_SNAKE | `MAX_RETRIES` |
| Private | _prefix | `_internal_method()` |

### Imports

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

---

## Testing

### Run Tests

```bash
pytest
```

### With Coverage

```bash
pytest --cov=src --cov-report=term-missing
```

### Test Naming

- Files: `test_<module>.py`
- Functions: `test_<function>_<scenario>()`

---

## Common Tasks

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add New Dependency

```bash
pip install <package>
pip freeze > requirements.txt
```

### Run Linter

```bash
ruff check .
```

### Format Code

```bash
ruff format .
```

---

## AI Assistant Guidelines

### Do

- Write clean, readable code
- Include type hints
- Add docstrings to public functions
- Write unit tests for new features
- Follow existing patterns in the codebase

### Don't

- Remove existing tests without explanation
- Change coding style mid-project
- Add dependencies without justification
- Leave commented-out code

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Anthropic API key | No |
| `OPENAI_API_KEY` | OpenAI API key | No |

---

## Notes

[Add project-specific notes, gotchas, or context here]
