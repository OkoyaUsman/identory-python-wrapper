class APIError(Exception):
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}
        super().__init__(self.message)
    
    def __str__(self):
        if self.status_code:
            return f"API Error {self.status_code}: {self.message}"
        return f"API Error: {self.message}"

class AuthenticationError(APIError):
    def __init__(self, message: str = "Authentication failed", response_data: dict = None):
        super().__init__(message, 401, response_data)

class NotFoundError(APIError):
    def __init__(self, message: str = "Resource not found", response_data: dict = None):
        super().__init__(message, 404, response_data)

class RateLimitError(APIError):
    def __init__(self, message: str = "Rate limit exceeded", response_data: dict = None):
        super().__init__(message, 429, response_data)

class ValidationError(APIError):
    def __init__(self, message: str = "Validation error", response_data: dict = None):
        super().__init__(message, 422, response_data)