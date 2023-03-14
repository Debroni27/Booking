import enum


class Environment(str, enum.Enum):
    BASE: str = "BASE"  # type: ignore
    DEV: str = "DEV"  # type: ignore
