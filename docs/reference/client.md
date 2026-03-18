---
sidebar_position: 1
title: AgentClient / AsyncAgentClient
description: Constructor options and public methods for the AgentClient Python client.
---

# AgentClient / AsyncAgentClient

## `AgentClient` Constructor

```python
from agent import AgentClient, Area

client = AgentClient(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `area` | `Area` | Yes | — | Region for API routing (`Area.US`, `Area.EU`, `Area.AP`, `Area.CN`) |
| `app_id` | `str` | Yes* | — | App ID (app-credentials mode) |
| `app_certificate` | `str` | Yes* | — | App Certificate (app-credentials mode) |
| `username` | `str` | Yes* | — | Customer ID (Basic Auth mode) |
| `password` | `str` | Yes* | — | Customer Secret (Basic Auth mode) |
| `auth_token` | `str` | No | — | Pre-built `agora token=<value>` |
| `headers` | `Dict[str, str]` | No | `None` | Additional headers sent with every request |
| `timeout` | `float` | No | `60` | Request timeout in seconds |
| `follow_redirects` | `bool` | No | `True` | Whether to follow HTTP redirects |
| `httpx_client` | `httpx.Client` | No | `None` | Custom httpx client instance |

*Provide either `app_id` + `app_certificate`, or `username` + `password`.

## `AsyncAgentClient` Constructor

Identical to `AgentClient` except:

| Parameter | Difference |
|---|---|
| `httpx_client` | Accepts `httpx.AsyncClient` instead of `httpx.Client` |

```python
from agent import AsyncAgentClient, Area

client = AsyncAgentClient(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)
```

## Public Methods

### `next_region()`

Cycle to the next region prefix in the pool. Call this when a request fails to try a different endpoint.

```python
client.next_region()
```

- **Returns:** `None`
- **Sync on both `AgentClient` and `AsyncAgentClient`**

### `select_best_domain()`

Trigger DNS-based domain selection to find the fastest-responding domain suffix.

```python
# Sync (AgentClient)
client.select_best_domain()

# Async (AsyncAgentClient) — MUST use await
await client.select_best_domain()
```

- **Returns:** `None`
- **`AgentClient`:** regular method
- **`AsyncAgentClient`:** coroutine — requires `await`
- Results are cached for 30 seconds

### `get_current_url()`

Get the current base URL being used for requests.

```python
url = client.get_current_url()
# "https://api-us-west-1.agora.io/api/conversational-ai-agent"
```

- **Returns:** `str`
- **Sync on both `AgentClient` and `AsyncAgentClient`**

### `pool` (property)

Access the underlying `Pool` object for advanced domain management.

```python
pool = client.pool
pool.get_area()  # Area.US
```

- **Returns:** `Pool`

## Sub-Clients (Fern-Generated)

Both `AgentClient` and `AsyncAgentClient` expose Fern-generated sub-clients as properties:

| Property | Type (sync / async) | Description |
|---|---|---|
| `client.agents` | `AgentsClient` / `AsyncAgentsClient` | Start, stop, list, update agents |
| `client.telephony` | `TelephonyClient` / `AsyncTelephonyClient` | Telephony operations |
| `client.phone_numbers` | `PhoneNumbersClient` / `AsyncPhoneNumbersClient` | Phone number management |

These are lazily initialized on first access. For most use cases, prefer the [AgentSession](./session.md) API instead of calling `client.agents` directly.
