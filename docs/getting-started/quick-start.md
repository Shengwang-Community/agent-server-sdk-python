---
sidebar_position: 3
title: Quick Start
description: Build and run your first Conversational AI agent in Python.
---

# Quick Start

This guide walks you through building a voice agent using the cascading flow (ASR → LLM → TTS) with both sync and async clients.

## Sync Example

This complete script creates an agent with Aliyun for the LLM, MiniMax for TTS, and Fengming for STT:

```python
from agent import Agora, Area
from agent.agentkit import Agent
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

# 1. Create a client with app credentials
client = Agora(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)

# 2. Build an agent with vendor configuration
agent = (
    Agent(name='support-assistant', instructions='你是一个智能语音助手。')
    .with_llm(AliyunLLM(api_key='your-aliyun-key', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='your-minimax-key', voice_id='your-voice-id'))
    .with_stt(FengmingSTT(language='zh-CN'))
)

# 3. Create and start a session
session = agent.create_session(
    client,
    channel='support-room-123',
    agent_uid='1',
    remote_uids=['100'],
)
agent_id = session.start()
print(f'Agent started with ID: {agent_id}')

# 4. Interact with the agent
session.say('你好！有什么可以帮助你的？')

# 5. Stop the session when done
session.stop()
print('Agent stopped.')
```

## Async Example

For async applications, use `AsyncAgora` for the client. All session methods become coroutines that require `await`:

```python
import asyncio
from agent import AsyncAgora, Area
from agent.agentkit import Agent
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

async def main():
    # 1. Create an async client
    client = AsyncAgora(
        area=Area.CN,
        app_id='your-app-id',
        app_certificate='your-app-certificate',
    )

    # 2. Build an agent (same as sync — Agent is client-agnostic)
    agent = (
        Agent(name='support-assistant', instructions='你是一个智能语音助手。')
        .with_llm(AliyunLLM(api_key='your-aliyun-key', model='qwen-max'))
        .with_tts(MiniMaxTTS(key='your-minimax-key', voice_id='your-voice-id'))
        .with_stt(FengmingSTT(language='zh-CN'))
    )

    # 3. Create a session — works with both sync and async clients
    session = agent.create_session(
        client,
        channel='support-room-123',
        agent_uid='1',
        remote_uids=['100'],
    )

    # 4. All session methods are coroutines — use await
    agent_id = await session.start()
    print(f'Agent started with ID: {agent_id}')

    await session.say('你好！有什么可以帮助你的？')
    await session.stop()
    print('Agent stopped.')

asyncio.run(main())
```

## What Happens Under the Hood

1. The `Agent` builder collects your vendor configuration into a properties object
2. `session.start()` generates an RTC token (using the client's `app_id` and `app_certificate`), then calls the API to start the agent
3. The agent connects to the specified channel and begins listening for audio from the remote UIDs
4. `session.say()` sends text to be spoken by the agent's TTS
5. `session.stop()` gracefully shuts down the agent

## Next Steps

- Learn how the [Agent builder](../concepts/agent.md) works
- Understand the [AgentSession lifecycle](../concepts/session.md)
- Explore the full [vendor catalog](../concepts/vendors.md)
