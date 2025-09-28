"""
Groups endpoint module for the Identory API.

This module provides methods to interact with the Identory Groups API endpoints.
"""

from typing import Dict, Any

GROUPS_ENDPOINT = "/api/v1/groups"


class GroupsMixin:
    def get_groups(self) -> Dict[str, Any]:
        """
        Retrieve a list of all groups.

        Returns:
            Dict[str, Any]: Response containing list of groups with id, name, etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> groups = client.get_groups()
            >>> for group in groups:
            ...     print(f"Group: {group['name']}")
        """
        return self.get(GROUPS_ENDPOINT)
    
    def get_group(self, group_id: str) -> Dict[str, Any]:
        """
        Retrieve a specific group by ID.
        
        Args:
            group_id (str): The unique identifier of the group
            
        Returns:
            Dict[str, Any]: Group data including id, name, etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> group = client.get_group("00000000-0000-0000-0000-000000000000")
            >>> print(group)
        """
        return self.get(f"{GROUPS_ENDPOINT}/{group_id}")
    
    def create_group(self, name: str, color: str = None) -> Dict[str, Any]:
        """
        Create a new group.
        
        Args:
            name (str): Name of the group (required)
            color (str, optional): Color of the group. Can be:
                - Predefined colors: 'secondary', 'primary', 'success', 'danger', 'warning', 'info'
                - Custom hex color: '#000000' format
                - None for default color
            
        Returns:
            Dict[str, Any]: Created group data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> group = client.create_group("New group", "#000")
            >>> print(group)
        """
        data = {"name": name}
        
        if color is not None:
            data["color"] = color
            
        return self.post(GROUPS_ENDPOINT, data=data)
    
    def update_group(self, group_id: str, name: str = None, color: str = None) -> Dict[str, Any]:
        """
        Update an existing group.
        
        Args:
            group_id (str): The unique identifier of the group
            name (str, optional): New name for the group
            color (str, optional): New color for the group. Can be:
                - Predefined colors: 'secondary', 'primary', 'success', 'danger', 'warning', 'info'
                - Custom hex color: '#000000' format
                - None to remove color
            
        Returns:
            Dict[str, Any]: Updated group data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> group = client.update_group("00000000-0000-0000-0000-000000000000", name="Updated Group", color="success")
        """
        data = {}
        
        if name is not None:
            data["name"] = name
        if color is not None:
            data["color"] = color
            
        return self.put(f"{GROUPS_ENDPOINT}/{group_id}", data=data)
    
    def delete_group(self, group_id: str) -> Dict[str, Any]:
        """
        Delete a group.
        
        Args:
            group_id (str): The unique identifier of the group
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> client.delete_group("00000000-0000-0000-0000-000000000000")
        """
        return self.delete(f"{GROUPS_ENDPOINT}/{group_id}")