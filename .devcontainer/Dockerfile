# Base image: Python 3.12 on Debian Bookworm (slim for smaller size)
FROM python:3.12-slim-bookworm

# Avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js LTS (required for OpenCode)
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install OpenCode globally (latest version)
RUN npm install -g @opencode/cli@latest

# Set working directory
WORKDIR /workspaces

# Default command
CMD ["bash"]
