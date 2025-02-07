# Your First Steps in Dataloop 🎯

Let's get you started with Dataloop by setting up your authentication and creating your first project!

## Authentication & Security 🔐

### 1. Interactive Login

```python
import dtlpy as dl

# Smart login with token handling
if dl.token_expired():
    dl.login()
```

### 2. Headless Authentication

```python
# Using API key (recommended for automation)
dl.login_api_key(api_key=os.environ['DTLPY_API_KEY'])

# Using email/password (not recommended for production)
dl.login_m2m(email='your-email@company.com', 
             password=os.environ['DTLPY_PASSWORD'])
```

### 3. Token Management

```python
# Check token status
is_expired = dl.token_expired()

# Logout
dl.logout()
```

## Project Management Mastery 🏗️

### 1. Creating Your First Project

```python
# Create a new project
project = dl.projects.create(project_name='My-Awesome-Project')

# Get existing project
project = dl.projects.get(project_name='My-Awesome-Project')
```

### 2. Project Configuration

```python
# Add project members
project.add_member(
    email='teammate@company.com',
    role=dl.MemberRole.Developer
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
# Create a new dataset
dataset = project.datasets.create(dataset_name='training-data')

# Clone an existing dataset
cloned_dataset = dataset.clone(
    clone_name='validation-data'
)
```

### 2. Dataset Management

```python
# List all datasets
datasets = project.datasets.list()

# Get dataset by name
dataset = project.datasets.get(dataset_name='training-data')

# Update dataset
dataset.name = 'training-data-v1'
dataset.update()
```

## Team Collaboration Essentials 👥

### 1. Role Management

```python
# Add team member with role
project.add_member(
    email='annotator@company.com',
    role=dl.MemberRole.Annotator
)

# Update member role
project.update_member(
    email='annotator@company.com',
    role=dl.MemberRole.Developer
)
```

### 2. Access Control

```python
# List project members
members = project.members.list()
for member in members:
    print(f"{member.email}: {member.role}")

# Remove member
project.remove_member(email='ex-teammate@company.com')
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
   dl.login_m2m(force=True)
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
       dataset.update(description='New description')
   except dl.exceptions.Forbidden:
       print("Insufficient permissions!")
   ```

Ready to start working with data? Let's move on to data management! 🚀 