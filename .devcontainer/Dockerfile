# Base image: Node.js LTS on Debian Bookworm (includes npm for OpenCode)
FROM node:20-bookworm-slim

# Avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3 and system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python command
RUN ln -sf /usr/bin/python3 /usr/bin/python \
    && ln -sf /usr/bin/pip3 /usr/bin/pip

# Install OpenCode globally
RUN npm install -g @opencode/cli@latest

# Set working directory
WORKDIR /workspaces

# Default command
CMD ["bash"]
