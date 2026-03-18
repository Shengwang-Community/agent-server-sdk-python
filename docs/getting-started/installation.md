---
sidebar_position: 1
title: Installation
description: Install the Conversational AI Python SDK.
---

# Installation

## Prerequisites

- Python >= 3.8

## Install with pip

```sh
pip install agent-server-sdk
```

## Install with Poetry

```sh
poetry add agent-server-sdk
```

## Dependencies

The following packages are installed automatically:

| Package | Purpose |
|---|---|
| `httpx` (>= 0.21.2) | HTTP client for sync and async requests |
| `pydantic` (>= 1.9.2) | Data validation for vendor configuration and API types |
| `typing_extensions` (>= 4.0.0) | Backported type hints for Python 3.8+ |

## Sync vs. Async

The SDK supports both synchronous and asynchronous usage:

- **Synchronous** — import `AgentClient` from `agent` and use blocking method calls
- **Asynchronous** — import `AsyncAgentClient` and `AsyncAgentSession` from `agent` and use `await` with all API calls

```python
# Sync
from agent import AgentClient, Area

# Async
from agent import AsyncAgentClient, AsyncAgentSession, Area
```

Both clients share the same constructor parameters and capabilities. See [Authentication](./authentication.md) for setup details.
