from afxapicom.client import Client
from afxapicom.errors import (
    FXAPIError,
    AuthenticationFailed,
    RateLimited,
    QuotaExceeded,
    Forbidden,
    NotFound,
    ValidationError,
    InternalServerError,
    InvalidRequest,
)

__version__ = "0.1.0"
__all__ = [
    "Client",
    "FXAPIError",
    "AuthenticationFailed",
    "RateLimited",
    "QuotaExceeded",
    "Forbidden",
    "NotFound",
    "ValidationError",
    "InternalServerError",
    "InvalidRequest",
]
