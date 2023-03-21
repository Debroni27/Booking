from abc import ABC
from uuid import UUID, uuid4

from utils.base import ValidatedString

ENTITY_ID_ALLOWED = False


# ID PART
class ID(UUID, ABC):
    @classmethod
    def generate(cls):
        generated = uuid4()
        return cls(int=generated.int, is_safe=generated.is_safe)

    @classmethod
    def _from(cls, some: UUID):
        return cls(int=some.int, is_safe=some.is_safe)


class EntityID(ID, ABC):
    pass


class UserID(EntityID):
    pass


class AdminID(EntityID):
    pass


class HotelID(EntityID):
    pass


class RoomID(EntityID):
    pass


class GeoLocationID(EntityID):
    pass


# REPR PART


class ValidStr(ValidatedString):
    min_length = 1
    strip_whitespace = True


class EntityRepr(ValidStr):
    pass
