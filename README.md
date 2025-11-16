# Identory Python Wrapper

[![PyPI version](https://badge.fury.io/py/identory.svg)](https://badge.fury.io/py/identory)
[![Python Support](https://img.shields.io/pypi/pyversions/identory.svg)](https://pypi.org/project/identory/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python wrapper for the Identory browser automation platform. This library provides a simple and intuitive interface for interacting with Identory's API endpoints, including profile management, settings configuration, tools, status management, groups, and presets.

## 🚀 Features

- **Complete API Coverage** - Full support for all Identory API endpoints
- **Playwright Compatibility** - Works perfectly with Playwright CDP.
- **Type Safety** - Comprehensive type hints for better IDE support
- **Error Handling** - Custom exceptions with detailed error messages
- **Auto-Launch** - Automatically starts the Identory CLI service
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Easy to Use** - Simple, intuitive API design
- **Well Documented** - Extensive documentation and examples

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install identory
```

### From Source

```bash
git clone https://github.com/okoyausman/identory-python-wrapper.git
cd identory-python-wrapper
pip install -e .
```

## 🏁 Quick Start

```python
from identory import IdentoryWrapper

# Initialize the client (this will auto-launch Identory CLI)
client = IdentoryWrapper(access_token="your-access-token", auto_launch=True)

# Get all profiles
profiles = client.get_profiles()
print(f"Found {len(profiles)} profiles")

# Create a new profile
profile = client.create_profile("My Browser Profile")
print(f"Created profile: {profile['name']}")

# Start a profile
result = client.start_profile(profile['id'], headless=False)
print(f"Profile started with WebSocket: {result['browserWSEndpoint']}")

# Connect with Playwright-python (optional)
import asyncio
from playwright.async_api import async_playwright

async def quick_automation():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.connect_over_cdp(result['browserWSEndpoint'])
    context = browser.contexts[0] if browser.contexts else await browser.new_context()
    page = context.pages[0] if context.pages else await context.new_page()
    await page.goto('https://example.com')
    await browser.close()
    client.stop_profile(profile['id'])

# Run automation
asyncio.run(quick_automation())
```

## 📚 API Reference

### Client Initialization

```python
from identory import IdentoryWrapper

client = IdentoryWrapper(
    access_token="your-access-token",
    auto_launch=True, #Default True to auto launch CLI, set False if you handled it in your app
    base_url="http://127.0.0.1",  # Default localhost
    port=3005,                    # Default port
    timeout=30                    # Default timeout
)
```

### Profile Management

```python
# Get all profiles
profiles = client.get_profiles()

# Get specific profile
profile = client.get_profile("profile-id")

# Create a new profile
profile = client.create_profile(
    name="Test Browser",
    timezone="UTC",
    platform="Win32"
)

# Update a profile
updated_profile = client.update_profile(
    "profile-id", 
    name="Updated Name",
    timezone="America/New_York"
)

# Start a profile
result = client.start_profile(
    "profile-id",
    headless=False,
    skipConnectionCheck=False,
    changeIP=True
)

# Stop a profile
client.stop_profile("profile-id")

# Get running profiles
running = client.get_running_profiles()

# Get profile status
status = client.get_profile_status("profile-id")

# Change profile IP
client.change_profile_ip("profile-id")

# Import/Export profiles
client.import_profile("path/to/profile.zip", {"name": "Imported Profile"})
client.export_profile("profile-id", "path/to/export.zip")

# Cookie management
cookies = client.get_profile_cookies("profile-id")
client.export_profile_cookies("profile-id", "cookies.json")

# Profile warmup
client.start_profile_warmup(
    "profile-id",
    ["https://www.google.com", "mountain", "https://www.youtube.com"],
    skipConnectionCheck=False
)

# Human typing
client.human_typing("profile-id", "Hello, world!")

# Delete profiles
client.delete_profile("profile-id")
client.delete_profiles(["id1", "id2"])
```

### Settings Management

```python
# Get default settings
settings = client.get_default_settings()

# Set default settings
client.set_default_settings(
    autoStartProfiles=False,
    maxConcurrentProfiles=5
)
```

### Tools & Utilities

```python
# Check proxy connection
proxy_result = client.check_proxy(
    "proxy.example.com", 
    8080, 
    "http://", 
    "username", 
    "password"
)

# Get IP information
ip_info = client.get_ip_info(
    "proxy.example.com",
    8080,
    "socks5://",
    "username",
    "password"
)
```

### Status Management

```python
# Get all statuses
statuses = client.get_statuses()

# Create a status
status = client.create_status("In Progress", "primary")

# Update a status
client.update_status("status-id", name="Completed", color="success")

# Delete a status
client.delete_status("status-id")
```

### Group Management

```python
# Get all groups
groups = client.get_groups()

# Create a group
group = client.create_group("Work Group", "blue")

# Update a group
client.update_group("group-id", name="Updated Group", color="green")

# Delete a group
client.delete_group("group-id")
```

### Preset Management

```python
# Get all presets
presets = client.get_presets()

# Create a preset with proxy
preset = client.create_preset(
    "Proxy Preset",
    useProxy=2,
    proxyType="socks5://",
    proxyHost="127.0.0.1",
    proxyPort="5000",
    proxyUsername="user",
    proxyPassword="pass"
)

# Create a preset with screen size
preset = client.create_preset(
    "Desktop Preset",
    screenSize="1920x1080",
    platform="Win32",
    platformVersionLimit=2
)

# Update a preset
client.update_preset("preset-id", proxyHost="new.proxy.com")

# Delete a preset
client.delete_preset("preset-id")
```

## 🔧 Configuration

### Access Token

You need a valid Identory access token to use this wrapper. You can obtain one from your Identory dashboard.

### Auto-Launch Behavior

The wrapper automatically attempts to launch the Identory CLI service when initialized. It supports:

- **Windows**: `%userprofile%\AppData\Local\Programs\identory\identory.exe`
- **macOS**: `/Applications/IDENTORY.app/Contents/MacOS/IDENTORY`
- **Linux**: `identory` (must be in PATH)

## 🛠️ Advanced Usage

### Playwright Integration

The Identory wrapper works seamlessly with Playwright for browser automation. Here's how to connect Playwright to an Identory profile:

```python
import asyncio
from identory import IdentoryWrapper
from playwright.async_api import async_playwright

async def browser_automation():
    # Initialize Identory client
    client = IdentoryWrapper()
    
    # Start a profile
    start_response = client.start_profile(
        "your-profile-id",
        headless=False
    )
    
    # Connect Playwright to the profile
    playwright = await async_playwright().start()
    browser = await playwright.chromium.connect_over_cdp(result['browserWSEndpoint'])
    
    # Get a new page
    context = browser.contexts[0] if browser.contexts else await browser.new_context()
    page = context.pages[0] if context.pages else await context.new_page()
    
    # Navigate to a website
    await page.goto('https://example.com', timeout=30000)
    
    # Perform actions
    await page.keyboard.type('input[name="username"]', 'random-username')
    await page.keyboard.type('input[name="passwd"]', 'random-password')
    await page.click('button[type="submit"]')
    
    # Take a screenshot
    await page.screenshot(path='webpage.png')
    
    # Close browser
    await browser.close()
    
    # Stop the profile
    client.stop_profile("your-profile-id")

# Run the automation
asyncio.run(browser_automation())
```

### Error Handling

```python
from identory import IdentoryWrapper, APIError, AuthenticationError, NotFoundError

try:
    profile = client.get_profile("invalid-id")
except NotFoundError:
    print("Profile not found")
except AuthenticationError:
    print("Invalid access token")
except APIError as e:
    print(f"API Error: {e}")
```

### Working with Profiles and Presets

```python
# Create a profile from a preset
preset = client.get_preset("preset-id")
profile = client.create_profile(
    name="Profile from Preset",
    **preset  # Apply preset settings
)

# Bulk operations
profile_ids = ["id1", "id2", "id3"]
client.delete_profiles(profile_ids)
```

### Custom Screen Sizes

```python
# Create preset with custom screen size
preset = client.create_preset(
    "Custom Screen",
    hasCustomScreenSize=True,
    customScreenWidth=1366,
    customScreenHeight=768
)
```

### Mobile Profiles

```python
# Create mobile preset
mobile_preset = client.create_preset(
    "Mobile Safari",
    platform="iPhone",
    mobileBrowser="SAFARI"
)
```

## 🐛 Troubleshooting

### Common Issues

1. **Identory CLI not found**
   ```
   Solution: Ensure Identory is properly installed and accessible
   ```

2. **Connection refused**
   ```
   Solution: Check if the port is available and Identory is running
   ```

3. **Authentication failed**
   ```
   Solution: Verify your access token is valid and not expired
   ```

4. **Profile not found**
   ```
   Solution: Ensure the profile ID exists and you have access to it
   ```

## 📋 Requirements

- Python 3.8+
- Identory application installed
- Valid Identory access token

### Optional Dependencies

For browser automation with Playwright:

```bash
pip install playwright
playwright install
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Identory Official Website](https://identory.com)
- [Identory Documentation](https://docs.identory.com)
- [PyPI Package](https://pypi.org/project/identory/)
- [GitHub Repository](https://github.com/okoyausman/identory-python-wrapper)

## 📞 Support

- **Documentation**: [https://docs.identory.com](https://docs.identory.com)
- **Issues**: [GitHub Issues](https://github.com/okoyausman/identory-python-wrapper/issues)
- **Email**: usmanokoya10@gmail.com

---

**Made with ❤️ for the Identory community**