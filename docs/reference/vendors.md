---
sidebar_position: 4
title: Vendor Reference
description: Constructor options for all LLM, TTS, STT, and Avatar vendor classes.
---

# Vendor Reference

All vendor classes are available from `agent.agentkit.vendors`:

```python
from agent.agentkit.vendors import AliyunLLM, MiniMaxTTS, FengmingSTT, SensetimeAvatar
```

---

## LLM Vendors

### `AliyunLLM`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | Yes | — | Aliyun API key |
| `model` | `str` | No | `None` | Model name |
| `base_url` | `str` | No | `None` | Custom base URL |
| `temperature` | `float` | No | `None` | Sampling temperature |
| `top_p` | `float` | No | `None` | Nucleus sampling |
| `max_tokens` | `int` | No | `None` | Maximum tokens to generate |
| `system_messages` | `List[Dict]` | No | `None` | System messages |
| `greeting_message` | `str` | No | `None` | Greeting message |
| `failure_message` | `str` | No | `None` | Failure message |
| `input_modalities` | `List[str]` | No | `None` | Input modalities |
| `params` | `Dict[str, Any]` | No | `None` | Additional model parameters |

```python
from agent.agentkit.vendors import AliyunLLM

llm = AliyunLLM(api_key='your-key', model='qwen-max')
```

### `BytedanceLLM`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | Yes | — | Bytedance API key |
| `model` | `str` | No | `None` | Model name |
| `base_url` | `str` | No | `None` | Custom base URL |
| `temperature` | `float` | No | `None` | Sampling temperature |
| `top_p` | `float` | No | `None` | Nucleus sampling |
| `max_tokens` | `int` | No | `None` | Maximum tokens |
| `system_messages` | `List[Dict]` | No | `None` | System messages |
| `greeting_message` | `str` | No | `None` | Greeting message |
| `failure_message` | `str` | No | `None` | Failure message |
| `input_modalities` | `List[str]` | No | `None` | Input modalities |

```python
from agent.agentkit.vendors import BytedanceLLM

llm = BytedanceLLM(api_key='your-key', model='doubao-pro')
```

### `DeepSeekLLM`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | Yes | — | DeepSeek API key |
| `model` | `str` | No | `None` | Model name |
| `base_url` | `str` | No | `None` | Custom base URL |
| `temperature` | `float` | No | `None` | Sampling temperature |
| `max_tokens` | `int` | No | `None` | Maximum tokens |
| `system_messages` | `List[Dict]` | No | `None` | System messages |
| `greeting_message` | `str` | No | `None` | Greeting message |
| `failure_message` | `str` | No | `None` | Failure message |
| `input_modalities` | `List[str]` | No | `None` | Input modalities |

```python
from agent.agentkit.vendors import DeepSeekLLM

llm = DeepSeekLLM(api_key='your-key', model='deepseek-chat')
```

### `TencentLLM`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | Yes | — | Tencent API key |
| `model` | `str` | No | `None` | Model name |
| `base_url` | `str` | No | `None` | Custom base URL |
| `temperature` | `float` | No | `None` | Sampling temperature |
| `max_tokens` | `int` | No | `None` | Maximum tokens |
| `system_messages` | `List[Dict]` | No | `None` | System messages |
| `greeting_message` | `str` | No | `None` | Greeting message |
| `failure_message` | `str` | No | `None` | Failure message |
| `input_modalities` | `List[str]` | No | `None` | Input modalities |

```python
from agent.agentkit.vendors import TencentLLM

llm = TencentLLM(api_key='your-key', model='hunyuan-pro')
```

### `CustomLLM`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | Yes | — | API key |
| `model` | `str` | No | `None` | Model name |
| `base_url` | `str` | No | `None` | Custom base URL |
| `temperature` | `float` | No | `None` | Sampling temperature |
| `max_tokens` | `int` | No | `None` | Maximum tokens |
| `system_messages` | `List[Dict]` | No | `None` | System messages |
| `greeting_message` | `str` | No | `None` | Greeting message |
| `failure_message` | `str` | No | `None` | Failure message |
| `input_modalities` | `List[str]` | No | `None` | Input modalities |

