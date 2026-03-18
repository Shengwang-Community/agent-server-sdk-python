from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from typing_extensions import Literal

# Supported sample rates across all TTS providers.
SampleRate = Literal[8000, 16000, 22050, 24000, 44100, 48000]

# Provider-specific sample rate constraints.
MicrosoftSampleRate = Literal[8000, 16000, 24000, 48000]


class BaseLLM(ABC):
    """Abstract base class for all LLM vendor implementations."""

    @abstractmethod
    def to_config(self) -> Dict[str, Any]:
        """Serialize the LLM configuration to a dict for the REST API."""


class BaseTTS(ABC):
    """Abstract base class for all TTS vendor implementations."""

    @abstractmethod
    def to_config(self) -> Dict[str, Any]:
        """Serialize the TTS configuration to a dict for the REST API."""

    @property
    @abstractmethod
    def sample_rate(self) -> Optional[int]:
        """The configured sample rate in Hz, or ``None`` if not explicitly set."""


class BaseSTT(ABC):
    """Abstract base class for all STT vendor implementations."""

    @abstractmethod
    def to_config(self) -> Dict[str, Any]:
        """Serialize the STT configuration to a dict for the REST API."""


class BaseMLLM(ABC):
    """Abstract base class for all MLLM (multimodal LLM) vendor implementations."""

    @abstractmethod
    def to_config(self) -> Dict[str, Any]:
        """Serialize the MLLM configuration to a dict for the REST API."""


class BaseAvatar(ABC):
    """Abstract base class for all avatar vendor implementations."""

    @property
    @abstractmethod
    def required_sample_rate(self) -> int:
        """The TTS sample rate (Hz) that this avatar requires."""

    @abstractmethod
    def to_config(self) -> Dict[str, Any]:
        """Serialize the avatar configuration to a dict for the REST API."""
