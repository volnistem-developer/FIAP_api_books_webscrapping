class AppException(Exception):
    status_code = 500
    message = "Deu erro aqui oh"

    def __init__(self, message=None):
        if message:
            self.message = message


class BusinessException(AppException):
    status_code = 400

class ForbiddenException(AppException):
    status_code = 403


class ConflictException(AppException):
    status_code = 409


class NotFoundException(AppException):
    status_code = 404

class InvalidCredentialsException(AppException):
    status_code = 400

class InfraException(AppException):
    status_code = 500
