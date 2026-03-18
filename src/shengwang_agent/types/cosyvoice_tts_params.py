# Alibaba Cloud CosyVoice TTS configuration parameters.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class CosyvoiceTtsParams(UncheckedBaseModel):
    """
    Alibaba Cloud CosyVoice TTS configuration parameters.
    See https://help.aliyun.com/zh/model-studio/cosyvoice-large-model-for-speech-synthesis/
    """

    api_key: str = pydantic.Field()
    """CosyVoice API key"""

    model: str = pydantic.Field()
    """Model (e.g., cosyvoice-v1)"""

    voice: str = pydantic.Field()
    """Voice ID (e.g., longxiaochun)"""

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
