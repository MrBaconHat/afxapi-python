class FXAPIError(Exception):
    """Base error for all FXAPI related exceptions."""
    pass

class QuotaExceeded(FXAPIError):
    pass

class AuthenticationFailed(FXAPIError):
    pass

class RateLimited(FXAPIError):
    pass

class InvalidRequest(FXAPIError):
    pass

class Forbidden(FXAPIError):
    pass

class InternalServerError(FXAPIError):
    pass

class NotFound(FXAPIError):
    pass

class ValidationError(FXAPIError):
    pass