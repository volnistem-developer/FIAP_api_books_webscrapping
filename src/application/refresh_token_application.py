from datetime import datetime
from typing import Optional
from src.data.database.unity_of_work import UnityOfWork
from src.entity.refresh_token_entity import RefreshTokenEntity
from src.infraestrutura.logging.logger import get_logger
from src.interfaces.application.interface_refresh_token_application import IRefreshTokenApplication
from src.interfaces.domain.interface_refresh_token_domain import IRefreshTokenDomain


class RefreshTokenApplication(IRefreshTokenApplication):

    def __init__(self, domain: IRefreshTokenDomain) -> None:
        self.__domain = domain
        self.__logger = get_logger(self.__class__.__name__)
    
    def create_refresh_token(
        self,
        token: str,
        user_id: int,
        expires_at: datetime
    ) -> RefreshTokenEntity:
        self.__logger.info(
            f"Creating refresh token for user_id={user_id}, expires_at={expires_at}"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                entity = self.__domain.create_refresh_token(
                    token, user_id, expires_at
                )

                self.__logger.info(
                    f"Refresh token created successfully (id={entity.id}, user_id={user_id})"
                )
                return entity

            except Exception:
                self.__logger.exception(
                    f"Error while creating refresh token for user_id={user_id}"
                )
                raise
    
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        self.__logger.info("Fetching refresh token")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                entity = self.__domain.get_refresh_token(token)

                if entity:
                    self.__logger.info(
                        f"Refresh token found (id={entity.id}, user_id={entity.user_id})"
                    )
                else:
                    self.__logger.warning("Refresh token not found")

                return entity

            except Exception:
                self.__logger.exception("Error while fetching refresh token")
                raise
        
    def revoke_refresh_token(self, token_id: int) -> None:
        self.__logger.info(f"Revoking refresh token (id={token_id})")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                self.__domain.revoke_refresh_token(token_id)

                self.__logger.info(
                    f"Refresh token revoked successfully (id={token_id})"
                )

            except Exception:
                self.__logger.exception(
                    f"Error while revoking refresh token (id={token_id})"
                )
                raise
        