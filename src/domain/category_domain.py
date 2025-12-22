from typing import List
from src.data.database.unity_of_work import UnityOfWork
from src.entity.category_entity import CategoryEntity


class CategoryDomain():

    def __init__(self, repository):
        self.__repository = repository

    def attach_uow(self, uow: UnityOfWork) -> None:
        self.__repository.uow = uow

    def list_all_categories(self) -> List[CategoryEntity]:
        return self.__repository.get_all()