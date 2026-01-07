from typing import List
from src.dtos.category_dto import CategoryReadDTO
from src.entity.category_entity import CategoryEntity
from src.interfaces.service.interface_service_category import IServiceCategory


class CategoryService(IServiceCategory):

    def __init__(self, application) -> None:
        self.application = application

    def list_all_categories(self) -> List[CategoryReadDTO]:
        categories = self.application.list_all_categories()

        return categories
        # return [self.__convert_entity_to_dto(c) for c in categories]
    
    def __convert_entity_to_dto(self, entity: CategoryEntity) -> CategoryReadDTO:
        return CategoryReadDTO(
            id=entity.id,
            name=entity.name
        )