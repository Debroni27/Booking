from src.models.base import ABCEntity, EntityId
from src.repository.base import BaseCRUDRepository


class UserRepository(BaseCRUDRepository):
    """User repository"""

    def get_all(self, model: ABCEntity) -> list[ABCEntity]:
        return ABCEntity

    def get(self, model: ABCEntity, id: EntityId) -> ABCEntity:
        return ABCEntity

    def create(self, model: ABCEntity) -> ABCEntity:
        return ABCEntity

    def update(self, model: ABCEntity, id: EntityId) -> ABCEntity:
        return ABCEntity

    def delete(self, model: ABCEntity, id: EntityId) -> None:
        ...
