from datetime import datetime, timedelta, timezone
from src.aplicacao.aplicacao_refresh_token import AplicacaoRefreshToken
from src.dominio.exceptions import (
    InvalidCredentialsException, AppException, BusinessException
)

from src.anticorrupcao.auth.jwt_security import JWTSecurity
from src.aplicacao.aplicacao_user import AplicacaoUser
from src.dtos.token_dto import TokenDTO


class ServiceAuth:

    def __init__(self) -> None:
        self.__aplicacao_user = AplicacaoUser()
        self.__aplicacao_refresh = AplicacaoRefreshToken()
        self.__jwt_security = JWTSecurity()
        self.__exceptions = []

    def create_user_token(self, username: str, password:str) -> TokenDTO:
        try:
            user = self.__aplicacao_user.get_by_username(username)

            if not user or not self.__jwt_security.verify_password(password, user.password):
                self.__exceptions.append(InvalidCredentialsException("Username ou senha inválidos"))
            
            access_expires = timedelta(minutes=15)
            access_token = self.__jwt_security.create_access_token({"username": user.username,
                                                                    "email": user.email,
                                                                    "id": user.id}, 
                                                                    access_expires)
            
            refresh_token = self.__jwt_security.generate_refresh_token()
            refresh_token_expires_at = datetime.now(timezone.utc) + timedelta(days=7)

            self.__aplicacao_refresh.create_refresh_token(refresh_token, user.id, refresh_token_expires_at)

            return TokenDTO(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=int(access_expires.total_seconds())
            )
        
        except Exception as e:
            self.__exceptions.append(AppException(e))
    
    def update_refresh_token(self, refresh_token: str) -> TokenDTO:
        refresh_token = self.__aplicacao_refresh.get_refresh_token(refresh_token)

        if not refresh_token or refresh_token.revoked:
            self.__exceptions.append(BusinessException("Refresh token inválido ou revogado"))

        if refresh_token.expires_at.timestamp() < datetime.now(timezone.utc).timestamp():
            self.__exceptions.append(BusinessException("Refresh token expirado"))

        self.__aplicacao_refresh.revoke_refresh_token(refresh_token.id)

        user = self.__aplicacao_user.get_by_id(refresh_token.user_id)
        if not user:
            self.__exceptions.append(BusinessException("Usuário do refresh token não foi encontrado"))

        access_expires = timedelta(minutes=15)
        access_token = self.__jwt_security.create_access_token({"username": user.username,
                                                                "email": user.email,
                                                                "id": user.id},
                                                                access_expires)
        
        refresh_token = self.__jwt_security.generate_refresh_token()
        refresh_token_expires_at = datetime.now(timezone.utc) + timedelta(days=7)

        self.__aplicacao_refresh.create_refresh_token(refresh_token, user.id, refresh_token_expires_at)

        return TokenDTO(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=int(access_expires.total_seconds())
        ) 

    def has_exceptions(self):
        return len(self.__exceptions) > 0
    
    def get_exceptions(self):
        return self.__exceptions