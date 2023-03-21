import enum


class Environment(str, enum.Enum):
    BASE: str = "BASE"
    DEV: str = "DEV"
