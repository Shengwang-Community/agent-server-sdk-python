---
sidebar_position: 4
title: Vendors
description: Typed vendor classes for LLM, TTS, STT, and Avatar providers.
---

# Vendors

The SDK provides typed vendor classes for every supported provider. Each vendor class validates its configuration with Pydantic and produces the correct API payload automatically.

All vendor classes are available from `agent.agentkit.vendors`:

```python
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT
```

## LLM Vendors

Used with `agent.with_llm()` for the cascading flow (ASR → LLM → TTS).

| Class | Provider | Required Parameters |
|---|---|---|
| `AliyunLLM` | Aliyun (Qwen) | `api_key` |
| `BytedanceLLM` | Bytedance (Doubao) | `api_key` |
| `DeepSeekLLM` | DeepSeek | `api_key` |
| `TencentLLM` | Tencent (Hunyuan) | `api_key` |
| `CustomLLM` | Custom endpoint | `api_key` |

```python
from agent.agentkit.vendors import AliyunLLM

llm = AliyunLLM(api_key='your-aliyun-key', model='qwen-max')
```

## TTS Vendors

Used with `agent.with_tts()`. Each TTS vendor produces audio at a specific sample rate — this matters when using [avatars](../guides/avatars.md).

| Class | Provider | Required Parameters |
|---|---|---|
| `MiniMaxTTS` | MiniMax | `key` |
| `TencentTTS` | Tencent | `key` |
| `BytedanceTTS` | Bytedance | `key` |
| `MicrosoftTTS` | Microsoft Azure | `key`, `region`, `voice_name` |
| `CosyVoiceTTS` | CosyVoice (Aliyun) | `key` |
| `BytedanceDuplexTTS` | Bytedance Duplex | `key` |
| `StepFunTTS` | StepFun | `key` |

```python
from agent.agentkit.vendors import MiniMaxTTS

tts = MiniMaxTTS(key='your-minimax-key', voice_id='your-voice-id')
```

## STT Vendors

Used with `agent.with_stt()`.

| Class | Provider | Required Parameters |
|---|---|---|
| `FengmingSTT` | Fengming ASR | — (all optional) |
| `TencentSTT` | Tencent | `app_id`, `secret_id`, `secret_key` |
| `MicrosoftSTT` | Microsoft Azure | `key`, `region` |
| `XfyunSTT` | Xfyun (iFlytek) | `app_id`, `api_key` |
| `XfyunBigModelSTT` | Xfyun Big Model | `app_id`, `api_key` |
| `XfyunDialectSTT` | Xfyun Dialect | `app_id`, `api_key` |

```python
from agent.agentkit.vendors import FengmingSTT

stt = FengmingSTT(language='zh-CN')
```

## Avatar Vendors

Used with `agent.with_avatar()`. Avatars require specific TTS sample rates — see [Avatar Integration](../guides/avatars.md).

| Class | Provider | Required Parameters |
|---|---|---|
| `SensetimeAvatar` | Sensetime | `api_key`, `agora_uid` |

```python
from agent.agentkit.vendors import SensetimeAvatar

avatar = SensetimeAvatar(api_key='your-sensetime-key', agora_uid='2')
```

## Base Classes

If you need to create a custom vendor, extend the appropriate base class:

| Base Class | Abstract Method |
|---|---|
| `BaseLLM` | `to_config() -> Dict[str, Any]` |
| `BaseTTS` | `to_config() -> Dict[str, Any]`, `sample_rate -> Optional[int]` |
| `BaseSTT` | `to_config() -> Dict[str, Any]` |
| `BaseMLLM` | `to_config() -> Dict[str, Any]` |
| `BaseAvatar` | `to_config() -> Dict[str, Any]`, `required_sample_rate -> int` |

For the full constructor options for every vendor, see the [Vendor Reference](../reference/vendors.md).
