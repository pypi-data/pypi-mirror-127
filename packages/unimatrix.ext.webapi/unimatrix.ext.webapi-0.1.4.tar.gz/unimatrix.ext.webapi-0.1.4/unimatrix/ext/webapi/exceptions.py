"""Declares common exceptions classes."""
from unimatrix.ext.model.exc import CanonicalException


class AuthenticationRequired(CanonicalException):
    """Raised when an operation required authenticated requests."""
    code = 'AUTHENTICATION_REQUIRED'
    http_status_code = 401
    message = "The operation requires authenticated requests."
    detail = (
        "An operation against a protected resource was attempted and it does "
        "not allow interactions with unauthenticated requests."
    )


class BearerAuthenticationRequired(AuthenticationRequired):
    hint = "Provide valid credentials using the Authorization header."


class UpstreamServiceNotAvailable(CanonicalException):
    """Raised when the application is not able to establish
    a (network) connection to an upstream service.
    """
    code = 'SERVICE_NOT_AVAILABLE'
    http_status_code = 503
    message = "The service is currently not available."
    detail = (
        "Network or other infrastructure issues prevent "
        "proper operation of the service."
    )
    hint = "Try again in 600 seconds."


class UpstreamConnectionFailure(UpstreamServiceNotAvailable):
    """Raised when an upstream service listens at the configured address
    and port, but there are issued in establish the connection according
    to the agreed protocol. Such errors may occur when, for example, the
    upstream service is booting and has bound to its address and port, but
    is not yet ready to serve.
    """
    hint = "Try again in 10 seconds."
