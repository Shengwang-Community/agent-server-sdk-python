from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .base import BaseAvatar

SENSETIME_SAMPLE_RATE = 16000


class SensetimeAvatarOptions(BaseModel):
    """Sensetime digital human avatar. See https://aigc.softsugar.com/"""

    agora_token: str = Field(..., description="Agora token for avatar stream")
    agora_uid: str = Field(..., description="Agora UID for the avatar stream (numeric string, max 32-bit)")
    appId: str = Field(..., description="Sensetime app ID")
    app_key: str = Field(..., description="Sensetime app key")
    sceneList: List[Dict[str, Any]] = Field(..., description="Scene list with digital_role config")

    class Config:
        extra = "forbid"


class SensetimeAvatar(BaseAvatar):
    def __init__(self, **kwargs: Any):
        self.options = SensetimeAvatarOptions(**kwargs)

    @property
    def required_sample_rate(self) -> int:
        return SENSETIME_SAMPLE_RATE

    def to_config(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "agora_token": self.options.agora_token,
            "agora_uid": self.options.agora_uid,
            "appId": self.options.appId,
            "app_key": self.options.app_key,
            "sceneList": self.options.sceneList,
        }

        return {"vendor": "sensetime", "params": params}
