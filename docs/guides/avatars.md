---
sidebar_position: 3
title: Avatar Integration
description: Add a digital avatar (Sensetime) to your Conversational AI agent.
---

# Avatar Integration

You can attach a digital avatar to your voice agent so that users see a visual representation of the AI speaking.

| Provider | Class | Description |
|---|---|---|
| Sensetime | `SensetimeAvatar` | Sensetime digital avatar |

## Sample Rate Constraint

Each avatar vendor requires a specific TTS sample rate. The SDK validates this when you call `with_avatar()` — if the TTS sample rate does not match, a `ValueError` is raised immediately:

```
ValueError: Avatar requires TTS sample rate of 24000 Hz, but TTS is configured with 16000 Hz. Please update your TTS sample_rate to 24000.
```

This validation happens at build time (when chaining methods), not at runtime when the session starts.

Additionally, if the TTS `sample_rate` is not explicitly set (returns `None`), the SDK issues a warning.

## Sensetime Avatar

```python
from agent import AgentClient, Area
from agent.agentkit import Agent
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT, SensetimeAvatar

client = AgentClient(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)

agent = (
    Agent(name='avatar-agent', instructions='你是一个有数字形象的智能助手。')
    .with_llm(AliyunLLM(api_key='your-aliyun-key', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='your-minimax-key', voice_id='your-voice-id'))
    .with_stt(FengmingSTT(language='zh-CN'))
    .with_avatar(SensetimeAvatar(
        api_key='your-sensetime-key',
        agora_uid='2',
        avatar_id='your-avatar-id',
    ))
)

session = agent.create_session(client, channel='avatar-room', agent_uid='1', remote_uids=['100'])
agent_id = session.start()
session.say('你好！我是你的数字助手。')
session.stop()
```

## Order Matters

The `with_avatar()` call validates against the currently configured TTS. Always call `with_tts()` before `with_avatar()`:

```python
# Correct order: TTS first, then avatar
agent = (
    Agent(name='my-agent', instructions='你是一个智能助手。')
    .with_tts(MiniMaxTTS(key='your-key', voice_id='your-voice-id'))
    .with_avatar(SensetimeAvatar(api_key='your-key', agora_uid='2'))
)
```

If you call `with_avatar()` before `with_tts()`, the sample rate check is deferred to `session.start()`, which validates the configuration before making the API call.

## Sensetime Options

| Parameter | Type | Required | Description |
|---|---|---|---|
| `api_key` | `str` | Yes | Sensetime API key |
| `agora_uid` | `str` | Yes | UID for the avatar video stream |
| `avatar_id` | `str` | No | Avatar ID |
