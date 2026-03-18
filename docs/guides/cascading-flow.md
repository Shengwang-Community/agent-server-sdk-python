---
sidebar_position: 1
title: Cascading Flow (ASR → LLM → TTS)
description: Build a voice agent using Speech-to-Text, a text LLM, and Text-to-Speech.
---

# Cascading Flow (ASR → LLM → TTS)

The cascading flow is the most common pattern for building voice agents. Audio from a user is transcribed by an STT (ASR) vendor, the transcript is sent to an LLM for a response, and the response is rendered as audio by a TTS vendor.

```
User audio → STT → LLM → TTS → Agent audio
```

## Combo 1: Aliyun + MiniMax + Fengming

### Sync

```python
from shengwang_agent import AgentClient, Area
from shengwang_agent.agentkit import Agent
from shengwang_agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

client = AgentClient(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)

agent = (
    Agent(name='assistant', instructions='你是一个友好的客服助手。')
    .with_llm(AliyunLLM(api_key='your-aliyun-key', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='your-minimax-key', voice_id='your-voice-id'))
    .with_stt(FengmingSTT(language='zh-CN'))
)

session = agent.create_session(client, channel='support-room', agent_uid='1', remote_uids=['100'])
agent_id = session.start()
session.say('你好！有什么可以帮助你的？')
# ... agent listens and responds automatically ...
session.stop()
```

### Async

```python
import asyncio
from shengwang_agent import AsyncAgentClient, Area
from shengwang_agent.agentkit import Agent
from shengwang_agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

async def main():
    client = AsyncAgentClient(
        area=Area.CN,
        app_id='your-app-id',
        app_certificate='your-app-certificate',
    )

    agent = (
        Agent(name='assistant', instructions='你是一个友好的客服助手。')
        .with_llm(AliyunLLM(api_key='your-aliyun-key', model='qwen-max'))
        .with_tts(MiniMaxTTS(key='your-minimax-key', voice_id='your-voice-id'))
        .with_stt(FengmingSTT(language='zh-CN'))
    )

    session = agent.create_session(client, channel='support-room', agent_uid='1', remote_uids=['100'])
    agent_id = await session.start()
    await session.say('你好！有什么可以帮助你的？')
    # ... agent listens and responds automatically ...
    await session.stop()

asyncio.run(main())
```

## Combo 2: DeepSeek + Microsoft TTS + Microsoft STT

This combination uses DeepSeek for LLM and Microsoft Azure for speech services:

```python
from shengwang_agent import AgentClient, Area
from shengwang_agent.agentkit import Agent
from shengwang_agent.agentkit.vendors import DeepSeekLLM, MicrosoftTTS, MicrosoftSTT

client = AgentClient(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)

agent = (
    Agent(name='deepseek-agent', instructions='你是一个企业客户的智能助手。')
    .with_llm(DeepSeekLLM(
        api_key='your-deepseek-key',
        model='deepseek-chat',
    ))
    .with_tts(MicrosoftTTS(
        key='your-azure-speech-key',
        region='eastasia',
        voice_name='zh-CN-XiaoxiaoNeural',
        sample_rate=24000,
    ))
    .with_stt(MicrosoftSTT(
        key='your-azure-speech-key',
        region='eastasia',
        language='zh-CN',
    ))
)

session = agent.create_session(client, channel='enterprise-room', agent_uid='1', remote_uids=['100'])
agent_id = session.start()
session.say('你好！我是你的企业助手。')
session.stop()
```

## Customizing the LLM

All LLM vendors support optional parameters for fine-tuning:

```python
from shengwang_agent.agentkit.vendors import AliyunLLM

llm = AliyunLLM(
    api_key='your-aliyun-key',
    model='qwen-max',
    temperature=0.7,
    top_p=0.9,
    max_tokens=1024,
)
```

## Adding a Greeting

The `greeting` parameter on `Agent` makes the agent speak automatically when the session starts:

```python
agent = Agent(
    name='greeter',
    instructions='你是一个智能助手。',
    greeting='你好！有什么可以帮你的？',
)
```

## Next Steps

- To add a visual avatar, see [Avatars](./avatars.md)
- For the full vendor catalog, see [Vendors](../concepts/vendors.md)
