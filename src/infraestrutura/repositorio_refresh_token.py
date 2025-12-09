from datetime import datetime
from typing import Optional
from src.dados.database.db import Database
from src.entidades.refresh_token_entity import RefreshTokenEntity

class RepositorioRefreshToken:
    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        with Database() as db:
            entity = RefreshTokenEntity(token=token, user_id=user_id, expires_at=expires_at, revoked=False)
            db.add(entity)
            db.commit()
            db.expunge(entity)

            return entity
    
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        with Database() as db:
            return db.query(RefreshTokenEntity).filter(RefreshTokenEntity.token == token).first()
    
    def revoke_refresh_token(self, token_id: int) -> None:
        with Database() as db:
            rt = db.query(RefreshTokenEntity).get(token_id)
            if rt:
                rt.revoked = True
                db.add(rt)
                db.commit()
    
    def revoke_all_user_refresh_tokens(self, user_id: int) -> None:
        with Database() as db:
            db.query(RefreshTokenEntity).filter(RefreshTokenEntity.user_id == user_id).update({"revoked": True})
            db.commit()