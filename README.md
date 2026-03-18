# Agent Server SDK for Python

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FShengwang-Community%2Fagent-server-sdk-python)
[![pypi](https://img.shields.io/pypi/v/agent-server-sdk)](https://pypi.python.org/pypi/agent-server-sdk)

The Conversational AI SDK provides convenient access to the Conversational AI APIs,
enabling you to build voice-powered AI agents with support for cascading flows (ASR -> LLM -> TTS).


## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install agent-server-sdk
```

## Quick Start

Use the **builder pattern** with `Agent` and `AgentSession`. The SDK auto-generates all required tokens:

```python
from shengwang_agent import AgentClient, Area
from shengwang_agent.agentkit import Agent, expires_in_hours
from shengwang_agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

client = AgentClient(
    area=Area.CN,
    app_id="your-app-id",
    app_certificate="your-app-certificate",
)

agent = (
    Agent(name="support-assistant", instructions="你是一个智能语音助手。")
    # Create Agent: STT → LLM → TTS → (optional) Avatar
    .with_stt(FengmingSTT(language="zh-CN"))
    .with_llm(AliyunLLM(api_key="your-aliyun-key", model="qwen-max"))
    .with_tts(MiniMaxTTS(key="your-minimax-key", voice_id="your-voice-id"))
    # .with_avatar(SensetimeAvatar(...))  # optional
)

session = agent.create_session(
    client,
    channel="support-room-123",
    agent_uid="1",
    remote_uids=["100"],
    expires_in=expires_in_hours(12),  # optional — default is 24 h
)

# start() returns a session ID unique to this agent session
agent_session_id = session.start()

# In production, stop is typically called when your client signals the session has ended.
# Your server receives that request and calls session.stop().
session.stop()
```

For async usage, use `AsyncAgentClient` and `await session.start()`, etc. See [Quick Start](docs/getting-started/quick-start.md).

### Session lifecycle

`start()` joins the agent to the channel and returns a **session ID** — a unique identifier for this agent session. The session stays active until `stop()` is called.

There are two ways to stop a session depending on how your server is structured:

**Option 1 — Hold the session in memory:**

```python
# start-session handler
agent_session_id = session.start()  # unique ID for this session
# stop-session handler (same process, session still in scope)
session.stop()
```

**Option 2 — Store the session ID and stop by ID (stateless servers):**

```python
# start-session handler: return session ID to your client app
agent_session_id = session.start()
# ... return agent_session_id to client ...

# stop-session handler: client sends back agent_session_id
client = AgentClient(area=Area.CN, app_id="...", app_certificate="...")
client.stop_agent(agent_session_id)
```

### Manual tokens (for debugging)

Generate tokens yourself and pass them in — useful when inspecting or reusing tokens:

```python
from shengwang_agent import AgentClient, Area
from shengwang_agent.agentkit.token import generate_convo_ai_token, expires_in_hours

APP_ID = "your-app-id"
APP_CERT = "your-app-certificate"
CHANNEL = "support-room-123"
AGENT_UID = "1"

# Auth header token — used by the SDK to authenticate REST API calls
auth_token = generate_convo_ai_token(
    app_id=APP_ID, app_certificate=APP_CERT,
    channel_name=CHANNEL, account=AGENT_UID,
    token_expire=expires_in_hours(12),
)

# Channel join token — embedded in the start request so the agent can join the channel
join_token = generate_convo_ai_token(
    app_id=APP_ID, app_certificate=APP_CERT,
    channel_name=CHANNEL, account=AGENT_UID,
    token_expire=expires_in_hours(12),
)

client = AgentClient(
    area=Area.CN,
    app_id=APP_ID,
    app_certificate=APP_CERT,
    auth_token=auth_token,  # SDK sets Authorization: agora token=<auth_token>
)

session = agent.create_session(
    client, channel=CHANNEL, agent_uid=AGENT_UID, remote_uids=["100"],
    token=join_token,  # channel join token
)
```

## Documentation

API reference documentation is available [here](docs/index.md).

## Reference

A full reference for this library is available [here](https://github.com/Shengwang-Community/agent-server-sdk-python/blob/HEAD/./reference.md).


## Usage

Instantiate and use the client with the following:

```python
from shengwang_agent import AgentClient, MicrosoftTtsParams, Tts_Microsoft
from shengwang_agent.agents import (
    StartAgentsRequestProperties,
    StartAgentsRequestPropertiesAsr,
    StartAgentsRequestPropertiesLlm,
)

client = AgentClient(
    authorization="YOUR_AUTHORIZATION",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.agents.start(
    appid="appid",
    name="unique_name",
    properties=StartAgentsRequestProperties(
        channel="channel_name",
        token="token",
        agent_rtc_uid="1001",
        remote_rtc_uids=["1002"],
        idle_timeout=120,
        asr=StartAgentsRequestPropertiesAsr(
            language="zh-CN",
        ),
        tts=Tts_Microsoft(
            params=MicrosoftTtsParams(
                key="key",
                region="eastasia",
                voice_name="zh-CN-XiaoxiaoNeural",
            ),
        ),
        llm=StartAgentsRequestPropertiesLlm(
            url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
            api_key="<your_llm_key>",
            system_messages=[
                {"role": "system", "content": "你是一个智能助手。"}
            ],
            params={"model": "qwen-max"},
            max_history=32,
            greeting_message="你好，有什么可以帮助你的？",
            failure_message="请稍等一下。",
        ),
    ),
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from shengwang_agent import AsyncAgentClient, MicrosoftTtsParams, Tts_Microsoft
from shengwang_agent.agents import (
    StartAgentsRequestProperties,
    StartAgentsRequestPropertiesAsr,
    StartAgentsRequestPropertiesLlm,
)

client = AsyncAgentClient(
    authorization="YOUR_AUTHORIZATION",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)


async def main() -> None:
    await client.agents.start(
        appid="appid",
        name="unique_name",
        properties=StartAgentsRequestProperties(
            channel="channel_name",
            token="token",
            agent_rtc_uid="1001",
            remote_rtc_uids=["1002"],
            idle_timeout=120,
            asr=StartAgentsRequestPropertiesAsr(
                language="zh-CN",
            ),
            tts=Tts_Microsoft(
                params=MicrosoftTtsParams(
                    key="key",
                    region="eastasia",
                    voice_name="zh-CN-XiaoxiaoNeural",
                ),
            ),
            llm=StartAgentsRequestPropertiesLlm(
                url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
                api_key="<your_llm_key>",
                system_messages=[
                    {"role": "system", "content": "你是一个智能助手。"}
                ],
                params={"model": "qwen-max"},
                max_history=32,
                greeting_message="你好，有什么可以帮助你的？",
                failure_message="请稍等一下。",
            ),
        ),
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from shengwang_agent.core.api_error import ApiError

try:
    client.agents.start(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from shengwang_agent import AgentClient

client = AgentClient(
    authorization="YOUR_AUTHORIZATION",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
response = client.agents.list(
    appid="appid",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.agents.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from shengwang_agent import AgentClient

client = AgentClient(
    ...,
)
response = client.agents.with_raw_response.start(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.agents.list(...)
print(pager.response)  # access the typed response for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.agents.start(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from shengwang_agent import AgentClient

client = AgentClient(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.agents.start(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from shengwang_agent import AgentClient

client = AgentClient(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
