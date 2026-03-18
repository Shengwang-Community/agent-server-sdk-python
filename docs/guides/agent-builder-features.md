---
sidebar_position: 5
title: Agent Builder Features
description: Configure SAL, advanced features, parameters, geofence, labels, RTC, filler words, and more.
---

# Agent Builder Features

The Agent builder supports many configuration options beyond the core LLM, TTS, and STT vendors. This guide shows how to use each feature.

For string values with a finite set of options (e.g. `data_channel`, `sal_mode`, `area`), use the type-safe constants (`DataChannel`, `SalModeValues`, `GeofenceArea`, etc.) instead of raw strings to avoid typos and get IDE autocomplete.

## Overview

| Feature | Method | Description |
|---|---|---|
| `sal` | `with_sal(config)` | Selective Attention Locking — speaker recognition and noise suppression |
| `advanced_features` | `with_advanced_features(features)` | Enable MLLM, RTM, SAL, tools |
| `parameters` | `with_parameters(params)` | Silence config, farewell config, data channel |
| `failure_message` | `with_failure_message(msg)` | Message spoken when LLM fails |
| `max_history` | `with_max_history(n)` | Max conversation turns in LLM context |
| `geofence` | `with_geofence(config)` | Restrict backend server regions |
| `labels` | `with_labels(labels)` | Custom key-value labels (returned in callbacks) |
| `rtc` | `with_rtc(config)` | RTC media encryption |
| `filler_words` | `with_filler_words(config)` | Filler words while waiting for LLM |

## SAL (Selective Attention Locking)

SAL helps the agent focus on the primary speaker and suppress background noise. Enable it via `advanced_features` and configure with `with_sal`:

```python
from agent import AgentClient, Area
from agent.agentkit import Agent, AdvancedFeatures, SalConfig, SalModeValues
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

agent = (
    Agent(
        name='sal-assistant',
        instructions='你是一个智能助手。',
        advanced_features=AdvancedFeatures(enable_sal=True),
    )
    .with_sal(SalConfig(
        sal_mode=SalModeValues.LOCKING,
        sample_urls={'primary-speaker': 'https://example.com/voiceprint.pcm'},
    ))
    .with_llm(AliyunLLM(api_key='your-key', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='your-key', voice_id='your-voice-id'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

Use `SalModeValues.LOCKING` or `SalModeValues.RECOGNITION` for type safety.

## Advanced Features

Enable MLLM, RTM, SAL, or tools:

```python
from agent.agentkit import Agent, AdvancedFeatures

# RTM signaling for custom data delivery
agent = Agent(advanced_features=AdvancedFeatures(enable_rtm=True))

# Enable tool invocation via MCP
agent = Agent(advanced_features=AdvancedFeatures(enable_tools=True))
```

## Session Parameters

Configure silence handling, farewell behavior, and data channel:

```python
from agent.agentkit import (
    Agent,
    SessionParams,
    SilenceConfig,
    FarewellConfig,
    SilenceActionValues,
    DataChannel,
)

