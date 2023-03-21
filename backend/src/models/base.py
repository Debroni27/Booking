from datetime import datetime
import uuid

from pydantic import BaseModel, Field, UUID4


class EntityId(UUID4):  # type: ignore
    pass


class ABCEntity(BaseModel):  # type: ignore
    id: EntityId = Field(default_factory=uuid.uuid4())
    created_at: datetime
    updated_at: datetime


class RequestModel(ABCEntity):  # type: ignore
    pass


class ResponseModel(ABCEntity):  # type: ignore
    pass
