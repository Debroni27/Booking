from abc import ABC, abstractmethod
from models.base import ABCEntity, EntityId


class BaseCRUDRepository(ABC):
    """Basic CRUD repository for working with entities"""

    @abstractmethod
    def get_all(self) -> list[ABCEntity]:
        pass

    @abstractmethod
    def get(self, model: ABCEntity, id: EntityId) -> ABCEntity:
        return ABCEntity(id=None, created_at="test", updated_at="test")

    @abstractmethod
    def create(self, model: ABCEntity) -> ABCEntity:
        pass

    @abstractmethod
    def update(self, model: ABCEntity, id: EntityId) -> ABCEntity:
        pass

    @abstractmethod
    def delete(self, model: ABCEntity, id: EntityId) -> None:
        pass