agent = (
    Agent(name='params-agent')
    .with_parameters(SessionParams(
        silence_config=SilenceConfig(
            timeout_ms=10000,
            action=SilenceActionValues.SPEAK,
            content="我还在，请慢慢说。",
        ),
        farewell_config=FarewellConfig(
            graceful_enabled=True,
            graceful_timeout_seconds=10,
        ),
        data_channel=DataChannel.RTM,  # or DataChannel.DATASTREAM
    ))
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

## Failure Message and Max History

```python
agent = (
    Agent(
        name='assistant',
        failure_message='抱歉，遇到了错误，请重试。',
        max_history=20,
    )
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)

# Or via builder methods
agent = (
    Agent()
    .with_failure_message('出了点问题。')
    .with_max_history(15)
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

## Geofence

Restrict which geographic regions the backend can use:

```python
from agent.agentkit import Agent, GeofenceConfig, GeofenceArea, GeofenceExcludeArea

agent = (
    Agent()
    .with_geofence(GeofenceConfig(area=GeofenceArea.NORTH_AMERICA))
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)

# Global with exclusion
agent = (
    Agent()
    .with_geofence(GeofenceConfig(area=GeofenceArea.GLOBAL, exclude_area=GeofenceExcludeArea.EUROPE))
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

Use `GeofenceArea` and `GeofenceExcludeArea` for type-safe region values.

## Labels

Attach custom labels returned in notification callbacks:

```python
agent = (
    Agent()
    .with_labels({
        'environment': 'production',
        'team': 'support',
        'version': '1.2.0',
    })
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

## RTC Encryption

Configure RTC media encryption:

```python
from agent.agentkit import Agent, RtcConfig

agent = (
    Agent()
    .with_rtc(RtcConfig(
        encryption_key='your-32-byte-key',
        encryption_mode=5,  # AES_128_GCM
    ))
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

## Filler Words

Play filler words while waiting for the LLM response:

```python
from agent.agentkit import (
    Agent,
    FillerWordsConfig,
    FillerWordsTrigger,
    FillerWordsTriggerFixedTimeConfig,
    FillerWordsContent,
    FillerWordsContentStaticConfig,
    FillerWordsSelectionRule,
)

agent = (
    Agent()
    .with_filler_words(FillerWordsConfig(
        enable=True,
        trigger=FillerWordsTrigger(
            mode='fixed_time',
            fixed_time_config=FillerWordsTriggerFixedTimeConfig(response_wait_ms=2000),
        ),
        content=FillerWordsContent(
            mode='static',
            static_config=FillerWordsContentStaticConfig(
                phrases=['让我想想...', '稍等一下...', '嗯...'],
                selection_rule=FillerWordsSelectionRule.SHUFFLE,
            ),
        ),
    ))
    .with_llm(AliyunLLM(api_key='...', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='...', voice_id='...'))
    .with_stt(FengmingSTT(language='zh-CN'))
)
```

## Properties (Getters)

Read back configuration via properties:

```python
from agent.agentkit import Agent, GeofenceConfig, GeofenceArea

agent = (
    Agent(max_history=20)
    .with_geofence(GeofenceConfig(area=GeofenceArea.EUROPE))
    .with_labels({'env': 'staging'})
)

agent.name           # str | None
agent.max_history    # 20
agent.geofence       # GeofenceConfig(area='EUROPE')
agent.labels         # {'env': 'staging'}
agent.sal            # SalConfig | None
agent.advanced_features
agent.parameters
agent.failure_message
agent.rtc
agent.filler_words
agent.config         # Full read-only snapshot
```

## Chaining All Features

```python
from agent import AgentClient, Area
from agent.agentkit import (
    Agent,
    AdvancedFeatures,
    SessionParams,
    SilenceConfig,
    FarewellConfig,
    GeofenceConfig,
    GeofenceArea,
    FillerWordsConfig,
    FillerWordsTrigger,
    FillerWordsTriggerFixedTimeConfig,
    FillerWordsContent,
    FillerWordsContentStaticConfig,
    SilenceActionValues,
    DataChannel,
    FillerWordsSelectionRule,
)
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT

client = AgentClient(
    area=Area.CN,
    app_id='your-app-id',
    app_certificate='your-app-certificate',
)

agent = (
    Agent(
        name='full-featured-assistant',
        instructions='你是一个智能语音助手。',
        greeting='你好！有什么可以帮你的？',
        failure_message='抱歉，处理出了点问题。',
        max_history=20,
    )
    .with_llm(AliyunLLM(api_key='your-key', model='qwen-max'))
    .with_tts(MiniMaxTTS(key='your-key', voice_id='your-voice-id'))
    .with_stt(FengmingSTT(language='zh-CN'))
    .with_advanced_features(AdvancedFeatures(enable_rtm=True))
    .with_parameters(SessionParams(
        silence_config=SilenceConfig(
            timeout_ms=8000,
            action=SilenceActionValues.SPEAK,
            content="我在听。",
        ),
        farewell_config=FarewellConfig(
            graceful_enabled=True,
            graceful_timeout_seconds=5,
        ),
    ))
    .with_geofence(GeofenceConfig(area=GeofenceArea.NORTH_AMERICA))
    .with_labels({'app': 'voice-assistant', 'version': '2.0'})
    .with_filler_words(FillerWordsConfig(
        enable=True,
        trigger=FillerWordsTrigger(
            mode='fixed_time',
            fixed_time_config=FillerWordsTriggerFixedTimeConfig(response_wait_ms=1500),
        ),
        content=FillerWordsContent(
            mode='static',
            static_config=FillerWordsContentStaticConfig(
                phrases=['让我想想...', '请稍等。'],
                selection_rule=FillerWordsSelectionRule.SHUFFLE,
            ),
        ),
    ))
)

session = agent.create_session(
    client,
    channel='demo-room',
    agent_uid='1',
    remote_uids=['100'],
    idle_timeout=120,
)

agent_id = session.start()
```

## Next steps

- [Agent Reference](../reference/agent.md) — full API signatures
- [Cascading Flow](./cascading-flow.md) — ASR → LLM → TTS setup
- [Regional Routing](./regional-routing.md) — client area and geofence
