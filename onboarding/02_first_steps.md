# Your First Steps in Dataloop 🎯

## What Can You Do? 🌟

With our powerful Python SDK, you'll have full control over your entire AI development lifecycle:

### Core Resources 📊
- 📁 **Projects** - Your high-level workspaces
- 📊 **Datasets** - Your data collections
- 🖼️ **Items** - Your individual files
- ✏️ **Annotations** - Your data labels
- 📝 **Metadata** - Your custom data attributes

### Advanced Features 🚀
- 🤖 **Model Management** - Train, deploy, and monitor ML models
- 🔄 **Pipelines** - Build automated AI workflows
- ⚡ **FaaS (Function as a Service)** - Deploy serverless functions
- 📦 **DPKs (Dataloop Package Kit)** - Package and share your solutions
- 🎯 **Tasks** - Manage annotation and review workflows

### AI Development Tools 🧠
- 🔍 **Model Zoo** - Access pre-trained models
- 🎓 **Transfer Learning** - Fine-tune existing models
- 📈 **Model Metrics** - Track performance and metrics
- 🔄 **Data Versioning** - Manage dataset versions

### Automation & Integration 🔗
- 🔄 **Webhooks** - Set up event-driven workflows
- 🌐 **REST API** - Integrate with external systems
- 🔌 **Plugins** - Extend platform functionality
- 🤝 **Team Collaboration** - Manage users and roles

## Authentication & Security 🔐

### 1. Interactive Login

> ```python
> import dtlpy as dl
>
> # Smart login with token handling
> if dl.token_expired():
>     dl.login()
> 
> # Test your installation
> print(dl.__version__)
> ```

### 2. Token Management

> ```python
> # Check token status
> is_expired = dl.token_expired()
>
> # Logout
> dl.logout()
> ```

### 3. Headless Authentication

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

## Project Management Mastery 🏗️

### 1. Creating Your First Project

> ```python
> # Project Setup
>
> # Set your project name here
> project_name = "onboarding-project"
> try:
>     # Try to get existing project
>     project = dl.projects.get(project_name=project_name)
>     print(f"Project '{project_name}' already exists")
> except dl.exceptions.NotFound:
>     # Create project if it doesn't exist
>     project = dl.projects.create(project_name=project_name)
>     print(f"Created project '{project_name}'")
> ```

### 2. Project Configuration

> ```python
> # Add project members
> project.add_member(
>     email='teammate@company.com',
>     role=dl.MemberRole.DEVELOPER
> )
> ```

### 3. Project Organization

> ```python
> # List all projects
> projects = dl.projects.list()
> for p in projects:
>     print(f"Project: {p.name}")
> ```


### 4. Project Exploration

**open_in_web()** 🌐

The `open_in_web()` method launches the Dataloop web platform in your default browser, providing direct access to view and manage your project resources from the SDK.


> ```python
> # Print project details
> project.print()
>
> # Open project in Dataloop platform and explore it
> project.open_in_web()
> ```

## Dataset Organization 📊

### 1. Creating Datasets

> ```python
> # Dataset Setup
>
> # Set your dataset name
> dataset_name = "onboarding-dataset"
>
> try:
>     # Try to get existing dataset
>     dataset = project.datasets.get(dataset_name=dataset_name)
>     print(f"Dataset '{dataset_name}' already exists")
> except dl.exceptions.NotFound:
>     # Create dataset if it doesn't exist
>     dataset = project.datasets.create(dataset_name=dataset_name)
>     print(f"Created dataset '{dataset_name}'")
> ```

### 2. Dataset Management

> ```python
> # List all datasets
> datasets = project.datasets.list()
>
> # Get dataset by name
> dataset = project.datasets.get(dataset_name=dataset_name)
>
> # Print dataset details
> dataset.print()
> ```

> ```python
> # Explore dataset in Dataloop platform
> dataset.open_in_web()
> ```

## Team Collaboration Essentials 👥

### 1. Role Management

> ```python
> # Add team member with role
> project.add_member(
>     email='annotator@company.com',
>     role=dl.MemberRole.ANNOTATOR
> )
>
> # Update member role
> project.update_member(
>     email='annotator@company.com',
>     role=dl.MemberRole.DEVELOPER
> )
> ```

### 2. Access Control

> ```python
> # List project members
> members = project.list_members()
> for member in members:
>     print(f"{member.email}: {member.role}")
>
> # Remove member
> project.remove_member(email='annotator@company.com')
> ```

Ready to start working with data? Let's move on to data management! 🚀
