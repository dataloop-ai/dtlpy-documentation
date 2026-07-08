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
- CPU: 2+ cores recommended
- RAM: 4GB minimum, 8GB+ recommended
- Storage: 1GB+ free space for SDK and dependencies
- Internet: Stable connection required

### Software Prerequisites
- Operating System:
  - Windows 10/11
  - macOS 10.14+
  - Ubuntu 18.04+ or other modern Linux distributions
- Python: Version 3.8 to 3.12

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

### 2. Setting Up a Virtual Environment

> 📌 **Run these commands in your terminal**:
>
> ```bash
> # Create a new virtual environment:
> python -m venv .venv
>
> # Activate the environment:
>
> # On Windows:
> .venv\Scripts\activate  
>
> # On macOS/Linux:
> # source .venv/bin/activate
>
> # Install ipykernel for Jupyter notebook support:
> pip install ipykernel
> ```

## SDK Installation Guide 📦

### 1. Basic Installation

 **Select the correct Python interpreter**

 📌 **Important**: After activating the virtual environment, make sure to select the `.venv` kernel in your Jupyter notebook:
 1. Click on "Kernel" in the top menu
 2. Select "Change kernel"
 3. Choose `.venv` from the list
 4. Verify the kernel is selected (top right corner should show .venv)

 There are two ways to add Python packages to your active `.venv`:

 **Option 1: Install package for active venv on terminal**

Open terminal and run:
> ```bash
> # Activate the virtual environment first
> .venv\Scripts\activate  # Windows
> # or
> source .venv/bin/activate  # macOS/Linux
>
> # Install the package
> pip install dtlpy
>
> # Verify installation
> pip show dtlpy
> ```

**Option 2: Run directly from Jupyter notebook**

> ```python
> # Install the Dataloop SDK
> !pip install dtlpy
>
> # Verify installation
> !pip show dtlpy
> ```

### 2. Validation

> ```python
> # Test your installation
> import dtlpy as dl
> print(dl.__version__)
> ```

## Best Practices & Tips 👑

### 1. API Keys (For Automated / Headless Workflows) 🔑

For interactive use, `dl.login()` (covered in the next chapter) is the simplest way to authenticate — it opens a browser window and handles everything for you.

For **automated or headless environments** (CI/CD pipelines, remote servers, scheduled scripts), use an API key instead:

**How to Create an API Key:**
1. Navigate to your project dashboard
2. Go to the **API Keys** tab
3. Click "Create New Key"
4. Store it securely in a `.env` file to avoid exposing sensitive information

**Using API Keys Securely:**

Use `python-dotenv` and `.env` files to load the API key:

🔒 Best Practices for .env Files:
1. Add .env to your .gitignore file to prevent committing sensitive data
2. Create a .env.example file with dummy values as a template
3. Never commit real credentials to version control
4. Use strong, unique API keys
5. Regularly rotate your API keys

📚 Learn more about environment variable best practices and python dotenv [here](https://github.com/theskumar/python-dotenv)

> ```python
> # Install python-dotenv
> !pip install python-dotenv
> ```

> ```python
> from dotenv import load_dotenv
> import os
>
> # Load environment variables from .env file
> load_dotenv()
>
> # Access your API key securely
> api_key = os.getenv('DTLPY_API_KEY')
>
> # Initialize Dataloop with the API key
> dl.login_api_key(api_key=api_key)
> ```

> ```python
> # DON'T: Hardcode credentials
> # api_key = "your-api-key"  # ❌
> # Always use environment variables instead
> ```

## Validation Checklist ✅

Before proceeding, ensure:
- Python version between 3.8 and 3.12 is installed
- Virtual environment is created and activated
- Dataloop SDK is installed
- Installation is verified
- Environment variables are set
- Test import is successful

Ready to start your Dataloop journey? Let's move on to authentication and project setup! 🚀
