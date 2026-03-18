---
sidebar_position: 10
title: Low-Level API
description: Direct client.agents.start() usage without the builder pattern.
---

# Low-Level API

For full control over request payloads you can call the generated clients directly and pass raw types such as `StartAgentsRequestProperties`. Use this when you need vendor or options not exposed by the agentkit, or when integrating with generated types from the API spec.

## Cascading flow (ASR → LLM → TTS)

```python
from shengwang_agent import AgentClient, Area
from shengwang_agent.agents import (
    StartAgentsRequestProperties,
    StartAgentsRequestPropertiesAsr,
    StartAgentsRequestPropertiesLlm,
)

client = AgentClient(
    area=Area.CN,
    app_id="YOUR_APP_ID",
    app_certificate="YOUR_APP_CERTIFICATE",
)
client.agents.start(
    client.app_id,
    name="unique_name",
    properties=StartAgentsRequestProperties(
        channel="channel_name",
        token="token",
        agent_rtc_uid="1001",
        remote_rtc_uids=["1002"],
        idle_timeout=120,
        asr=StartAgentsRequestPropertiesAsr(
            language="zh-CN",
            vendor="fengming",
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

## Async (low-level)

```python
import asyncio
from shengwang_agent import Area, AsyncAgentClient
from shengwang_agent.agents import (
    StartAgentsRequestProperties,
    StartAgentsRequestPropertiesAsr,
    StartAgentsRequestPropertiesLlm,
)

client = AsyncAgentClient(
    area=Area.CN,
    app_id="YOUR_APP_ID",
    app_certificate="YOUR_APP_CERTIFICATE",
)

async def main() -> None:
    await client.agents.start(
        client.app_id,
        name="unique_name",
        properties=StartAgentsRequestProperties(
            channel="channel_name",
            token="token",
            agent_rtc_uid="1001",
            remote_rtc_uids=["1002"],
            idle_timeout=120,
            asr=StartAgentsRequestPropertiesAsr(
                language="zh-CN",
                vendor="fengming",
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

For more on the agentkit-based flow, see [Cascading Flow](./cascading-flow.md).
