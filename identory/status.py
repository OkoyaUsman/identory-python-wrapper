"""
Status endpoint module for the Identory API.

This module provides methods to interact with the Identory Statuses API endpoints
"""

from typing import Dict, Any

STATUS_ENDPOINT = "/api/v1/statuses"


class StatusMixin:
    def get_statuses(self) -> Dict[str, Any]:
        """
        Retrieve a list of all statuses.

        Returns:
            Dict[str, Any]: Response containing list of statuses with id, name, etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> statuses = client.get_statuses()
            >>> for status in statuses:
            ...     print(f"Status: {status['name']}")
        """
        return self.get(STATUS_ENDPOINT)
    
    def get_status(self, status_id: str) -> Dict[str, Any]:
        """
        Retrieve a specific status by ID.
        
        Args:
            status_id (str): The unique identifier of the status
            
        Returns:
            Dict[str, Any]: Status data including id, name etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> status = client.get_status("00000000-0000-0000-0000-000000000000")
            >>> print(status)
        """
        return self.get(f"{STATUS_ENDPOINT}/{status_id}")
    
    def create_status(self, name: str, color: str = None) -> Dict[str, Any]:
        """
        Create a new status.
        
        Args:
            name (str): Name of the status (required)
            color (str, optional): Color of the status. Can be:
                - Predefined colors: 'secondary', 'primary', 'success', 'danger', 'warning', 'info'
                - Custom hex color: '#000000' format
                - None for default color
            
        Returns:
            Dict[str, Any]: Created status data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> status = client.create_status("New Status", "primary")
            >>> print(f"Created status: {status['name']} with color {status['color']}")
        """
        data = {"name": name}
        
        if color is not None:
            data["color"] = color
            
        return self.post(STATUS_ENDPOINT, data=data)
    
    def update_status(self, status_id: str, name: str = None, color: str = None) -> Dict[str, Any]:
        """
        Update an existing status.
        
        Args:
            status_id (str): The unique identifier of the status
            name (str, optional): New name for the status
            color (str, optional): New color for the status. Can be:
                - Predefined colors: 'secondary', 'primary', 'success', 'danger', 'warning', 'info'
                - Custom hex color: '#000000' format
                - None to remove color
            
        Returns:
            Dict[str, Any]: Updated status data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> status = client.update_status("00000000-0000-0000-0000-000000000000", name="Updated Status", color="success")
        """
        data = {}
        
        if name is not None:
            data["name"] = name
        if color is not None:
            data["color"] = color
            
        return self.put(f"{STATUS_ENDPOINT}/{status_id}", data=data)
    
    def delete_status(self, status_id: str) -> Dict[str, Any]:
        """
        Delete a status.
        
        Args:
            status_id (str): The unique identifier of the status
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> client.delete_status("00000000-0000-0000-0000-000000000000")
        """
        return self.delete(f"{STATUS_ENDPOINT}/{status_id}")