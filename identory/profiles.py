"""
Profiles endpoint module for the Identory API.

This module provides methods to interact with the Identory Profiles API endpoints,
including profile management, creation, updates, and deletion operations.
"""

from typing import Dict, Any, List

PROFILES_ENDPOINT = "/api/v1/profiles"


class ProfilesMixin:
    def get_profiles(self) -> Dict[str, Any]:
        """
        Retrieve a list of all profiles.

        Returns:
            Dict[str, Any]: Response containing profiles list.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> profiles = client.get_profiles()
            >>> for profile in profiles:
            ...     print(profile["name"])
        """
        return self.get(PROFILES_ENDPOINT)
    
    def get_profile(self, profile_id: str) -> Dict[str, Any]:
        """
        Retrieve a specific profile by ID.
        
        Args:
            profile_id (str): The unique identifier of the profile
            
        Returns:
            Dict[str, Any]: Profile data including id, name, status, etc.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> profile = client.get_profile("123")
            >>> print(profile["name"])
        """
        return self.get(f"{PROFILES_ENDPOINT}/{profile_id}")
    
    def create_profile(self, name: str, **profile_data) -> Dict[str, Any]:
        """
        Create a new profile.
        
        Args:
            name (str): Profile's full name
            **profile_data: Additional profile data fields according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/c6plui8d1k6up4kmfa4g/profiles-api-endpoint.
            
        Returns:
            Dict[str, Any]: Created profile data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> profile = client.create_profile(name="Test Browser")
        """
        data = {
            "name": name,
            **profile_data
        }
        
        return self.post(PROFILES_ENDPOINT, data=data)
    
    def update_profile(self, profile_id: str, **profile_data) -> Dict[str, Any]:
        """
        Update an existing profile.
        
        Args:
            profile_id (str): The unique identifier of the profile
            **profile_data: Profile data fields to update according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/c6plui8d1k6up4kmfa4g/profiles-api-endpoint.
            
        Returns:
            Dict[str, Any]: Updated profile data
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> profile = client.update_profile("00000000-0000-0000-0000-000000000000", name="Jane Doe", timezone="UTC")
        """
        return self.put(f"{PROFILES_ENDPOINT}/{profile_id}", data=profile_data)
    
    def delete_profile(self, profile_id: str) -> Dict[str, Any]:
        """
        Delete a profile.
        
        Args:
            profile_id (str): The unique identifier of the profile
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> client.delete_profile("00000000-0000-0000-0000-000000000000")
        """
        return self.delete(f"{PROFILES_ENDPOINT}/{profile_id}")
    
    def delete_profiles(self, profile_ids: List[str]) -> Dict[str, Any]:
        """
        Delete multiple profiles.
        
        Args:
            profile_ids (List[str]): A list of profile IDs to delete
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> client.delete_profiles(["00000000-0000-0000-0000-000000000000", "00000000-0000-0000-0000-000000000001"])
        """
        data = {
            "profileIds": profile_ids
        }
        
        return self.delete(PROFILES_ENDPOINT, data=data)
    
    def start_profile(self, profile_id: str, headless: bool = False, skipConnectionCheck: bool = False, changeIP: bool = False, enableDebugger: bool = False, **browserOptions) -> Dict[str, Any]:
        """
        Start a profile.
        
        Args:
            profile_id (str): The unique identifier of the profile
            headless (bool): Whether to run the browser in headless mode (default: False)
            skipConnectionCheck (bool): Whether to skip the connection check (default: False)
            changeIP (bool): Whether to change the IP address (default: False)
            enableDebugger (bool): Whether to enable the debugger (default: False)
            **browserOptions: Additional browser options according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/c6plui8d1k6up4kmfa4g/profiles-api-endpoint.
        Returns:
            Dict[str, Any]: Response containing the started profile
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.start_profile("00000000-0000-0000-0000-000000000000")
            >>> print(result["browserWSEndpoint"])
        """
        data = {
            "headless": headless,
            "skipConnectionCheck": skipConnectionCheck,
            "changeIP": changeIP,
            "enableDebugger": enableDebugger,
            **browserOptions
        }
        
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/start", data=data)
    
    def stop_profile(self, profile_id: str) -> Dict[str, Any]:
        """
        Stop a profile.
        
        Args:
            profile_id (str): The unique identifier of the profile
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.stop_profile("00000000-0000-0000-0000-000000000000")
        """
        data = {
            "profile_id": profile_id
        }
        
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/stop", data=data)
    
    def get_running_profiles(self) -> Dict[str, Any]:
        """
        Retrieve a list of all running profiles.

        Returns:
            Dict[str, Any]: Response containing running profiles list.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> profiles = client.get_running_profiles()
            >>> for profile in profiles:
            ...     print(profile["id"])
        """
        return self.get(f"{PROFILES_ENDPOINT}/running")

    def get_profile_status(self, profile_id: str) -> Dict[str, Any]:
        """
        Retrieve the status of a specific profile by ID.
        
        Args:
            profile_id (str): The unique identifier of the profile
            
        Returns:
            Dict[str, Any]: Profile data including status.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> profile = client.get_profile_status("00000000-0000-0000-0000-000000000000")
            >>> print(profile["status"])
        """
        return self.get(f"{PROFILES_ENDPOINT}/{profile_id}/status")

    def change_profile_ip(self, profile_id: str) -> Dict[str, Any]:
        """
        Change the IP address of a profile.
        
        Args:
            profile_id (str): The unique identifier of the profile
            
        Returns:
            Dict[str, Any]: Empty response on success
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.change_profile_ip("00000000-0000-0000-0000-000000000000")
        """
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/change-ip")

    def import_profile(self, file_path: str, overwrite: dict = None) -> Dict[str, Any]:
        """
        Import a profile.
        
        Args:
            file_path (str): The path to the file to import
            overwrite (dict): Profile parameters that need to be overwritten after import, in the example below the profile name will be overwritten: {"name": "Test Browser"}
            
        Returns:
            Dict[str, Any]: Response containing the imported profile
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.import_profile("path/to/profile.zip")
        """
        data = {
            "filePath": file_path
        }
        if overwrite:
            data["overwrite"] = overwrite
        
        return self.post(f"{PROFILES_ENDPOINT}/import", data=data)

    def export_profile(self, profile_id: str, file_path: str) -> Dict[str, Any]:
        """
        Export a profile.
        
        Args:
            profile_id (str): The unique identifier of the profile
            file_path (str): The path to export the profile to
            
        Returns:
            Dict[str, Any]: Response containing the exported profile
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.export_profile("00000000-0000-0000-0000-000000000000", "path/to/profile.zip")
        """
        data = {
            "filePath": file_path
        }
        
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/export", data=data)

    def get_profile_cookies(self, profile_id: str) -> Dict[str, Any]:
        """
        Retrieve the cookies of a specific profile by ID.
        
        Args:
            profile_id (str): The unique identifier of the profile
            
        Returns:
            Dict[str, Any]: Cookies data.
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> cookies = client.get_profile_cookies("00000000-0000-0000-0000-000000000000")
            >>> print(cookies)
        """
        return self.get(f"{PROFILES_ENDPOINT}/{profile_id}/get-cookies")
    
    def export_profile_cookies(self, profile_id: str, file_path: str) -> Dict[str, Any]:
        """
        Export the cookies of a specific profile by ID.
        
        Args:
            profile_id (str): The unique identifier of the profile
            file_path (str): The path to export the profile to
            
        Returns:
            Dict[str, Any]: Response containing the exported cookies
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.export_profile_cookies("00000000-0000-0000-0000-000000000000", "path/to/cookies.json")
        """
        data = {
            "filePath": file_path
        }
        
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/export-cookies", data=data)
    
    def start_profile_warmup(self, profile_id: str, listOfUrls: list, settings: dict = None, skipConnectionCheck: bool = False, enableDebugger: bool = False) -> Dict[str, Any]:
        """
        Start a profile warmup.
        
        Args:
            profile_id (str): The unique identifier of the profile
            listOfUrls (list): List of sites to visit and/or Google search terms
            settings (dict): Settings for the warmup (according to https://docs.identory.com/s/c6nht0od1k6up4kmf9og/api-documentation-en/d/c6plui8d1k6up4kmfa4g/profiles-api-endpoint)
            skipConnectionCheck (bool): Whether to skip the connection check (default: False)
            enableDebugger (bool): Whether to enable the debugger (default: False)
        Returns:
            Dict[str, Any]: Response containing the started warmup
            
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.start_profile_warmup("00000000-0000-0000-0000-000000000000", ["https://www.google.com", "mountain" "https://www.youtube.com", "gemini"])
            >>> print(result["browserWSEndpoint"])
        """
        data = {
            "list": listOfUrls,
            "skipConnectionCheck": skipConnectionCheck,
            "enableDebugger": enableDebugger
        }
        if settings:
            data["settings"] = settings
        
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/warm-up", data=data)
        
    def human_typing(self, profile_id: str, text: str, frame: str = None) -> Dict[str, Any]:
        """
        Enters text as it would be entered by a real human, typing speed depends on the value of the parameter "avgWpm" set in the profile. Before sending a request, the element must be focused on the page.
        
        Args:
            profile_id (str): The unique identifier of the profile
            text (str): The text to enter
            frame (str): ID of a specific frame
            
        Returns:
            Dict[str, Any]: Empty response on success
        
        Example:
            >>> client = IdentoryWrapper(api_key="your-key")
            >>> result = client.human_typing("00000000-0000-0000-0000-000000000000", "Hello, world!")
        """
        data = {
            "text": text
        }
        if frame:
            data["frameId"] = frame
            
        return self.post(f"{PROFILES_ENDPOINT}/{profile_id}/human-typing", data=data)