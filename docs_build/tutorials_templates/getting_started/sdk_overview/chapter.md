# Welcome to Dataloop SDK: Your AI Development Companion 🚀

Ready to supercharge your AI development? The Dataloop SDK is your all-in-one toolkit for managing the complete AI lifecycle. Think of it as your command center for everything from data management to production deployment!

## What Can You Do? 🎯

With our powerful Python SDK, you'll have full control over:

- 📁 Projects - Your high-level workspaces
- 📊 Datasets - Your data collections
- 🖼️ Items - Your individual files
- ✏️ Annotations - Your data labels
- 📝 Metadata - Your custom data attributes

## Getting Started: Your Journey Begins Here 🌟

Let's get you up and running with everything you need:

### 1. Setting Up Your Environment 🛠️

First, let's get the essential tools installed:

#### Python Installation 🐍
1. Visit [Python Downloads](https://www.python.org/downloads/)
2. Get Python 3.8 or later
3. Follow the installation wizard

> 💡 **Pro Tip**: Make sure to check "Add Python to PATH" during installation!

#### Dataloop SDK Installation 📦

```bash
# Install using pip
pip install dtlpy

# Verify installation
pip show dtlpy  # Should show version 1.64.9 or later
```

### 2. Logging In: Your Gateway to Dataloop 🔑

```python
import dtlpy as dl

# Smart login that handles token expiration
if dl.token_expired():
    dl.login()
```

#### For Long-Running Jobs: M2M Authentication 🤖

```python
# Using API key (recommended for automation)
dl.login_api_key(api_key=os.environ['DTLPY_API_KEY'])
```

> ⚠️ **Security Tip**: Always store API keys as environment variables!

#### Logging In with an API Key

In addition to standard browser-based authentication, the Dataloop SDK supports API key authentication, which is ideal for automated workflows, pipelines, etc.
To generate your API Key, refer to the [Dataloop Documentation](https://docs.dataloop.ai/docs/project-dashboard-1#manage-api-keys).

```python
import dtlpy as dl

# Set environment (optional)
dl.setenv('rc')  # or 'prod'

# Authenticate
dl.login_api_key('YOUR_API_KEY_HERE')
```

### 3. Creating Your First Project 🎨

```python
# Create a new project
project = dl.projects.create(project_name='My-Awesome-Project')

# Or get an existing one
project = dl.projects.get(project_name='My-Awesome-Project')
```

### 4. Managing Team Access 👥

```python
# Add a team member
project.add_member(
    email='teammate@company.com',
    role=dl.MemberRole.Developer
)

# Update roles
project.update_member(
    email='teammate@company.com',
    role=dl.MemberRole.Annotator
)
```

### 5. Working with Datasets 📊

```python
# Create a new dataset
dataset = project.datasets.create(dataset_name='My-First-Dataset')

# Upload items
item = dataset.items.upload(
    local_path=r'C:\path\to\your\image.jpg'
)
```

> 🎯 **Pro Tip**: Use `remote_path` to organize files in folders!

### 6. Adding Annotations ✏️

```python
# Create an annotation builder
builder = item.annotations.builder()

# Add a classification
builder.add(
    annotation_definition=dl.Classification(
        label='cat'
    )
)

# Add a bounding box
builder.add(
    annotation_definition=dl.Box(
        left=100,
        top=100,
        right=200,
        bottom=200,
        label='cat-face'
    )
)

# Save annotations
item.annotations.upload(builder)
```

### 7. Smart Filtering 🔍

```python
# Create a filter
filters = dl.Filters()

# Find all items with 'cat' annotations
filters.add_join(field='label', values='cat')

# Get filtered items
items = dataset.items.list(filters=filters)
for item in items.all():
    print(f"Found cat in: {item.name}")
```

### 8. Working with Metadata 📝

```python
# Add metadata to an item
item.metadata['user'] = {
    'photographer': 'John Doe',
    'location': 'New York',
    'date': '2024-03-20'
}
item = item.update()

# Filter by metadata
filters = dl.Filters()
filters.add(field='metadata.user.location', values='New York')
```

### 9. Creating Tasks 📋

```python
# Create an annotation task
task = dataset.tasks.create(
    task_name='Annotate Cats',
    assignee_ids=['annotator@company.com'],
    due_date=datetime.datetime(2024, 12, 31).timestamp()
)
```

## Best Practices 👑

1. **Error Handling** 🛡️
   ```python
   try:
       item = dataset.items.get(item_id='your-item-id')
   except dl.exceptions.NotFound:
       print("Item not found!")
   ```

2. **Batch Operations** ⚡
   ```python
   # Upload multiple items
   dataset.items.upload(
       local_path=r'C:\path\to\folder',
       local_annotations_path=r'C:\path\to\annotations'
   )
   ```

3. **Resource Cleanup** 🧹
   ```python
   # Always logout when done
   dl.logout()
   ```

## Ready to Build Something Amazing? 🚀

You now have all the tools to:
- Manage your AI projects
- Organize your datasets
- Label your data
- Create annotation tasks
- Track everything with metadata

Happy coding! 🎉

> 📚 **Want to Learn More?** Check out our [full onboarding](onboarding.md)!
