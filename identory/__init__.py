"""
Identory API Python Wrapper

A Python wrapper for the Identory API.
"""

from .client import IdentoryWrapper
from .exceptions import APIError, AuthenticationError, NotFoundError, RateLimitError

__version__ = "0.1.5"
__author__ = "Okoya Usman"
__email__ = "usmanokoya10@gmail.com"
__all__ = [
    "IdentoryWrapper",
    "APIError", 
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
]