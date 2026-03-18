# StepFun TTS configuration parameters.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class StepfunTtsParams(UncheckedBaseModel):
    """
    StepFun TTS configuration parameters.
    See https://platform.stepfun.com/docs/api-reference/audio/ws_audio
    """

    api_key: str = pydantic.Field()
    """StepFun API key"""

    model: str = pydantic.Field()
    """Model (e.g., step-tts-mini)"""

    voice_id: str = pydantic.Field()
    """Voice ID"""

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
