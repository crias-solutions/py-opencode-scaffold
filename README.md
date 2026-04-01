# py-opencode-scaffold

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-2088FF?style=for-the-badge&logo=github)](https://codespaces.new/crias-solutions/py-opencode-scaffold)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-F77F00?style=for-the-badge&logo=mozilla)](https://opensource.org/licenses/MPL-2.0)

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-20-339933?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org/)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-8B5CF6?style=flat-square&logo=openai&logoColor=white)](https://opencode.ai/)

---

A ready-to-use Python development environment template for GitHub Codespaces with OpenCode AI assistant pre-configured. Create your own copy, launch a Codespace, and start coding with AI assistance in minutes.

---

## Why

### Problem

Developers spend significant time setting up local development environments. Installing tools, configuring extensions, and ensuring consistency across machines slows down productivity.

### Motivation

This template eliminates manual setup. It provides a pre-configured Codespace with Python, Node.js, and OpenCode ready to use immediately after launch.

### Intended Impact

Reduce environment setup from hours to minutes. Enable developers to focus on writing code rather than configuring tools.

---

## How

### Architecture

The project uses GitHub Codespaces with a DevContainer configuration. This provides a consistent, containerized development environment that runs in the cloud.

### Technical Approach

1. **DevContainer** – Defines the development environment with all required tools and extensions
2. **Template Repository** – Users create their own copy from this template
3. **Environment Variables** – API keys are configured via GitHub Codespaces secrets

### Key Components

- Python 3.12 for runtime
- Node.js 20 for CLI tools
- OpenCode CLI for AI assistance
- GSD (Get Shit Done) for structured AI workflows
- spec-kit for specification-first development
- VS Code extensions pre-configured

---

## What

### Core Features

1. **One-click Codespace setup** – Launch a fully configured environment from the template
2. **Pre-configured AI assistance** – OpenCode ready to use with `/help` command
3. **Structured AI workflows** – GSD provides plan/execute/verify commands out of the box
4. **Specification-first development** – spec-kit for constitution, specs, plans, and tasks
5. **Customizable context** – AGENTS.md template for project-specific instructions

### What's Included

- DevContainer configuration
- AGENTS.md template for OpenCode context
- Python dependencies (requirements.txt)
- Git configuration (.gitattributes, .gitignore)

---

## Installation

1. Click **"Use this template"** → **"Create a new repository"**
2. Name your project and choose visibility (public/private)
3. Click **"Create repository"**
4. In your new repo, click the **"Open in Codespaces"** badge
5. Wait for the environment to build (~2 minutes)
6. Open terminal and run:
   ```bash
   opencode
   ```
7. Start coding with AI assistance

---

## Configuration

### API Keys Setup

OpenCode requires an API key from a supported provider.

#### Option 1: Anthropic (Claude)

1. Get your API key from [console.anthropic.com](https://console.anthropic.com/)
2. In GitHub, go to **Settings** → **Codespaces** → **Secrets**
3. Click **New secret**:
   - Name: `ANTHROPIC_API_KEY`
   - Value: Your API key
4. Rebuild your Codespace

#### Option 2: OpenAI (GPT)

1. Get your API key from [platform.openai.com](https://platform.openai.com/)
2. In GitHub, go to **Settings** → **Codespaces** → **Secrets**
3. Click **New secret**:
   - Name: `OPENAI_API_KEY`
   - Value: Your API key
4. Rebuild your Codespace

---

## Models

OpenCode supports multiple AI providers. Choose based on your needs:

| Model | Provider | Best For |
|-------|----------|----------|
| Claude 3.5 Sonnet | Anthropic | General coding, debugging, explanations |
| Claude 3 Opus | Anthropic | Complex reasoning, large codebases |
| GPT-4o | OpenAI | Fast responses, broad knowledge |
| GPT-4 Turbo | OpenAI | Cost-effective coding tasks |

### Selecting a Model

OpenCode automatically uses the model associated with your configured API key. Set either `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` in your Codespaces secrets.

---

## Usage

### Launch OpenCode

```bash
opencode
```

### Common Commands

| Command | Description |
|---------|-------------|
| `opencode` | Launch AI assistant |
| `/help` | Show available commands |
| `/clear` | Clear conversation |
| `/quit` | Exit OpenCode |

### Typical Workflow

1. Run `opencode` in terminal
2. Describe what you want to build
3. AI assists with coding, debugging, and explaining

---

## Project Structure

```
py-opencode-scaffold/
├── .devcontainer/
│   └── devcontainer.json    # Codespaces configuration
├── .gitattributes           # Git file handling rules
├── .gitignore               # Ignored files and folders
├── AGENTS.md                # AI context template
├── LICENSE                  # MPL 2.0
├── README.md                # This file
├── requirements.txt         # Python dependencies
└── WRITING.md               # Documentation standards
```

---

## AI Context Files

This template includes two files that help OpenCode understand your project:

### AGENTS.md

**Purpose**: Provides context about your project to OpenCode.

**When to use**:
- When you create a new project from this template
- When your project evolves (new tech stack, conventions, dependencies)
- When you need OpenCode to follow specific coding standards

**How to use**: Edit [AGENTS.md](AGENTS.md) to describe:
- Project name and description
- Tech stack and dependencies
- Coding standards and conventions
- Common tasks and commands

### WRITING.md

**Purpose**: Defines documentation standards for this project.

**When to use**:
- When creating or updating README.md files
- When writing any project documentation
- When ensuring consistency across documentation

**How to use**: OpenCode automatically reads WRITING.md when modifying documentation. It enforces:
- Golden Circle structure (Why → How → What)
- Rule of Three for content organization
- KISS principle for clarity

---

## License

This project is licensed under the Mozilla Public License 2.0.  
SPDX-License-Identifier: MPL-2.0

See the [LICENSE](LICENSE) file for full details.

---

## Acknowledgments

This template includes the following third-party tools:

- **[GSD (Get Shit Done)](https://github.com/gsd-build/get-shit-done)** — Developed by [TACHES](https://github.com/gsd-build/get-shit-done) under the MIT License. Copyright (c) 2025 Lex Christopherson. See the [GSD LICENSE](https://github.com/gsd-build/get-shit-done/blob/main/LICENSE) for full details.

- **[spec-kit](https://github.com/github/spec-kit)** — Developed by [GitHub](https://github.com/github/spec-kit) under the MIT License. Copyright (c) GitHub, Inc. See the [spec-kit LICENSE](https://github.com/github/spec-kit/blob/main/LICENSE) for full details.
