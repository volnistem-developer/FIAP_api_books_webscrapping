from src.anticorruption.books_scrape_script import AnticorruptionBooksScraping
from src.api.service.auth_service import AuthService
from src.api.service.book_service import BookService
from src.api.service.category_service import CategoryService
from src.api.service.scrap_service import ScrapService
from src.api.service.stats_service import StatsService
from src.api.service.user_service import UserService
from src.application.book_application import BookApplication
from src.application.category_application import CategoryApplication
from src.application.refresh_token_application import RefreshTokenApplication
from src.application.scrap_application import ScrapApplication
from src.application.stats_application import StatsApplication
from src.application.user_application import UserApplication
from src.data.database.unity_of_work import UnityOfWork
from src.domain.book_domain import BookDomain
from src.domain.category_domain import CategoryDomain
from src.domain.refresh_token_domain import RefreshTokenDomain
from src.domain.scrap_domain import ScrapDomain
from src.domain.stats_domain import StatsDomain
from src.domain.user_domain import UserDomain
from src.infraestrutura.repository.book_repository import BookRepository
from src.infraestrutura.repository.category_repository import CategoryRepository
from src.infraestrutura.repository.refresh_token_repository import RefreshTokenRepository
from src.infraestrutura.repository.scrap_repository import ScrapRepository
from src.infraestrutura.repository.user_repository import UserRepository 

class GetServices():

    def user_service(self):
        uow = UnityOfWork()

        user_repository = UserRepository(uow)
        user_domain = UserDomain(user_repository)
        user_application = UserApplication(user_domain)

        return UserService(user_application), uow
    
    def auth_service(self):
        uow = UnityOfWork()

        user_repository = UserRepository(uow)
        refresh_repository = RefreshTokenRepository(uow)

        user_domain = UserDomain(user_repository)
        refresh_domain = RefreshTokenDomain(refresh_repository)

        user_application = UserApplication(user_domain)
        refresh_application = RefreshTokenApplication(refresh_domain)

        return AuthService(user_application, refresh_application), uow
    
    def get_scrap_service(self):
        repository = ScrapRepository()
        domain = ScrapDomain(repository)

        scraper = AnticorruptionBooksScraping()
        application = ScrapApplication(domain, scraper)

        return ScrapService(application)

    def book_service(self):
        uow = UnityOfWork()

        book_repository = BookRepository(uow)
        book_domain = BookDomain(book_repository)
        book_application = BookApplication(book_domain)

        return BookService(book_application)
    
    def category_service(self):
        uow = UnityOfWork()

        category_repository = CategoryRepository(uow)
        category_domain = CategoryDomain(category_repository)
        category_application = CategoryApplication(category_domain)

        return CategoryService(category_application)
    
    def get_stats_service(self):
        uow = UnityOfWork()

        book_repo = BookRepository(uow)
        scrap_repo = ScrapRepository()

        domain = StatsDomain(book_repo, scrap_repo)
        application = StatsApplication(domain, uow)
        
        return StatsService(application)

services = GetServices()
        
        



