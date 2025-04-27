# Before You Begin: Essential Setup 🛠️

Welcome to your Dataloop journey! Let's get your environment perfectly set up for success.

## Useful Resources 📚

Before diving into the setup, here are some helpful resources:

1. 🔍 [Dataloop Python SDK Cheat Sheet](https://docs.dataloop.ai/docs/sdk-cheatsheet) - Quick reference for SDK code examples
2. 💻 [Recommended Specifications](https://docs.dataloop.ai/docs/platform-recommended) - System requirements, supported browsers, and file formats
3. 🔑 [Sign Up](https://console.dataloop.ai) - Create your free Dataloop account
4. 📂 [Onboarding Files](https://github.com/dataloop-ai/dtlpy-documentation/tree/main/onboarding) - Access all onboarding exercise files
5. 📚 [In-depth SDK Documentation](https://sdk-docs.dataloop.ai/en/latest/entities.html) - Detailed SDK reference

## System Requirements 💻

### Hardware Requirements
- **CPU**: 2+ cores recommended
- **RAM**: 4GB minimum, 8GB+ recommended
- **Storage**: 1GB+ free space for SDK and dependencies
- **Internet**: Stable connection required

### Software Prerequisites
- **Operating System**: 
  - Windows 10/11
  - macOS 10.14+
  - Ubuntu 18.04+ or other modern Linux distributions
- **Python**: Version 3.6 or higher
- **pip**: Latest version recommended

## Python Environment Setup 🐍

### 1. Installing Python

```bash
# Check if Python is installed
python --version  # or python3 --version

# If not installed, download from:
# https://www.python.org/downloads/
```

> 💡 **Pro Tip**: Always check "Add Python to PATH" during Windows installation!

### 2. Setting Up a Virtual Environment

```bash
# Create a new virtual environment
python -m venv dataloop-env

# Activate the environment
# On Windows:
dataloop-env\Scripts\activate
# On macOS/Linux:
source dataloop-env/bin/activate
```

## SDK Installation Guide 📦

### 1. Basic Installation

```bash
# Install the Dataloop SDK
pip install dtlpy

# Verify installation
pip show dtlpy
```

### 2. Validation

```python
# Test your installation
import dtlpy as dl
print(dl.__version__)
```

## Environment Configuration ⚙️

### 1. Setting Up Environment Variables

```bash
# Windows
set DTLPY_API_KEY=your-api-key

# Linux/macOS
export DTLPY_API_KEY=your-api-key
```

### 2. Configuration File Setup

```python
import dtlpy as dl
# Create a default configuration
dl.login_api_key(api_key=os.environ['DTLPY_API_KEY'])

# Check if the configuration is successful
dl.projects.list().print()
```

## Best Practices & Tips 👑

### 1. Environment Management
- Always use virtual environments
- Keep dependencies updated
- Document your environment setup

### 2. Security Best Practices
```python
# DON'T: Hardcode credentials
api_key = "your-api-key"  # ❌

# DO: Use environment variables
import os
api_key = os.environ.get('DTLPY_API_KEY')  # ✅
```

Suggestion:  Use `python-dotenv` and `.env` files to load the API key easily:

```python
# Install python-dotenv
# pip install python-dotenv

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key securely
api_key = os.getenv('DTLPY_API_KEY')

# Initialize Dataloop with the API key
dl.login_api_key(api_key=api_key)
```

> 🔒 **Best Practices for .env Files**:
> 1. Create a `.env` file in your project root:
>    ```plaintext
>    DTLPY_API_KEY=your-api-key-here
>    ```
> 2. Add `.env` to your `.gitignore` file to prevent committing sensitive data
> 3. Create a `.env.example` file with dummy values as a template
> 4. Never commit real credentials to version control
> 5. Use strong, unique API keys
> 6. Regularly rotate your API keys
> 
> 📚 Learn more about environment variable best practices and python dotenv [here]](https://github.com/theskumar/python-dotenv?tab=readme-ov-file)

### 3. Installation Troubleshooting

Common issues and solutions:

1. **SSL Certificate Errors**
   ```bash
   # Temporary fix
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org dtlpy
   ```

2. **Dependency Conflicts**
   ```bash
   # Clean installation
   pip uninstall dtlpy
   pip cache purge
   pip install dtlpy
   ```

3. **Version Mismatch**
   ```bash
   # Force specific version
   pip install dtlpy==x.y.z
   ```

## Validation Checklist ✅

Before proceeding, ensure:

- [ ] Python version between 3.8 and 3.12 is installed
- [ ] Virtual environment is created and activated
- [ ] Dataloop SDK is installed
- [ ] Installation is verified
- [ ] Environment variables are set
- [ ] Test import is successful

## Next Steps 🎯

Once your environment is ready:
1. Configure your credentials
2. Create your first project
3. Start exploring Dataloop's features

> 🔍 **Need Help?** Check our [troubleshooting guide](https://docs.dataloop.ai/docs/troubleshooting)

## Pro Tips 💡

1. **IDE Integration**
   - Use VS Code or PyCharm for better development experience
   - Install Python extensions for code completion

2. **Development Workflow**
   ```python
   import dtlpy as dl
   # Enable debug logging
   dl.verbose.logging_level = "DEBUG"

   ```

3. **Resource Management**
   ```python
   # Always clean up resources
   try:
       # Your code here
   finally:
       dl.logout()
   ```

Ready to start your Dataloop journey? Let's move on to authentication and project setup! 🚀 