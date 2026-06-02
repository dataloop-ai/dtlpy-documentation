# Before You Begin: Essential Setup 🛠️

Welcome to your Dataloop journey! Let's get your environment perfectly set up for success.

## Useful Resources 📚

Before diving into the setup, here are some helpful resources:

1. 🔍 [Dataloop Python SDK Cheat Sheet](https://docs.dataloop.ai/docs/sdk-cheatsheet) - Quick reference for SDK code examples
2. 💻 [Recommended Specifications](https://docs.dataloop.ai/docs/platform-recommended) - System requirements, supported browsers, and file formats
3. 🔑 [Sign Up](https://console.dataloop.ai) - Create your free Dataloop account
4. 📂 [Onboarding Files](https://github.com/dataloop-ai/dtlpy-documentation/tree/main/onboarding) - Access all onboarding exercise files
5. 📚 [In-depth SDK Documentation](https://sdk-docs.dataloop.ai/en/latest/entities.html) - Detailed SDK reference

[Dataloop Python SDK Cheat Sheet](https://docs.dataloop.ai/docs/sdk-cheatsheet)
[Recommended Specifications](https://docs.dataloop.ai/docs/platform-recommended)
[Sign Up](https://console.dataloop.ai)
[Onboarding Files](https://github.com/dataloop-ai/dtlpy-documentation/tree/main/onboarding)
[In-depth SDK Documentation](https://sdk-docs.dataloop.ai/en/latest/entities.html)

## System Requirements 💻

### Hardware Requirements
- CPU: 2+ cores recommended
- RAM: 4GB minimum, 8GB+ recommended
- Storage: 1GB+ free space for SDK and dependencies
- Internet: Stable connection required

### Software Prerequisites
- Operating System:
  - Windows 10/11
  - macOS 10.14+
  - Ubuntu 18.04+ or other modern Linux distributions
- Python: Version 3.12 
- uv: Latest version recommended

## Choose Your Package Manager

### Why Use uv? ⚡

**uv** is a modern Python package manager written in Rust that provides significant performance improvements and better reliability compared to traditional pip. It's designed to be a drop-in replacement for pip while offering faster operations and more robust dependency resolution.

See https://www.datacamp.com/tutorial/python-uv for more information

## Python Environment Setup 🐍

### 1. Installing Python

> 📌 **Run these commands in your terminal**:
>
> ```bash
> # Check if Python is installed
> python --version
>
> # If not installed, download from:
> # https://www.python.org/downloads/
> ```

💡 Pro Tip: Always check "Add Python to PATH" during Windows installation!

### 2. Installing uv

> 📌 **Run these commands in your terminal**:
>
> ```bash
> # Install uv
> # On Windows (PowerShell):
> irm https://astral.sh/uv/install.ps1 | iex
>
> # On macOS/Linux:
> curl -LsSf https://astral.sh/uv/install.sh | sh
>
> # Verify installation (restart PowerShell first on Windows)
> uv --version
> ```

### 3. Setting Up a Virtual Environment

> 📌 **Run these commands in your terminal**:
>
> ```bash
> # Initialize a new project and create a virtual environment using uv
>
> # uv init creates a pyproject.toml file and sets up the project structure:
> uv init 
>
> # Create a new virtual environment using uv (creates a .venv directory by default):
> uv venv
>
> # Activate the environment:
>
> # On Windows:
> .venv\Scripts\activate  
>
> # On macOS/Linux:
># source .venv/bin/activate
>
> # from activated venv - install ipykernel for Jupyter notebook support:
> uv add ipykernel
> ```

## SDK Installation Guide 📦

### 1. Basic Installation

> **Select the correct Python interpreter**
>
> 📌 **Important**: After activating the virtual environment, make sure to select the `.venv` kernel in your Jupyter notebook:
> 1. Click on "Kernel" in the top menu
> 2. Select "Change kernel"
> 3. Choose `.venv` from the list
> 4. Verify the kernel is selected (top right corner should show .venv)

> There are two ways to add Python packages to your active `.venv`:
>
> **Option 1: Install package for active venv on terminal**


> ```bash
> Open terminal and run:
>
> # Activate the virtual environment first
> .venv\Scripts\activate  # Windows
> # or
> source .venv/bin/activate  # macOS/Linux
>
> # Install the package
> uv add dtlpy
>
> # Verify installation
> uv pip show dtlpy
> ```
>
> **Option 2: Run directly from Jupyter notebook**

```python
# Install the Dataloop SDK
!uv add dtlpy

# Verify installation
!uv pip show dtlpy
```

### 2. Validation

```python
# Test your installation
import dtlpy as dl
print(dl.__version__)
```

## Best Practices & Tips 👑
### 1. Create API Keys 🔑

> **What is an API Key?**
>
> An API key is used to authenticate and authorize your access to the Dataloop platform.
>
> **How to Create an API Key:**
> 1. Navigate to your project dashboard
> 2. Go to the **API Keys** tab
> 3. Click "Create New Key"
> 4. Store it securely in a `.env` file to avoid exposing sensitive information

### 2. Environment Management

Use `python-dotenv` and `.env` files to load the API key:

> 🔒 Best Practices for .env Files:
> 1. Create a .env file in your project root: `DTLPY_API_KEY=your-api-key-here`
> 2. Add .env to your .gitignore file to prevent committing sensitive data
> 3. Create a .env.example file with dummy values as a template
> 4. Never commit real credentials to version control
> 5. Use strong, unique API keys
> 6. Regularly rotate your API keys

📚 Learn more about environment variable best practices and python dotenv [here](https://github.com/theskumar/python-dotenv)

```python
# Install python-dotenv
!uv add python-dotenv
```

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key securely
api_key = os.getenv('DTLPY_API_KEY')

# Initialize Dataloop with the API key
dl.login_api_key(api_key=api_key)
```

### 3. Security Best Practices

```python
# DON'T: Hardcode credentials
# api_key = "your-api-key"  # ❌


# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv('DTLPY_API_KEY')
```

### 4 Installation Troubleshooting

Common issues and solutions:

#### 1. SSL Certificate Errors

```bash
# Temporary fix using uv
uv add --trusted-host pypi.org --trusted-host files.pythonhosted.org dtlpy
```

```python
# Temporary fix using uv
!uv add --trusted-host pypi.org --trusted-host files.pythonhosted.org dtlpy
```
#### 2. Handle Dependency Conflicts

```python
# remove installed package
#uv uninstall dtlpy
# remove unused or old cached packages from uv's cache
#uv cache prune
# install the package again
# uv add dtlpy
```

#### 3. Version Mismatch

```bash
# Force specific version using uv
uv add dtlpy==x.y.z
```

```python
# Force specific version using uv
# uv add dtlpy==x.y.z
```

## Validation Checklist ✅

Before proceeding, ensure:
- Python version between 3.8 and 3.12 is installed
- Virtual environment is created and activated
- Dataloop SDK is installed
- Installation is verified
- Environment variables are set
- Test import is successful

## Next Steps 🎯

Once your environment is ready:

1. Configure your credentials
2. Create your first project
3. Start exploring Dataloop's features

🔍 Need Help? Check our [troubleshooting guide](https://docs.dataloop.ai/docs/troubleshooting)

## Pro Tips 💡

### 1. IDE Integration
- Use VS Code or PyCharm for better development experience
- Install Python extensions for code completion

### 2. Development Workflow

```python
import dtlpy as dl

# Enable debug logging
dl.verbose.logging_level = "DEBUG"
```

```python
import dtlpy as dl

# Enable debug logging
dl.verbose.logging_level = "DEBUG"
```

### 3. Resource Management

```python
# Always clean up resources
try:
    # Your code here
    pass
finally:
    dl.logout()
```
Ready to start your Dataloop journey? Let's move on to authentication and project setup! 🚀
