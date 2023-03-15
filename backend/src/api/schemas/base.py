from pydantic import BaseModel, UUID4
from datetime import datetime


class EntityId(UUID4):
    pass


class BaseEntity(BaseModel):
    """Base model schema"""

    id: EntityId | None
    updated_at: str
    created_at: str


class ResponseModel(BaseEntity):
    pass


class RequestModel(BaseEntity):
    pass
