import logging
import pathlib

import decouple
import pydantic

ROOT_DIR: pathlib.Path = pathlib.Path(
    __file__
).parent.parent.parent.parent.parent.resolve()


class BackendBaseSettings(pydantic.BaseSettings):
    TITLE: str = "API for boooking"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str | None = None
    DEBUG: bool = False

    SERVER_HOST: str = decouple.config("BACKEND_SERVER_HOST", cast=str)  # type: ignore
    SERVER_PORT: int = decouple.config("BACKEND_SERVER_PORT", cast=int)  # type: ignore
    SERVER_WORKERS: int = decouple.config("BACKEND_SERVER_WORKERS", cast=int)  # type: ignore
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    MONGODB_HOST: str = decouple.config("POSTGRES_HOST", cast=str)  # type: ignore
    MONGODB_PORT: int = decouple.config("POSTGRES_PORT", cast=int)  # type: ignore
    MONGODB_DB_NAME: str = decouple.config("POSTGRES_DB", cast=str)  # type: ignore
    MONGODB_USENRAME: str = decouple.config("POSTGRES_USERNAME", cast=str)  # type: ignore
    MONGODB_PASSWORD: str = decouple.config("POSTGRES_PASSWORD", cast=str)  # type: ignore
    MONGODB_MAX_POOL_SIZE: int = decouple.config("DB_MAX_POOL_CON", cast=int)  # type: ignore
    MONGODB_POOL_SIZE: int = decouple.config("DB_POOL_SIZE", cast=int)  # type: ignore

    IS_ALLOWED_CREDENTIALS: bool = decouple.config("IS_ALLOWED_CREDENTIALS", cast=bool)  # type: ignore
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://0.0.0.0:3000",
        "http://127.0.0.1:3000",
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config(pydantic.BaseConfig):
        case_sensitive: bool = True
        env_file: str = f"{str(ROOT_DIR)}/.env"
        validate_assignment: bool = True

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
