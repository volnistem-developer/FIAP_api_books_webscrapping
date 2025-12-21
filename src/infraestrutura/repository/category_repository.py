from src.data.database.unity_of_work import UnityOfWork
from src.entity.category_entity import CategoryEntity

class CategoryRepository:

    def __init__(self, uow: UnityOfWork):
        self.uow = uow

    def get_by_name(self, name: str):
        return (
            self.uow.session
            .query(CategoryEntity)
            .filter(CategoryEntity.name == name)
            .one()
        )

    def get_all(self):
        return self.uow.session.query(CategoryEntity).all()

    def get_or_create(self, name: str):
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