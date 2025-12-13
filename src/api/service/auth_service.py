from datetime import datetime, timedelta, timezone

from src.domain.exceptions import (
    InvalidCredentialsException, 
    AppException, 
    BusinessException,
    ForbiddenException
)

from src.infraestrutura.service.jwt_security import JWTSecurity
from src.dtos.token_dto import TokenDTO
from src.interfaces.application.interface_application_refresh_token import IRefreshTokenApplication
from src.interfaces.application.interface_application_user import IUserApplication
from src.interfaces.service.interface_service_refresh_token import IServiceRefreshToken


class AuthService(IServiceRefreshToken):

    def __init__(self, user_application: IUserApplication, refresh_token_application: IRefreshTokenApplication) -> None:
        self.__user_application = user_application
        self.__refresh_token_application = refresh_token_application
        self.__jwt_security = JWTSecurity()
        self.__exceptions: list[AppException] = []

    @property
    def validation(self):
        return self.__exceptions

    def create_user_token(self, username: str, password:str) -> TokenDTO:
        try:
            user = self.__user_application.get_by_username(username)

            if not user or not self.__jwt_security.verify_password(password, user.password):
                self.__exceptions.append(InvalidCredentialsException("Username ou senha inválidos"))

            if not user.active:
                self.__exceptions.append(ForbiddenException("Esse usuário foi inativado."))
            
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
        
        except Exception as e:
            self.__exceptions.append(AppException(e))
    
    def update_refresh_token(self, refresh_token: str) -> TokenDTO:
        refresh_token = self.__refresh_token_application.get_refresh_token(refresh_token)

        if not refresh_token or refresh_token.revoked:
            self.__exceptions.append(BusinessException("Refresh token inválido ou revogado"))

        if refresh_token.expires_at.timestamp() < datetime.now(timezone.utc).timestamp():
            self.__exceptions.append(BusinessException("Refresh token expirado"))

        self.__refresh_token_application.revoke_refresh_token(refresh_token.id)

        user = self.__user_application.get_by_id(refresh_token.user_id)

        if not user:
            self.__exceptions.append(BusinessException("Usuário do refresh token não foi encontrado"))

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

    def has_exceptions(self):
        return len(self.__exceptions) > 0
    
    def get_exceptions(self):
        return self.__exceptions