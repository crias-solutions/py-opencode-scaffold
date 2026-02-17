# Base image: Python 3.12 on Debian Bookworm (slim for smaller size)
FROM python:3.12-slim-bookworm

# Avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies including gnupg (required for NodeSource)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    build-essential \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js LTS (using NodeSource with proper setup)
RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install OpenCode globally (latest version)
RUN npm install -g @opencode/cli@latest

# Set working directory
WORKDIR /workspaces

# Default command
CMD ["bash"]
