# AGENTS.md

> Context for OpenCode and AI coding assistants.

## Critical Facts (Would Likely Miss Without Help)

- **Template repository**: When creating a new project from this template, you MUST update the project name and description in this file.
- **No application code**: The `src/` directory is intentionally empty - this is where you add your code.
- **Environment variables**: OpenCode requires API keys set via GitHub Codespaces secrets (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`), not in the repository.
- **Test naming**: Tests must follow `test_<module>.py` naming convention for pytest discovery.

## Essential Commands

### Dependency Management
```bash
# After editing requirements.txt
pip install <package> && pip freeze > requirements.txt
```

### Testing
```bash
# All tests
pytest

# Single test function
pytest tests/test_file.py::test_name

# With coverage
pytest --cov=src --cov-report=term-missing
```

### Code Quality
```bash
# Lint
ruff check .

# Format
ruff format .

# Type check
mypy src/
```

### AI Workflows (pre-installed)
```bash
# Specification-first development (spec-kit)
/speckit.specify    # Start feature specification
/speckit.plan       # Create implementation plan
/speckit.tasks      # Break plan into tasks
/speckit.implement  # Implement tasks

# Multi-step execution (GSD)
/gsd:new-project    # Start GSD workflow
/gsd:execute-phase N # Execute phase N
```

## Project Structure
```
py-opencode-scaffold/
├── src/                  # ← Add your application code here
├── tests/                # ← Test files (must be test_<module>.py)
├── .devcontainer/        # ← Codespaces configuration (generally don't modify)
├── AGENTS.md             # ← THIS FILE (update for your project context)
├── README.md
├── requirements.txt      # ← Python dependencies (keep updated)
└── WRITING.md            # ← Documentation standards
```

## Agent-Specific Guidelines

1. **Always update this file** when creating a new project from this template - it's how OpenCode learns about your specific project.
2. **Dependency changes**: Whenever you modify `requirements.txt`, run the pip install + freeze command to keep it synchronized.
3. **File locations matter**:
   - Source code → `src/` directory
   - Test files → `tests/` directory (must follow `test_<module>.py` naming)
   - Configuration → `.devcontainer/` (generally avoid modifying unless you understand DevContainers)
4. **No pre-existing logic**: This is a clean starting point - there is no business logic to preserve or reverse-engineer.
5. **OpenCode reads this file automatically** - keep it accurate and up-to-date for optimal AI assistance. Outdated or incorrect context will lead to poor AI performance.