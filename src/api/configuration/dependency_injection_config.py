from src.api.service.auth_service import AuthService
from src.api.service.user_service import UserService
from src.application.refresh_token_application import RefreshTokenApplication
from src.application.user_application import UserApplication
from src.data.database.db import Database
from src.domain.refresh_token_domain import RefreshTokenDomain
from src.domain.user_domain import UserDomain
from src.infraestrutura.repository.refresh_token_repository import RefreshTokenRepository
from src.infraestrutura.repository.user_repository import UserRepository 

class GetServices():
    
    db = Database()

    __user_repository = UserRepository(db)
    __user_domain = UserDomain(__user_repository)
    __user_application = UserApplication(__user_domain)
    user_service = UserService(__user_application)

    __refresh_repository = RefreshTokenRepository(db)
    __refresh_domain = RefreshTokenDomain(__refresh_repository)
    __refresh_application = RefreshTokenApplication(__refresh_domain)
    refresh_service = AuthService(__user_application, __refresh_application)

services = GetServices()
        
        



