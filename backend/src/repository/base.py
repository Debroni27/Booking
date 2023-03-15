from abc import ABC, abstractmethod
from api.schemas.base import BaseEntity, EntityId


class BaseCRUD(ABC):
    """Base repository for CRUD methods on entity"""


    def get_all(self, model: BaseEntity) -> list[BaseEntity]:
        pass

    def get(self) -> BaseEntity:
        return BaseEntity(id=None, created_at="test", updated_at="test")


    def create(
        self,
        model: BaseEntity,
    ) -> BaseEntity:
        pass

    def update(self, model: BaseEntity, id: EntityId) -> BaseEntity:
        pass


    def delete(self, model: BaseEntity, id: EntityId) -> None:
        pass
