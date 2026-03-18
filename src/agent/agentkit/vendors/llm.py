from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .base import BaseLLM


def _ensure_mcp_transport(servers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Ensure each MCP server has transport set (API requires it). Default to streamable_http."""
    result = []
    for s in servers:
        item = dict(s)
        if item.get("transport") is None:
            item["transport"] = "streamable_http"
        result.append(item)
    return result


class _BaseLLMOptions(BaseModel):
    """Common LLM options shared across all vendors."""

    url: str = Field(..., description="LLM callback URL (OpenAI-compatible)")
    api_key: Optional[str] = Field(default=None, description="LLM API key")
    model: Optional[str] = Field(default=None, description="Model name")
    max_tokens: Optional[int] = Field(default=None, gt=0)
    temperature: Optional[float] = Field(default=None, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    system_messages: Optional[List[Dict[str, Any]]] = Field(default=None)
    greeting_message: Optional[str] = Field(default=None)
    failure_message: Optional[str] = Field(default=None)
    max_history: Optional[int] = Field(default=None, description="Short-term memory entries [1,1024]")
    input_modalities: Optional[List[str]] = Field(default=None)
    output_modalities: Optional[List[str]] = Field(default=None)
    greeting_configs: Optional[Dict[str, Any]] = Field(default=None)
    template_variables: Optional[Dict[str, str]] = Field(default=None)
    params: Optional[Dict[str, Any]] = Field(default=None, description="Additional LLM params")
    mcp_servers: Optional[List[Dict[str, Any]]] = Field(default=None)

    class Config:
        extra = "forbid"


def _build_llm_config(options: _BaseLLMOptions, vendor: Optional[str]) -> Dict[str, Any]:
    """Build the LLM config dict from common options."""
    params: Dict[str, Any] = {}
    if options.model is not None:
        params["model"] = options.model
    if options.params is not None:
        params.update(options.params)
    if options.max_tokens is not None:
        params["max_tokens"] = options.max_tokens
    if options.temperature is not None:
        params["temperature"] = options.temperature
    if options.top_p is not None:
        params["top_p"] = options.top_p

    config: Dict[str, Any] = {"url": options.url}
    if options.api_key is not None:
        config["api_key"] = options.api_key
    if params:
        config["params"] = params
    if vendor is not None:
        config["vendor"] = vendor
    if options.system_messages is not None:
        config["system_messages"] = options.system_messages
    if options.greeting_message is not None:
        config["greeting_message"] = options.greeting_message
    if options.failure_message is not None:
        config["failure_message"] = options.failure_message
    if options.max_history is not None:
        config["max_history"] = options.max_history
    if options.input_modalities is not None:
        config["input_modalities"] = options.input_modalities
    if options.output_modalities is not None:
        config["output_modalities"] = options.output_modalities
    if options.greeting_configs is not None:
        config["greeting_configs"] = options.greeting_configs
    if options.template_variables is not None:
        config["template_variables"] = options.template_variables
    if options.mcp_servers is not None:
        config["mcp_servers"] = _ensure_mcp_transport(options.mcp_servers)
    return config


class AliyunLLM(BaseLLM):
    """Alibaba Cloud LLM."""

    def __init__(self, **kwargs: Any):
        self.options = _BaseLLMOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        return _build_llm_config(self.options, vendor="aliyun")


class BytedanceLLM(BaseLLM):
    """Bytedance (Volcengine) LLM."""

    def __init__(self, **kwargs: Any):
        self.options = _BaseLLMOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        return _build_llm_config(self.options, vendor="bytedance")


class DeepSeekLLM(BaseLLM):
    """DeepSeek LLM."""

    def __init__(self, **kwargs: Any):
        self.options = _BaseLLMOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        return _build_llm_config(self.options, vendor="deepseek")


class TencentLLM(BaseLLM):
    """Tencent LLM."""

    def __init__(self, **kwargs: Any):
        self.options = _BaseLLMOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        return _build_llm_config(self.options, vendor="tencent")


class CustomLLM(BaseLLM):
    """Custom LLM (carries extra turn_id and timestamp in requests)."""

    def __init__(self, **kwargs: Any):
        self.options = _BaseLLMOptions(**kwargs)

    def to_config(self) -> Dict[str, Any]:
        return _build_llm_config(self.options, vendor="custom")
