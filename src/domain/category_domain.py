from src.data.database.unity_of_work import UnityOfWork


class CategoryDomain():

    def __init__(self, repository):
        self.__repository = repository

    def attach_uow(self, uow: UnityOfWork):
        self.__repository.uow = uow

    def list_all_categories(self):
        return self.__repository.get_all()