"""
Tools endpoint module for the Identory API.

This module provides methods to interact with the Identory Tools API endpoints.
"""

from typing import Dict, Any

TOOLS_ENDPOINT = "/api/v1/tools"


class ToolsMixin:
    def check_proxy(self, proxy_host: str, proxy_port: int, proxy_type: str = "http://", username: str = None, password: str = None) -> Dict[str, Any]:
        """
        Check proxy connection and get proxy information.
        
        Args:
            proxy_host (str): Proxy server hostname or IP address
            proxy_port (int): Proxy server port
            proxy_type (str): Type of proxy ("http://", "socks://", "ssh://") (default: "http://")
            username (str, optional): Proxy username if authentication required
            password (str, optional): Proxy password if authentication required
            
        Returns:
            Dict[str, Any]: Response containing proxy check results
            
        Example:
            >>> client = IdentoryAPI(api_key="your-key")
            >>> ip_info = client.get_ip_info("proxy.example.com", 8080, "http://", "user", "pass")
            >>> print(ip_info)
        """
        data = {
            "proxyType": proxy_type,
            "proxyHost": proxy_host,
            "proxyPort": proxy_port
        }
        if username:
            data["proxyUsername"] = username
        if password:
            data["proxyPassword"] = password
            
        return self.post(f"{TOOLS_ENDPOINT}/check-proxy", data=data)
    
    def get_ip_info(self, proxy_host: str, proxy_port: int, proxy_type: str = "http://", username: str = None, password: str = None) -> Dict[str, Any]:
        """
        Get proxy IP information.
        
        Args:
            proxy_host (str): Proxy server hostname or IP address
            proxy_port (int): Proxy server port
            proxy_type (str): Type of proxy ("http://", "socks://", "ssh://") (default: "http://")
            username (str, optional): Proxy username if authentication required
            password (str, optional): Proxy password if authentication required
            
        Returns:
            Dict[str, Any]: Response containing proxy IP information like country, city, timezone, etc.
            
        Example:
            >>> client = IdentoryAPI(api_key="your-key")
            >>> result = client.get_ip_info("proxy.example.com", 8080, "http://", "user", "pass")
            >>> print(result)
        """
        data = {
            "host": proxy_host,
            "port": proxy_port,
            "type": proxy_type
        }
        
        if username:
            data["username"] = username
        if password:
            data["password"] = password
            
        return self.post(f"{TOOLS_ENDPOINT}/get-ip-info", data=data)