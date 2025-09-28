"""
Settings endpoint module for the Identory API.

This module provides methods to interact with the Identory Settings API endpoints.
"""

from typing import Dict, Any

SETTINGS_ENDPOINT = "/api/v1/settings"


class SettingsMixin:
    def get_default_settings(self) -> Dict[str, Any]:
        """
        Get default profile settings.

        Returns:
            Dict[str, Any]: Response containing default profile settings.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> settings = client.get_default_settings()
            >>> print(settings)
        """
        return self.get(f"{SETTINGS_ENDPOINT}/default-profile")
    
    def set_default_settings(self, **settings_data) -> Dict[str, Any]:
        """
        Set default profile settings.
        
        Args:
            **settings_data: Settings data fields to update according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/cdtq440d1k6sk1fsu4ug/presets-api-endpoint?currentPageId=cdtqhj0d1k6sk1fsu5c0
            
        Returns:
            Dict[str, Any]: Updated default profile settings data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> settings = client.update_settings(autoStartProfiles=False, maxConcurrentProfiles=5)
        """
        data = {
            **settings_data
        }

        return self.put(f"{SETTINGS_ENDPOINT}/default-profile", data=data)