from typing import List
from src.data.database.unity_of_work import UnityOfWork
from src.entity.category_entity import CategoryEntity
from src.interfaces.infrastructure.interface_category_repository import ICategoryRepository

class CategoryRepository(ICategoryRepository):

    def __init__(self, uow: UnityOfWork):
        self.uow = uow

    def get_by_name(self, name: str) -> CategoryEntity:
        return (
            self.uow.session
            .query(CategoryEntity)
            .filter(CategoryEntity.name == name)
            .one()
        )

    def get_all(self) -> List[CategoryEntity]:
        return self.uow.session.query(CategoryEntity).all()

    def get_or_create(self, name: str) -> CategoryEntity:
        category = (
            self.uow.session
            .query(CategoryEntity)
            .filter(CategoryEntity.name == name)
            .one_or_none()
        )

        if category:
            return category

        category = CategoryEntity(name=name)
        self.uow.session.add(category)

        return category