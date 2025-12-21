from datetime import datetime, timedelta, timezone

from src.exceptions.exceptions import (
    DataError,
    EntityDoesNotExistsError, 
    ForbiddenError,
    InvalidTokenError,
)

from src.infraestrutura.config.jwt_security import JWTSecurity
from src.dtos.token_dto import TokenDTO
from src.interfaces.application.interface_refresh_token_application import IRefreshTokenApplication
from src.interfaces.application.interface_user_application import IUserApplication
from src.interfaces.service.interface_service_refresh_token import IServiceRefreshToken


class AuthService(IServiceRefreshToken):

    def __init__(self, user_application: IUserApplication, refresh_token_application: IRefreshTokenApplication) -> None:
        self.__user_application = user_application
        self.__refresh_token_application = refresh_token_application
        self.__jwt_security = JWTSecurity()


    def create_user_token(self, username: str, password:str) -> TokenDTO:
        user = self.__user_application.get_by_username(username)

        if not user or not self.__jwt_security.verify_password(password, user.password):
            raise DataError("Usuário ou senha inválidos")

        if not user.active:
            raise ForbiddenError("Esse usuário foi inativado.")
        
        access_expires = timedelta(minutes=15)
        access_token = self.__jwt_security.create_access_token({"username": user.username,
                                                                "email": user.email,
                                                                "id": user.id}, 
                                                                access_expires)
        
        refresh_token = self.__jwt_security.generate_refresh_token()
        refresh_token_expires_at = datetime.now(timezone.utc) + timedelta(days=7)

        self.__refresh_token_application.create_refresh_token(refresh_token, user.id, refresh_token_expires_at)

        return TokenDTO(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=int(access_expires.total_seconds())
        )
    
    def update_refresh_token(self, refresh_token: str) -> TokenDTO:
        refresh_token = self.__refresh_token_application.get_refresh_token(refresh_token)

        if not refresh_token or refresh_token.revoked:
            raise InvalidTokenError('Token inválido ou revogado.')

        if refresh_token.expires_at.timestamp() < datetime.now(timezone.utc).timestamp():
            raise InvalidTokenError('Token inválido ou revogado.')

        self.__refresh_token_application.revoke_refresh_token(refresh_token.id)

        user = self.__user_application.get_by_id(refresh_token.user_id)

        if not user:
            raise EntityDoesNotExistsError("Usuário não foi encontrado")

        access_expires = timedelta(minutes=15)
        access_token = self.__jwt_security.create_access_token({"username": user.username,
                                                                "email": user.email,
                                                                "id": user.id},
                                                                access_expires)
        
        refresh_token = self.__jwt_security.generate_refresh_token()
        refresh_token_expires_at = datetime.now(timezone.utc) + timedelta(days=7)

        self.__refresh_token_application.create_refresh_token(refresh_token, user.id, refresh_token_expires_at)

        return TokenDTO(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=int(access_expires.total_seconds())
        ) 