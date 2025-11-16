import os
import json
import platform
import requests
import subprocess
from typing import Dict, Any, Optional
from requests.adapters import HTTPAdapter
from .tools import ToolsMixin
from .status import StatusMixin
from .groups import GroupsMixin
from .presets import PresetsMixin
from .profiles import ProfilesMixin
from .settings import SettingsMixin
from .exceptions import (
    APIError, 
    AuthenticationError, 
    NotFoundError, 
    RateLimitError,
    ValidationError
)

class IdentoryWrapper(ProfilesMixin, SettingsMixin, ToolsMixin, StatusMixin, GroupsMixin, PresetsMixin):
    """
    Client for interacting with the Identory API.
    
    This client provides methods to interact with various endpoints
    of the Identory API using access token authentication.
    
    Args:
        access_token (str): Your Identory access token, mandatory if auto_launch is True.
        auto_launch (bool, optional): Whether to auto-launch the Identory CLI. Defaults to False.
        base_url (str, optional): Base URL for the API. Defaults to production.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
    """
    
    def __init__(self, access_token: Optional[str] = None, auto_launch: bool = False, base_url: str = "http://127.0.0.1", port: int = 3005, timeout: int = 30):
        self.access_token = access_token
        self.port = port
        self.base_url = f"{base_url.rstrip('/')}:{port}"
        self.timeout = timeout
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(pool_maxsize=100))
        self.session.mount('https://', HTTPAdapter(pool_maxsize=100))
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': '`Identory-Python-Wrapper/0.1.5'
        })
        if auto_launch:
            if not access_token:
                raise ValueError("Access token is required")
            self._launch_cli()
    
    def _request(self, method: str, endpoint: str, data: dict = None, **kwargs) -> Dict[str, Any]:
        """
        Make a request to the API.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint (str): API endpoint path (e.g., '/profiles')
            data (dict, optional): Form data
            **kwargs: Additional arguments passed to requests
            
        Returns:
            Dict[str, Any]: JSON response data
            
        Raises:
            APIError: For various API-related errors
            requests.RequestException: For network-related errors
        """
        url = f"{self.base_url}{endpoint}"
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout

        body = json.dumps(data) if data else None
        try:
            response = self.session.request(method, url, data=body, **kwargs)
            
            # Handle different status codes
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 201:
                return response.json()
            elif response.status_code == 204:
                return {}
            elif response.status_code == 401:
                raise AuthenticationError("Invalid API key or authentication failed")
            elif response.status_code == 404:
                raise NotFoundError("Resource not found")
            elif response.status_code == 422:
                error_data = response.json() if response.content else {}
                raise ValidationError("Request validation failed", error_data)
            elif response.status_code == 429:
                raise RateLimitError("Rate limit exceeded. Please try again later.")
            else:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', f'HTTP {response.status_code}')
                except:
                    error_message = f'HTTP {response.status_code}: {response.text}'
                raise APIError(error_message, response.status_code)
                
        except requests.exceptions.Timeout:
            raise APIError("Request timed out")
        except requests.exceptions.ConnectionError:
            raise APIError("Connection error - please check your internet connection")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
    
    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """
        Make a GET request to the API.
        
        Args:
            endpoint (str): API endpoint path
            params (dict, optional): Query parameters
            **kwargs: Additional arguments passed to requests
            
        Returns:
            Dict[str, Any]: JSON response data
        """
        return self._request('GET', endpoint, params=params, **kwargs)
    
    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """
        Make a POST request to the API.
        
        Args:
            endpoint (str): API endpoint path
            data (dict, optional): Form data
            json (dict, optional): JSON data
            **kwargs: Additional arguments passed to requests
            
        Returns:
            Dict[str, Any]: JSON response data
        """
        return self._request('POST', endpoint, data=data, json=json, **kwargs)
    
    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """
        Make a PUT request to the API.
        
        Args:
            endpoint (str): API endpoint path
            data (dict, optional): Form data
            json (dict, optional): JSON data
            **kwargs: Additional arguments passed to requests
            
        Returns:
            Dict[str, Any]: JSON response data
        """
        return self._request('PUT', endpoint, data=data, json=json, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make a DELETE request to the API.
        
        Args:
            endpoint (str): API endpoint path
            **kwargs: Additional arguments passed to requests
            
        Returns:
            Dict[str, Any]: JSON response data
        """
        return self._request('DELETE', endpoint, **kwargs)

    def _launch_cli(self):
        system = platform.system()
        if system == "Windows":
            exe_path = os.path.expandvars(r"%userprofile%\AppData\Local\Programs\identory\identory.exe")
            cmd = [
                exe_path,
                "serve",
                f"--access-token={self.access_token}",
                f"--port={self.port}"
            ]
        elif system == "Linux":
            cmd = [
                "identory",
                "serve",
                f"--access-token={self.access_token}",
                f"--port={self.port}"
            ]
        elif system == "Darwin":
            exe_path = "/Applications/IDENTORY.app/Contents/MacOS/IDENTORY"
            cmd = [
                exe_path,
                "serve",
                f"--access-token={self.access_token}",
                f"--port={self.port}"
            ]
        else:
            raise RuntimeError(f"Unsupported operating system: {system}")
        try:
            process = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Identory started on port {self.port} (PID: {process.pid})")
            return process
        except FileNotFoundError:
            print("Identory executable not found. Please check installation.")
        except Exception as e:
            print(f"Failed to start Identory: {e}")