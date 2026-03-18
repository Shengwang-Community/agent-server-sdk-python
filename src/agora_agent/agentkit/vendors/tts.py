from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .base import BaseTTS, MicrosoftSampleRate


class MiniMaxTTSOptions(BaseModel):
    """Minimax TTS. See https://platform.minimaxi.com/docs/api-reference/speech-t2a-http"""

    key: str = Field(..., description="Minimax API key")
    model: str = Field(..., description="TTS model (e.g., speech-01-turbo)")
    voice_setting: Dict[str, Any] = Field(..., description="Voice settings (voice_id, speed, vol, pitch, emotion, etc.)")
    group_id: Optional[str] = Field(default=None, description="Minimax group ID")
    audio_setting: Optional[Dict[str, Any]] = Field(default=None, description="Audio settings (sample_rate, etc.)")
    pronunciation_dict: Optional[Dict[str, Any]] = Field(default=None, description="Pronunciation dictionary")
    language_boost: Optional[str] = Field(default=None, description="Language boost mode")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class MiniMaxTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = MiniMaxTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        if self.options.audio_setting and "sample_rate" in self.options.audio_setting:
            return self.options.audio_setting["sample_rate"]
        return None

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "key": self.options.key,
            "model": self.options.model,
            "voice_setting": self.options.voice_setting,
        }
        if self.options.group_id is not None:
            params["group_id"] = self.options.group_id
        if self.options.audio_setting is not None:
            params["audio_setting"] = self.options.audio_setting
        if self.options.pronunciation_dict is not None:
            params["pronunciation_dict"] = self.options.pronunciation_dict
        if self.options.language_boost is not None:
            params["language_boost"] = self.options.language_boost

        result: Dict[str, Any] = {"vendor": "minimax", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result


class TencentTTSOptions(BaseModel):
    """Tencent Cloud TTS. See https://cloud.tencent.com/document/product/1073/94308"""

    app_id: str = Field(..., description="Tencent app ID")
    secret_id: str = Field(..., description="Tencent secret ID")
    secret_key: str = Field(..., description="Tencent secret key")
    voice_type: int = Field(..., description="Voice type ID (e.g., 601005)")
    volume: Optional[int] = Field(default=None, description="Volume")
    speed: Optional[int] = Field(default=None, description="Speed")
    emotion_category: Optional[str] = Field(default=None, description="Emotion category")
    emotion_intensity: Optional[int] = Field(default=None, description="Emotion intensity")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class TencentTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = TencentTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        return None

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "app_id": self.options.app_id,
            "secret_id": self.options.secret_id,
            "secret_key": self.options.secret_key,
            "voice_type": self.options.voice_type,
        }
        if self.options.volume is not None:
            params["volume"] = self.options.volume
        if self.options.speed is not None:
            params["speed"] = self.options.speed
        if self.options.emotion_category is not None:
            params["emotion_category"] = self.options.emotion_category
        if self.options.emotion_intensity is not None:
            params["emotion_intensity"] = self.options.emotion_intensity

        result: Dict[str, Any] = {"vendor": "tencent", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result


class BytedanceTTSOptions(BaseModel):
    """Volcengine (Bytedance) TTS. See https://www.volcengine.com/docs/6561/79823"""

    token: str = Field(..., description="Volcengine token")
    app_id: str = Field(..., description="Volcengine app ID")
    cluster: Optional[str] = Field(default=None, description="Cluster (e.g., volcano_tts)")
    voice_type: str = Field(..., description="Voice type (e.g., BV700_streaming)")
    speed_ratio: Optional[float] = Field(default=None, description="Speed ratio")
    volume_ratio: Optional[float] = Field(default=None, description="Volume ratio")
    pitch_ratio: Optional[float] = Field(default=None, description="Pitch ratio")
    emotion: Optional[str] = Field(default=None, description="Emotion")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class BytedanceTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = BytedanceTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        return None

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "token": self.options.token,
            "app_id": self.options.app_id,
            "voice_type": self.options.voice_type,
        }
        if self.options.cluster is not None:
            params["cluster"] = self.options.cluster
        if self.options.speed_ratio is not None:
            params["speed_ratio"] = self.options.speed_ratio
        if self.options.volume_ratio is not None:
            params["volume_ratio"] = self.options.volume_ratio
        if self.options.pitch_ratio is not None:
            params["pitch_ratio"] = self.options.pitch_ratio
        if self.options.emotion is not None:
            params["emotion"] = self.options.emotion

        result: Dict[str, Any] = {"vendor": "bytedance", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result


class MicrosoftTTSOptions(BaseModel):
    """Microsoft Azure TTS."""

    key: str = Field(..., description="Azure subscription key")
    region: str = Field(..., description="Azure region (e.g., chinaeast2)")
    voice_name: str = Field(..., description="Voice name (e.g., zh-CN-YunxiNeural)")
    speed: Optional[float] = Field(default=None, description="Speed [0.5, 2.0]")
    volume: Optional[float] = Field(default=None, description="Volume [0.0, 100.0]")
    sample_rate: Optional[MicrosoftSampleRate] = Field(default=None, description="Sample rate in Hz")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class MicrosoftTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = MicrosoftTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        return self.options.sample_rate

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "key": self.options.key,
            "region": self.options.region,
            "voice_name": self.options.voice_name,
        }
        if self.options.speed is not None:
            params["speed"] = self.options.speed
        if self.options.volume is not None:
            params["volume"] = self.options.volume
        if self.options.sample_rate is not None:
            params["sample_rate"] = self.options.sample_rate

        result: Dict[str, Any] = {"vendor": "microsoft", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result


class CosyVoiceTTSOptions(BaseModel):
    """Alibaba Cloud CosyVoice TTS. See https://help.aliyun.com/zh/model-studio/cosyvoice-large-model-for-speech-synthesis/"""

    api_key: str = Field(..., description="CosyVoice API key")
    model: str = Field(..., description="Model (e.g., cosyvoice-v1)")
    voice: str = Field(..., description="Voice ID (e.g., longxiaochun)")
    sample_rate: Optional[int] = Field(default=None, description="Sample rate in Hz")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class CosyVoiceTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = CosyVoiceTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        return self.options.sample_rate

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "api_key": self.options.api_key,
            "model": self.options.model,
            "voice": self.options.voice,
        }
        if self.options.sample_rate is not None:
            params["sample_rate"] = self.options.sample_rate

        result: Dict[str, Any] = {"vendor": "cosyvoice", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result


class BytedanceDuplexTTSOptions(BaseModel):
    """Volcengine Duplex Streaming TTS. See https://www.volcengine.com/docs/6561/1329505"""

    app_id: str = Field(..., description="Volcengine app ID")
    token: str = Field(..., description="Volcengine token")
    speaker: str = Field(..., description="Speaker ID")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class BytedanceDuplexTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = BytedanceDuplexTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        return None

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "app_id": self.options.app_id,
            "token": self.options.token,
            "speaker": self.options.speaker,
        }

        result: Dict[str, Any] = {"vendor": "bytedance_duplex", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result


class StepFunTTSOptions(BaseModel):
    """StepFun TTS. See https://platform.stepfun.com/docs/api-reference/audio/ws_audio"""

    api_key: str = Field(..., description="StepFun API key")
    model: str = Field(..., description="Model (e.g., step-tts-mini)")
    voice_id: str = Field(..., description="Voice ID")
    skip_patterns: Optional[List[int]] = Field(default=None)

    class Config:
        extra = "forbid"


class StepFunTTS(BaseTTS):
    def __init__(self, **kwargs: Any):
        self.options = StepFunTTSOptions(**kwargs)

    @property
    def sample_rate(self) -> Optional[int]:
        return None

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "api_key": self.options.api_key,
            "model": self.options.model,
            "voice_id": self.options.voice_id,
        }

        result: Dict[str, Any] = {"vendor": "stepfun", "params": params}
        if self.options.skip_patterns is not None:
            result["skip_patterns"] = self.options.skip_patterns
        return result
