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

```python
import dtlpy as dl

# Smart login with token handling
if dl.token_expired():
    dl.login()
```

```python
# Test your installation
import dtlpy as dl
print(dl.__version__)
```

### 2. Token Management

```python
# Check token status
is_expired = dl.token_expired()
# Logout
dl.logout()
```

### 3. Headless Authentication

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

```python
# Using email/password (not recommended for production)
# dl.login_m2m(email='your-email@company.com', 
#              password=os.environ['DTLPY_PASSWORD'])
```

## Project Management Mastery 🏗️

### 1. Creating Your First Project

```python
# ============================================================================
# Project  Setup
# ============================================================================
# Create your project(or get if they already exist)
#set your project name here
project_name = "My-Awesome-Project-2"
try:
    # Try to get existing project
    project = dl.projects.get(project_name=project_name)
    print(f"Project '{project_name}' already exists")
except Exception:
    # Create project if it doesn't exist
    project = dl.projects.create(project_name=project_name)
    print(f"Created project '{project_name}'")
```

```python
# Get existing project
project = dl.projects.get(project_name=project_name)

project.print()

project.open_in_web()
```

### 2. Project Configuration

```python
# Add project members
project.add_member(
    email='teammate@company2.com',
    role=dl.MemberRole.DEVELOPER
)
```

### 3. Project Organization

```python
# List all projects
projects = dl.projects.list()
for project in projects:
    print(f"Project: {project.name}")
```

## Dataset Organization 📊

### 1. Creating Datasets

```python
# ============================================================================
# Datset  Setup
# ============================================================================
# Create your datset(or get if they already exist)

#set your training and update dataset name 
dataset_training_name = "training-data"

try:
    # Try to get existing dataset
    dataset = project.datasets.get(dataset_name=dataset_training_name)
    print(f"Dataset '{dataset_training_name}' already exists")
except Exception:
    # Create dataset if it doesn't exist
    dataset = project.datasets.create(dataset_name=dataset_training_name)
    print(f"Created dataset '{dataset_training_name}'")
```

```python
# Clone an existing dataset
cloned_dataset = dataset.clone(
    clone_name="validation-data"   
)
```

### 2. Dataset Management

```python
# List all datasets
datasets = project.datasets.list()

# Get dataset by name
dataset = project.datasets.get(dataset_name=dataset_training_name)

# Update dataset
dataset.name = "training-data-v1"
dataset.update()
```

```python
dataset.open_in_web()
```

## Team Collaboration Essentials 👥

### 1. Role Management

```python
# Add team member with role
project.add_member(
    email='annotator@company.com',
    role=dl.MemberRole.ANNOTATOR
)

# Update member role
project.update_member(
    email='annotator@company.com',
    role=dl.MemberRole.DEVELOPER
)
```

### 2. Access Control

```python
# List project members
members = project.list_members()
for member in members:
    print(f"{member.email}: {member.role}")

# Remove member
project.remove_member(email='annotator@company.com')
```

## Best Practices 👑

### 1. Project Organization
- Use clear naming conventions
- Add detailed descriptions
- Maintain proper documentation
- Tag resources appropriately

### 2. Security Practices

```python
# Use environment variables
api_key = os.environ.get('DTLPY_API_KEY')

# Regular token refresh
if dl.token_expired():
    dl.refresh_token()
```

### 3. Resource Management

```python
# Clean up unused resources
try:
    # Your code here
finally:
    # Logout when done
    dl.logout()
```

## Troubleshooting Guide 🔧

### Common Issues:

1. **Authentication Failures**

```python
# Check token status
print(dl.token_expired())
   
# Force re-authentication
dl.login_m2m(force=True, email="your_email", password="your_password")
```

2. **Project Access Issues**

```python
# Verify project existence
try:
    project = dl.projects.get(project_name='My-Project')
except dl.exceptions.NotFound:
    print("Project not found!")
```

3. **Dataset Operations**

```python
# Handle dataset errors
try:
    dataset.update(system_metadata='New description')
except dl.exceptions.Forbidden:
    print("Insufficient permissions!")
```

Ready to start working with data? Let's move on to data management! 🚀
