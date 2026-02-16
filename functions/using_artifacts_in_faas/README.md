# Using Artifacts

## Step 1: Uploading the file to the package using package.artifacts.upload

See [deploy line 17](deploy.py)

## Step 2: Downloading artifacts in the main class using package.artifacts.download

See [Package Code line 25](main.py)

## Service Execution

```python
ex = service.execute(function_name='run', project_id=project.id)
```

## The output prints will be:

```
"root - INFO - 140244145915648 - listing local files:"
"root - INFO - 140244145915648 - ['monkey-612x612.zip', '.gitignore', 'main.py', 'deploy.py', '__pycache__', 'README.md']"
"root - INFO - 140244145915648 - The artifact zip is now in our local folder"
```
