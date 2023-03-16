from datetime import datetime
import uuid

from pydantic import BaseModel, Field, UUID4


class EntityId(UUID4):
    pass


class ABCEntity(BaseModel):
    id: EntityId = Field(default_factory=uuid.uuid4())
    created_at: datetime
    updated_at: datetime


class RequestModel(ABCEntity):
    pass


class ResponseModel(ABCEntity):
    pass
