# Using Customer Docker and Code Registries
## 🐳 Custom Docker Environments

### Using Custom Docker Images
You can use any Docker image to run your FaaS application. Here's how:

Set the image in the manifest:

```json
"components": {
    "services": [
        {
            "name": "my-service",
            "runtime": {
                "runner_image": "docker.io/python:3.8"
            }
        }
    ]
}
```

```python
# Deploy with a custom Docker image
service = project.services.get('my-service')  
service.runtime.runner_image = 'docker.io/python:3.8'
service.update()
```

### Dataloop's Public Images
We maintain public Docker images with different configurations:

```python
# Use Dataloop's GPU-enabled image with CUDA 11.5 and Python 3.8
service.runtime.runner_image = 'dockerhub.io/dataloopai/dtlpy-agent:latest.gpu.cuda11.5.py3.8.opencv'
service.update()
```

Our images are available on [Dockerhub](https://hub.docker.com/repository/registry-1.docker.io/dataloopai/dtlpy-agent/tags).

### Building Custom Images
Need a specialized environment? Create your own Docker image:

```dockerfile
FROM dockerhub.io/dataloopai/dtlpy-agent:latest.gpu.cuda11.5.py3.8.opencv

# Add system dependencies
RUN apt update && apt install -y zip ffmpeg

# Switch to non-root user
USER 1000
ENV HOME=/tmp

# Install Python packages
RUN pip3 install --user \
    dtlpy==1.54.10 \
    dtlpy-agent==1.54.10 \
    torch \
    torchvision \
    imgaug \
    scikit-image==0.17.2
```

### Private Docker Registry
Need to use images from a private registry? Here's how to set it up:

```python
import base64
import json

# Set up registry credentials
username = '<docker hub username>'
password = '<docker hub password>'
email = '<email>'

# Create auth token
auth = base64.b64encode(f"{username}:{password}".encode('ascii')).decode('ascii')

# Create credentials payload
cred_payload = {
    "auths": {
        "docker.io": {
            "username": username,
            "password": password,
            "email": email,
            "auth": auth
        }
    }
}

# Encode credentials
encoded_cred = base64.b64encode(json.dumps(cred_payload).encode()).decode()

# Create organization integration
org = dl.organizations.get(organization_name='<org name>')
secret = org.integrations.create(
    integrations_type='private-registry',
    name='dockerhub-secret',
    options={
        "name": "_json_key",
        "spec": {"password": encoded_cred}
    }
)

# Now use your private image
service = package.deploy(
    service_name='private-service',
    runtime=dl.KubernetesRuntime(
        runner_image='private-registry.com/my-image:tag'
    )
)
```

## 🔗 Private Git Integration

### Setting Up Git Credentials
Configure authentication for private repositories:

```python
# Create username and password integrations
project = dl.projects.get(project_id='project_id')

username_integration = project.integrations.create(
    integrations_type=dl.IntegrationType.KEY_VALUE,
    name='github-username',
    options={
        "key": "username",
        "value": "<github_username>"
    }
)

password_integration = project.integrations.create(
    integrations_type=dl.IntegrationType.KEY_VALUE,
    name='github-token',
    options={
        "key": "password",
        "value": "<github_personal_access_token>"
    }
)
```

### Configuring Git in DPK Manifest
Add Git configuration to your `dataloop.json`:

```json
{
  "name": "private-git-dpk",
  "scope": "project",
  "codebase": {
    "type": "git",
    "gitUrl": "https://github.com/your-org/your-repo.git",
    "gitTag": "main",
    "credentials": {
      "username": {
        "key": "username",
        "id": "<username integration id>"
      },
      "password": {
        "key": "password",
        "id": "<password integration id>"
      }
    }
  },
  "components": {
    "services": [
      {
        "name": "my-service",
        "runtime": {
          "podType": "regular-s",
          "concurrency": 10
        }
      }
    ]
  }
}
```

### Publishing with Git Integration
Deploy your service from the Git repository:

```python
# Publish the DPK with Git integration
dpk = project.dpks.publish()

# Deploy specific service
service = dpk.services.deploy('my-service')
```
