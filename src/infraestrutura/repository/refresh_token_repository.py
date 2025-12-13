from datetime import datetime
from typing import Optional
from src.data.database.db import Database
from src.entity.refresh_token_entity import RefreshTokenEntity
from src.interfaces.infrastructure.interface_refresh_token_repository import IRefreshTokenRepository

class RefreshTokenRepository(IRefreshTokenRepository):
    
    def __init__(self, db_connection: Database):
        self.__db_connection = db_connection

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        with self.__db_connection as db:
            entity = RefreshTokenEntity(token=token, user_id=user_id, expires_at=expires_at, revoked=False)
            db.add(entity)
            db.commit()
            db.expunge(entity)

            return entity
    
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        with self.__db_connection as db:
            return db.query(RefreshTokenEntity).filter(RefreshTokenEntity.token == token).first()
    
    def revoke_refresh_token(self, token_id: int) -> None:
        with self.__db_connection as db:
            rt = db.query(RefreshTokenEntity).get(token_id)
            if rt:
                rt.revoked = True
                db.add(rt)
                db.commit()
    
    def revoke_all_user_refresh_tokens(self, user_id: int) -> None:
        with self.__db_connection as db:
            db.query(RefreshTokenEntity).filter(RefreshTokenEntity.user_id == user_id).update({"revoked": True})
            db.commit()