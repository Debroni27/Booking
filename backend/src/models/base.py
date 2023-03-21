import orjson
from pydantic import BaseModel


# ABSTRACT BASE MODELS PART
class FrozenBaseModel(BaseModel):
    """
    Хэшируемая дефолтная модель из pydantic
    """

    class Config:
        frozen = True
        use_enum_values = True
        smart_union = True
        json_loads = orjson.loads

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class BaseRequestModel(FrozenBaseModel):  # type: ignore
    pass


class BaseResponseModel(FrozenBaseModel):  # type: ignore
    pass
