---
sidebar_position: 2
title: MLLM Flow (Multimodal)
description: Use multimodal LLM for end-to-end audio processing.
---

# MLLM Flow (Multimodal)

The MLLM (Multimodal LLM) flow uses a single model to handle both audio input and output — no separate STT or TTS step. This gives the model direct access to voice tone, pacing, and emotion.

> **Note:** MLLM vendors are not yet available in the domestic API. This section is reserved for future support. For now, use the [Cascading Flow](./cascading-flow.md) instead.

## Required: Enable MLLM Mode

MLLM mode must be explicitly enabled via `advanced_features`:

```python
from shengwang_agent.agentkit import Agent, AdvancedFeatures

agent = Agent(
    name='realtime-agent',
    instructions='你是一个语音助手。',
    advanced_features=AdvancedFeatures(enable_mllm=True),
)
```

Without `AdvancedFeatures(enable_mllm=True)`, the SDK treats the session as a cascading flow and requires LLM + TTS vendors.

## When to Use MLLM vs. Cascading

| Consideration | MLLM | Cascading |
|---|---|---|
| Latency | Lower — single model, no pipeline | Higher — three models in sequence |
| Voice control | Model-dependent | Full vendor choice for TTS |
| Vendor flexibility | Limited | Mix and match LLM, TTS, STT vendors |
| Audio understanding | Model hears tone, pacing, emotion | STT produces text only |

## Next Steps

- For the cascading pipeline, see [Cascading Flow](./cascading-flow.md)
- To add a visual avatar, see [Avatars](./avatars.md)
