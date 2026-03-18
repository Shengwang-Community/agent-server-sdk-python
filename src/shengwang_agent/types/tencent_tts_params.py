# Tencent Cloud TTS configuration parameters.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class TencentTtsParams(UncheckedBaseModel):
    """
    Tencent Cloud TTS configuration parameters.
    See https://cloud.tencent.com/document/product/1073/94308
    """

    app_id: str = pydantic.Field()
    """Tencent app ID"""

    secret_id: str = pydantic.Field()
    """Tencent secret ID"""

    secret_key: str = pydantic.Field()
    """Tencent secret key"""

    voice_type: int = pydantic.Field()
    """Voice type ID (e.g., 601005)"""

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
