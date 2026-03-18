# Bytedance Duplex Streaming TTS configuration parameters.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class BytedanceDuplexTtsParams(UncheckedBaseModel):
    """
    Bytedance (Volcengine) Duplex Streaming TTS configuration parameters.
    See https://www.volcengine.com/docs/6561/1329505
    """

    app_id: str = pydantic.Field()
    """Volcengine app ID"""

    token: str = pydantic.Field()
    """Volcengine token"""

    speaker: str = pydantic.Field()
    """Speaker ID"""

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
