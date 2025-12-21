class BookScrapingApiError(Exception):
    
    def __init__(self, message: str = "Service is unavailable", name: str = "BookScrapingAPI"):
        self.message = message
        self.name   = name
        super().__init__(self.message, self.name)

class ServiceError(BookScrapingApiError): pass

class EntityDoesNotExistsError(BookScrapingApiError): pass

class DataError(BookScrapingApiError): pass

class IntegrityError(BookScrapingApiError): pass

class EntityAlreadyExistsError(BookScrapingApiError): pass

class InvalidOperationError(BookScrapingApiError): pass

class AuthenticationFailedError(BookScrapingApiError): pass

class InvalidTokenError(BookScrapingApiError): pass

class UnauthorizedError(BookScrapingApiError): pass

class ForbiddenError(BookScrapingApiError): pass
