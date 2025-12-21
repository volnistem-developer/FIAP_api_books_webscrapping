from datetime import datetime
from typing import Optional
from src.data.database.unity_of_work import UnityOfWork
from src.entity.refresh_token_entity import RefreshTokenEntity
from src.interfaces.infrastructure.interface_refresh_token_repository import IRefreshTokenRepository


class RefreshTokenRepository(IRefreshTokenRepository):

    def __init__(self, uow: UnityOfWork):
        self.uow = uow  

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        entity = RefreshTokenEntity(token=token, user_id=user_id, expires_at=expires_at, revoked=False)
        self.uow.session.add(entity)
        return entity
    
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        return (
            self.uow.session
            .query(RefreshTokenEntity)
            .filter(
                RefreshTokenEntity.token == token,
                RefreshTokenEntity.revoked == False
            )
            .one_or_none()
        )
    
    def revoke_refresh_token(self, token_id: int) -> None:
        entity = self.uow.session.get(RefreshTokenEntity, token_id)

        if not entity:
            return

        entity.revoked = True
    
    def revoke_all_user_refresh_tokens(self, user_id: int) -> None:
        (
            self.uow.session
            .query(RefreshTokenEntity)
            .filter(RefreshTokenEntity.user_id == user_id)
            .update({"revoked": True})
        )