# py-opencode-scaffold

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-2088FF?style=for-the-badge&logo=github)](https://codespaces.new/crias-solutions/py-opencode-scaffold)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-F77F00?style=for-the-badge&logo=mozilla)](https://opensource.org/licenses/MPL-2.0)

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-20-339933?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org/)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-8B5CF6?style=flat-square&logo=openai&logoColor=white)](https://opencode.ai/)

---

## What is this?

A ready-to-use Python development environment template for GitHub Codespaces with OpenCode AI assistant pre-configured. Create your own copy, launch a Codespace, and start coding with AI assistance in minutes.

---

## Getting Started

1. Click **"Use this template"** → **"Create a new repository"**
2. Name your project and choose visibility (public/private)
3. Click **"Create repository"**
4. In your new repo, click the **"Open in Codespaces"** badge above
5. Wait for the environment to build (~2 minutes)
6. Open terminal and run:
   ```bash
   opencode
   ```
7. Start coding with AI assistance!

---

## Configuration (Optional)

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
└── requirements.txt         # Python dependencies
```

---

## AGENTS.md Template

This scaffold includes an `AGENTS.md` file—a template for providing context to OpenCode about your project. Edit it to describe your application, coding standards, and project-specific instructions.

See [AGENTS.md](AGENTS.md) for the template.

---

## Saving Your Work

Before deleting your Codespace, always push your changes:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Your code is safely stored on GitHub. You can:
- Clone it locally: `git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git`
- Download as ZIP from GitHub
- Create a new Codespace anytime

---

## License

This project is licensed under the [Mozilla Public License 2.0](LICENSE).
