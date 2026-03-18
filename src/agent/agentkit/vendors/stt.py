from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .base import BaseSTT


class FengmingSTTOptions(BaseModel):
    """Fengming ASR."""

    language: Optional[str] = Field(default="zh-CN", description="Language code (e.g., zh-CN, en-US)")
    additional_params: Optional[Dict[str, Any]] = Field(default=None)

    class Config:
        extra = "forbid"


class FengmingSTT(BaseSTT):
    def __init__(self, **kwargs: Any):
        self.options = FengmingSTTOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if self.options.additional_params is not None:
            params.update(self.options.additional_params)

        return {
            "vendor": "fengming",
            "language": self.options.language,
            "params": params,
        }


class TencentSTTOptions(BaseModel):
    """Tencent Cloud ASR. See https://cloud.tencent.com/document/product/1093/48982"""

    key: str = Field(..., description="Tencent secret key")
    app_id: str = Field(..., description="Tencent app ID")
    secret: str = Field(..., description="Tencent secret")
    engine_model_type: Optional[str] = Field(default=None, description="Engine model type (e.g., 16k_zh)")
    voice_id: Optional[str] = Field(default=None, description="Voice ID")
    language: Optional[str] = Field(default="zh-CN", description="Language code")
    additional_params: Optional[Dict[str, Any]] = Field(default=None)

    class Config:
        extra = "forbid"


class TencentSTT(BaseSTT):
    def __init__(self, **kwargs: Any):
        self.options = TencentSTTOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "key": self.options.key,
            "app_id": self.options.app_id,
            "secret": self.options.secret,
        }
        if self.options.engine_model_type is not None:
            params["engine_model_type"] = self.options.engine_model_type
        if self.options.voice_id is not None:
            params["voice_id"] = self.options.voice_id
        if self.options.additional_params is not None:
            params.update(self.options.additional_params)

        return {
            "vendor": "tencent",
            "language": self.options.language,
            "params": params,
        }


class MicrosoftSTTOptions(BaseModel):
    """Microsoft Azure ASR."""

    key: str = Field(..., description="Azure subscription key")
    region: str = Field(..., description="Azure region (e.g., chinaeast2)")
    language: Optional[str] = Field(default="zh-CN", description="Language code")
    phrase_list: Optional[List[str]] = Field(default=None, description="Phrase list for hotwords")
    additional_params: Optional[Dict[str, Any]] = Field(default=None)

    class Config:
        extra = "forbid"


class MicrosoftSTT(BaseSTT):
    def __init__(self, **kwargs: Any):
        self.options = MicrosoftSTTOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "key": self.options.key,
            "region": self.options.region,
        }
        if self.options.language is not None:
            params["language"] = self.options.language
        if self.options.phrase_list is not None:
            params["phrase_list"] = self.options.phrase_list
        if self.options.additional_params is not None:
            params.update(self.options.additional_params)

        return {
            "vendor": "microsoft",
            "language": self.options.language,
            "params": params,
        }


class XfyunSTTOptions(BaseModel):
    """iFlytek (Xfyun) traditional ASR. See https://www.xfyun.cn/doc/spark/asr_llm/rtasr_llm.html"""

    api_key: str = Field(..., description="Xfyun API key")
    app_id: str = Field(..., description="Xfyun app ID")
    api_secret: str = Field(..., description="Xfyun API secret")
    language: Optional[str] = Field(default="zh_cn", description="Language code")
    additional_params: Optional[Dict[str, Any]] = Field(default=None)

    class Config:
        extra = "forbid"


class XfyunSTT(BaseSTT):
    def __init__(self, **kwargs: Any):
        self.options = XfyunSTTOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "api_key": self.options.api_key,
            "app_id": self.options.app_id,
            "api_secret": self.options.api_secret,
        }
        if self.options.language is not None:
            params["language"] = self.options.language
        if self.options.additional_params is not None:
            params.update(self.options.additional_params)

        return {
            "vendor": "xfyun",
            "language": self.options.language,
            "params": params,
        }


class XfyunBigModelSTTOptions(BaseModel):
    """iFlytek (Xfyun) Big Model ASR."""

    api_key: str = Field(..., description="Xfyun API key")
    app_id: str = Field(..., description="Xfyun app ID")
    api_secret: str = Field(..., description="Xfyun API secret")
    language_name: Optional[str] = Field(default="cn", description="Language name")
    language: Optional[str] = Field(default="mix", description="Language mode")
    additional_params: Optional[Dict[str, Any]] = Field(default=None)

    class Config:
        extra = "forbid"


class XfyunBigModelSTT(BaseSTT):
    def __init__(self, **kwargs: Any):
        self.options = XfyunBigModelSTTOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "api_key": self.options.api_key,
            "app_id": self.options.app_id,
            "api_secret": self.options.api_secret,
        }
        if self.options.language_name is not None:
            params["language_name"] = self.options.language_name
        if self.options.language is not None:
            params["language"] = self.options.language
        if self.options.additional_params is not None:
            params.update(self.options.additional_params)

        return {
            "vendor": "xfyun_bigmodel",
            "language": self.options.language,
            "params": params,
        }


class XfyunDialectSTTOptions(BaseModel):
    """iFlytek (Xfyun) Dialect ASR."""

    app_id: str = Field(..., description="Xfyun app ID")
    access_key_id: str = Field(..., description="Xfyun access key ID")
    access_key_secret: str = Field(..., description="Xfyun access key secret")
    language: Optional[str] = Field(default="zh-CN", description="Language code")
    additional_params: Optional[Dict[str, Any]] = Field(default=None)

    class Config:
        extra = "forbid"


class XfyunDialectSTT(BaseSTT):
    def __init__(self, **kwargs: Any):
        self.options = XfyunDialectSTTOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "app_id": self.options.app_id,
            "access_key_id": self.options.access_key_id,
            "access_key_secret": self.options.access_key_secret,
        }
        if self.options.language is not None:
            params["language"] = self.options.language
        if self.options.additional_params is not None:
            params.update(self.options.additional_params)

        return {
            "vendor": "xfyun_dialect",
            "language": self.options.language,
            "params": params,
        }
