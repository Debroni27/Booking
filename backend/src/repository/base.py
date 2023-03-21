from abc import ABC, abstractmethod

from config.types import EntityID
from models.base import FrozenBaseModel


class BaseCRUDRepository(ABC):
    """Basic CRUD repository for working with entities"""

    @abstractmethod
    def get_all(self) -> list[FrozenBaseModel]:
        pass

    @abstractmethod
    def get(self, model: FrozenBaseModel, id: EntityID) -> FrozenBaseModel:
        return FrozenBaseModel(id=None, created_at="test", updated_at="test")

    @abstractmethod
    def create(self, model: FrozenBaseModel) -> FrozenBaseModel:
        pass

    @abstractmethod
    def update(self, model: FrozenBaseModel, id: EntityID) -> FrozenBaseModel:
        pass

    @abstractmethod
    def delete(self, model: FrozenBaseModel, id: EntityID) -> None:
        pass
