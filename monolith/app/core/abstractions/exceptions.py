class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists."""
    pass

class UserNotFoundError(Exception):
    """Raised when a user cannot be found."""
    pass


class UserDoesNotExistsError(Exception):
    """Raised when a user does not exists"""
    pass

class InvalidCredentials(Exception):
    """Raised when a user entered invalid credentials"""
    pass
