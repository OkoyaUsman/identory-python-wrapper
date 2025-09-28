"""
Presets endpoint module for the Identory API.

This module provides methods to interact with the Identory Presets API endpoints.
"""

from typing import Dict, Any

PRESETS_ENDPOINT = "/api/v1/presets"


class PresetsMixin:
    def get_presets(self) -> Dict[str, Any]:
        """
        Retrieve a list of all presets.

        Returns:
            Dict[str, Any]: Response containing list of presets with id, presetName, etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> presets = client.get_presets()
            >>> for preset in presets:
            ...     print(f"Preset: {preset['presetName']}")
        """
        return self.get(PRESETS_ENDPOINT)
    
    def get_preset(self, preset_id: str) -> Dict[str, Any]:
        """
        Retrieve a specific preset by ID.
        
        Args:
            preset_id (str): The unique identifier of the preset
            
        Returns:
            Dict[str, Any]: Preset data including id, presetName, etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> preset = client.get_preset("00000000-0000-0000-0000-000000000000")
            >>> print(preset)
        """
        return self.get(f"{PRESETS_ENDPOINT}/{preset_id}")
    
    def create_preset(self, preset_name: str, **kwargs) -> Dict[str, Any]:
        """
        Create a new preset.
        
        Args:
            preset_name (str): Name of the preset (required)
            **kwargs: Additional preset parameters according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/cdtq440d1k6sk1fsu4ug/presets-api-endpoint
            
        Returns:
            Dict[str, Any]: Created preset data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> preset = client.create_preset("New preset", useProxy=2, proxyType="socks5://", proxyHost="127.0.0.1")
        """
        data = {"presetName": preset_name}
        data.update(kwargs)
        return self.post(PRESETS_ENDPOINT, data=data)
    
    def update_preset(self, preset_id: str, **kwargs) -> Dict[str, Any]:
        """
        Update an existing preset.
        
        Args:
            preset_id (str): The unique identifier of the preset
            **kwargs: Preset parameters to update according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/cdtq440d1k6sk1fsu4ug/presets-api-endpoint
            
        Returns:
            Dict[str, Any]: Updated preset data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> preset = client.update_preset("00000000-0000-0000-0000-000000000000", proxyHost="new.proxy.com", proxyPort="8080")
        """
        return self.put(f"{PRESETS_ENDPOINT}/{preset_id}", data=kwargs)
    
    def delete_preset(self, preset_id: str) -> Dict[str, Any]:
        """
        Delete a preset.
        
        Args:
            preset_id (str): The unique identifier of the preset
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> client.delete_preset("00000000-0000-0000-0000-000000000000")
        """
        return self.delete(f"{PRESETS_ENDPOINT}/{preset_id}")