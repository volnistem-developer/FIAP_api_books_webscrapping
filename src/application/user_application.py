from src.data.database.unity_of_work import UnityOfWork
from src.entity.user_entity import UserEntity
from src.infraestrutura.logging.logger import get_logger
from src.interfaces.application.interface_user_application import IUserApplication
from src.interfaces.domain.interface_user_domain import IUserDomain


class UserApplication(IUserApplication):

    def __init__(self, domain: IUserDomain) -> None:
        self.__domain = domain
        self.__logger = get_logger(self.__class__.__name__)


    def list_all(self) -> list[UserEntity]:
        self.__logger.info("Listing all users")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                users = self.__domain.list()

                self.__logger.info(f"{len(users)} users found")
                return users

            except Exception:
                self.__logger.exception("Error while listing users")
                raise

    def get_by_id(self, id: int) -> UserEntity:
        self.__logger.info(f"Fetching user by id={id}")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                user = self.__domain.get(id)

                self.__logger.info(f"User found (id={id})")
                return user

            except Exception:
                self.__logger.exception(f"Error while fetching user by id={id}")
                raise

    def get_by_username(self, username: str) -> UserEntity:
        self.__logger.info(f"Fetching user by username={username}")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                user = self.__domain.get_by_username(username)

                self.__logger.info(f"User found (username={username})")
                return user

            except Exception:
                self.__logger.exception(
                    f"Error while fetching user by username={username}"
                )
                raise

    def insert_user(self, entity: UserEntity) -> UserEntity:
        self.__logger.info(
            f"Creating user (username={entity.username}, email={entity.email})"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                created = self.__domain.insert(entity)

                self.__logger.info(
                    f"User created successfully (id={created.id}, username={created.username})"
                )
                return created

            except Exception:
                self.__logger.exception(
                    f"Error while creating user (username={entity.username})"
                )
                raise

    def delete_user(self, id: int) -> None:
        self.__logger.info(f"Deleting user (id={id})")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                self.__domain.delete(id)

                self.__logger.info(f"User deleted successfully (id={id})")

            except Exception:
                self.__logger.exception(f"Error while deleting user (id={id})")
                raise

    def update_user(self, id: int, name: str, username: str, email: str) -> UserEntity:
        self.__logger.info(
            f"Updating user (id={id}, username={username}, email={email})"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                updated = self.__domain.update(id, name, username, email)

                self.__logger.info(
                    f"User updated successfully (id={updated.id})"
                )
                return updated

            except Exception:
                self.__logger.exception(f"Error while updating user (id={id})")
                raise