```python
from agent.agentkit.vendors import CustomLLM

llm = CustomLLM(api_key='your-key', base_url='https://your-endpoint.com/v1')
```

---

## TTS Vendors

### `MiniMaxTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | MiniMax API key |
| `voice_id` | `str` | No | `None` | Voice ID |
| `model` | `str` | No | `None` | Model name |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

```python
from agent.agentkit.vendors import MiniMaxTTS

tts = MiniMaxTTS(key='your-key', voice_id='your-voice-id')
```

### `TencentTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | Tencent API key |
| `voice_type` | `int` | No | `None` | Voice type |
| `sample_rate` | `int` | No | `None` | Sample rate |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

### `BytedanceTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | Bytedance API key |
| `voice_type` | `str` | No | `None` | Voice type |
| `app_id` | `str` | No | `None` | App ID |
| `cluster` | `str` | No | `None` | Cluster |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

### `MicrosoftTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | Azure subscription key |
| `region` | `str` | Yes | — | Azure region (e.g., `eastasia`) |
| `voice_name` | `str` | Yes | — | Voice name (e.g., `zh-CN-XiaoxiaoNeural`) |
| `sample_rate` | `int` | No | `None` | Sample rate: 8000, 16000, 24000, or 48000 Hz |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

### `CosyVoiceTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | CosyVoice API key |
| `model` | `str` | No | `None` | Model name |
| `voice` | `str` | No | `None` | Voice name |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

### `BytedanceDuplexTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | Bytedance API key |
| `voice_type` | `str` | No | `None` | Voice type |
| `app_id` | `str` | No | `None` | App ID |
| `cluster` | `str` | No | `None` | Cluster |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

### `StepFunTTS`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | StepFun API key |
| `model` | `str` | No | `None` | Model name |
| `voice` | `str` | No | `None` | Voice name |
| `skip_patterns` | `List[int]` | No | `None` | Skip patterns |

---

## STT Vendors

### `FengmingSTT`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `language` | `str` | No | `None` | Language code |
| `additional_params` | `Dict[str, Any]` | No | `None` | Additional parameters |

```python
from agent.agentkit.vendors import FengmingSTT

stt = FengmingSTT(language='zh-CN')
```

### `TencentSTT`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `app_id` | `str` | Yes | — | Tencent App ID |
| `secret_id` | `str` | Yes | — | Tencent Secret ID |
| `secret_key` | `str` | Yes | — | Tencent Secret Key |
| `language` | `str` | No | `None` | Language code |
| `additional_params` | `Dict[str, Any]` | No | `None` | Additional parameters |

### `MicrosoftSTT`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `key` | `str` | Yes | — | Azure subscription key |
| `region` | `str` | Yes | — | Azure region |
| `language` | `str` | No | `None` | Language code |
| `additional_params` | `Dict[str, Any]` | No | `None` | Additional parameters |

### `XfyunSTT`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `app_id` | `str` | Yes | — | Xfyun App ID |
| `api_key` | `str` | Yes | — | Xfyun API key |
| `language` | `str` | No | `None` | Language code |
| `additional_params` | `Dict[str, Any]` | No | `None` | Additional parameters |

### `XfyunBigModelSTT`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `app_id` | `str` | Yes | — | Xfyun App ID |
| `api_key` | `str` | Yes | — | Xfyun API key |
| `language` | `str` | No | `None` | Language code |
| `additional_params` | `Dict[str, Any]` | No | `None` | Additional parameters |

### `XfyunDialectSTT`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `app_id` | `str` | Yes | — | Xfyun App ID |
| `api_key` | `str` | Yes | — | Xfyun API key |
| `language` | `str` | No | `None` | Language/dialect code |
| `additional_params` | `Dict[str, Any]` | No | `None` | Additional parameters |

---

## Avatar Vendors

### `SensetimeAvatar`

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `api_key` | `str` | Yes | — | Sensetime API key |
| `agora_uid` | `str` | Yes | — | Agora UID for avatar video stream |
| `avatar_id` | `str` | No | `None` | Avatar ID |

```python
from agent.agentkit.vendors import SensetimeAvatar

avatar = SensetimeAvatar(api_key='your-key', agora_uid='2')
```
