---
title: "Agentic Dev Sandbox"
collection: projects
permalink: /projects/agentic-dev-sandbox/
order: 1
excerpt: "A containerized LLM development environment with strict network isolation, hardened per-project security boundaries, and a human-in-the-loop Git workflow via local Gitea mirrors."
stack:
  - Docker
  - Bash
  - Gitea
  - CI
  - LLM APIs
---

## Overview

A secure AI development environment for running agentic coding tools (Claude Code, Codex, etc.) without giving them access to host credentials or production repositories.

## Key features

- **Containerized per-project isolation**: each project runs in its own Docker container with hardened network and filesystem boundaries.
- **Local Gitea mirror**: agents push/pull to a local Gitea instance rather than directly to GitHub/GitLab, keeping production repos fully isolated and enabling human-in-the-loop review.
- **External CI enforcement**: remediates common agentic failure modes (e.g., hallucinated test results) by requiring tests to pass on an external CI runner before changes are merged upstream.

## Stack

Docker, Bash, Gitea, CI pipelines, LLM APIs.

## Links

- [GitHub repository](https://github.com/joaopn/agentic-dev-sandbox)
