# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [v1.0.0] — 2026-03-11

Initial stable release of the Agent Server SDK for Python.

### Added

- `Agent` builder with fluent API (`.with_llm()`, `.with_tts()`, `.with_stt()`, `.with_mllm()`, `.with_avatar()`)
- `AgentSession` and `AsyncAgentSession` for synchronous and async session lifecycle management
- Automatic token generation — pass `app_id` + `app_certificate` and tokens are handled internally
- Token utilities: `generate_rtc_token`, `generate_convo_ai_token`, `expires_in_hours`, `expires_in_minutes`
- Turn detection configuration via `TurnDetectionConfig` with nested `StartOfSpeechConfig` and `EndOfSpeechConfig`
- SAL (Selective Attention Locking) via `SalConfig` with `SalMode`
- Filler words support: `FillerWordsConfig`, `FillerWordsTrigger`, `FillerWordsContent`
- Session parameters: `SessionParams`, `SilenceConfig`, `FarewellConfig`, `ParametersDataChannel`
- Geofencing via `GeofenceConfig`
- Advanced features (MLLM mode) via `AdvancedFeatures`
- Type-safe constants: `DataChannel`, `SilenceActionValues`, `SalModeValues`, `GeofenceArea`, `FillerWordsSelectionRule`, `TurnDetectionTypeValues`
- Vendor integrations:
  - **LLM**: `AliyunLLM`, `BytedanceLLM`, `DeepSeekLLM`, `TencentLLM`, `CustomLLM`
  - **TTS**: `MiniMaxTTS`, `TencentTTS`, `BytedanceTTS`, `MicrosoftTTS`, `CosyVoiceTTS`, `BytedanceDuplexTTS`, `StepFunTTS`
  - **STT**: `FengmingSTT`, `TencentSTT`, `MicrosoftSTT`, `XfyunSTT`, `XfyunBigModelSTT`, `XfyunDialectSTT`
  - **Avatar**: `SensetimeAvatar`
