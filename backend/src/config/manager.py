from functools import lru_cache

import decouple

from config.settings.base import BackendBaseSettings
from config.settings.development import BackendDevSettings
from config.settings.environment import Environment


class BackendSettingsFactory:
    """Select Enveronment"""

    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> BackendBaseSettings:
        if self.environment == Environment.BASE.value:
            return BackendBaseSettings()
        return BackendDevSettings()


@lru_cache()
def get_settings() -> BackendBaseSettings:
    return BackendSettingsFactory(
        environment=decouple.config("ENVIRONMENT", default="DEV", cast=str)
    )()


settings: BackendBaseSettings = get_settings()
