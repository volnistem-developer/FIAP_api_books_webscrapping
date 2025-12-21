from src.data.database.unity_of_work import UnityOfWork


class CategoryApplication():
        
    def __init__(self, domain) -> None:
        self.__domain = domain

    def list_all_categories(self):
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.list_all_categories()