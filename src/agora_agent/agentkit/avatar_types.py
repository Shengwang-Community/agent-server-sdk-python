import typing


def is_sensetime_avatar(config: typing.Dict[str, typing.Any]) -> bool:
    return config.get("vendor") == "sensetime"


def validate_avatar_config(config: typing.Dict[str, typing.Any]) -> None:
    """Validate avatar configuration.

    Parameters
    ----------
    config : dict
        The avatar configuration dict (vendor + params).

    Raises
    ------
    ValueError
        If the configuration is invalid.
    """
    if is_sensetime_avatar(config):
        params = config.get("params", {})
        if not params.get("appId"):
            raise ValueError("Sensetime avatar requires appId")
        if not params.get("app_key"):
            raise ValueError("Sensetime avatar requires app_key")
        if not params.get("agora_uid"):
            raise ValueError("Sensetime avatar requires agora_uid")
        if not params.get("agora_token"):
            raise ValueError("Sensetime avatar requires agora_token")


def validate_avatar_tts_compatibility(
    avatar_config: typing.Dict[str, typing.Any],
    tts_sample_rate: int,
) -> None:
    """Validate that TTS sample rate is compatible with the avatar vendor.

    Different avatar vendors have specific sample rate requirements:
    - Sensetime: supports 16,000 Hz

    Parameters
    ----------
    avatar_config : dict
        The avatar configuration dict.
    tts_sample_rate : int
        The TTS sample rate in Hz.

    Raises
    ------
    ValueError
        If TTS sample rate is incompatible with the avatar vendor.
    """
    if is_sensetime_avatar(avatar_config):
        if tts_sample_rate != 16000:
            raise ValueError(
                f"Sensetime avatars ONLY support 16,000 Hz sample rate. "
                f"Your TTS is configured with {tts_sample_rate} Hz. "
                f"Please update your TTS configuration to use 16kHz sample rate."
            )
