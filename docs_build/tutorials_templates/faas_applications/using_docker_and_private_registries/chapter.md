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
org = dl.organizations.get(organization_id=context.project.org['id'])
options = org.integrations.generate_docker_hub_options(
    username='',
    password=''
)
integration = org.integrations.create(
    integrations_type=dl.IntegrationType.PRIVATE_REGISTRY,
    name='dockerhub',
    metadata={"provider": "Dockerhub"},
    options=options
)

# Now use your private image
service = package.deploy(
    service_name='private-service',
    runtime=dl.KubernetesRuntime(
        runner_image='private-registry.com/my-image:tag'
    )
)
```

### AWS Elastic Container Registry (ECR) Integration

Ready to connect your AWS ECR to Dataloop? Let's make some cloud magic happen! ✨

**First Things First: Your AWS Checklist 📝**
1. 🪣 Create an S3 bucket in your AWS kingdom
2. 👮‍♂️ Set up an IAM policy (think of it as your security guard)
3. 🤝 Create the integration and get your VIP pass (IAM user) from Dataloop

Want the full scoop? Check out our [magical guide](https://docs.dataloop.ai/docs/aws-elastic-container-registry) in the Dataloop docs! 🎓

**Time to Connect! 🔌**

Let's write some code that'll make your AWS ECR and Dataloop become best friends:

```python
import dtlpy as dl

# Step 1: Get your organization by ID
org = dl.organizations.get(organization_id='your_organization_id')

# Step 2: Create the integration with AWS ECR
integration = org.integrations.create(
    integrations_type=dl.IntegrationType.PRIVATE_REGISTRY,  # Declares this as a private container registry
    name='aws-ecr-integration',  # Friendly name for this integration inside Dataloop

    # Step 3: Provide connection options for ECR
    options={
        "name": "AWS",  # Identifies the integration type/provider

        "spec": {
            "accessKeyId": "your_access_key_id",  # AWS Access Key ID (used for authentication)
            "secretAccessKey": "your_secret_access_key",  # AWS Secret Access Key
            "account": "your_aws_account_id",  # AWS Account ID (12-digit number, e.g., '123456789012')
            "region": "your_aws_region"  # AWS region where your ECR is hosted (e.g., 'us-west-2')
        }
    },

    # Step 4: Optional metadata to describe the provider
    metadata={"provider": "aws"}  # Tags this integration as an AWS provider
)
```

Once an integration is established, users can deploy services and pipelines using Container images stored in their private AWS ECR.

**🔑 Where to Find Your Secret Keys:**
Need help finding those mysterious AWS credentials? Our [documentation](https://docs.dataloop.ai/docs/aws-elastic-container-registry#prerequisites) has your treasure map!

**🎯 Final Step:**
Pop into your Dataloop platform and check the Integrations section - your new integration should be waving back at you! 👋


### Google Artifacts Registry (GAR) Integration

Want to manage your container artifacts like a pro?

#### 🏗️ Create and Configure (GAR)

1. Enable the GAR API

```bash
gcloud services enable artifactregistry.googleapis.com
```

This command enables the Artifact Registry API in your GCP project so you can start storing and managing container images, Maven packages, Python packages, etc.

2. Configure IAM Permissions

Ensure your account has the necessary permissions:

- Artifact Registry Admin (`roles/artifactregistry.admin`)
- Storage Admin (`roles/storage.admin`) (optional, for managing storage)


```bash
# Adds an IAM role binding to a specific Google Cloud project.
gcloud projects add-iam-policy-binding [PROJECT-ID] \     # Replace this with your actual GCP project ID.
  --member="user:[USER-EMAIL]" \          # Specifies the user (email address) to whom you're granting the role.
  --role="roles/artifactregistry.admin"   # Grants the Artifact Registry Admin role, which allows full control over Artifact Registry resources.
```

3. Authenticate Docker with GAR

Before pushing or pulling images, configure Docker to authenticate with GAR:

```bash
gcloud auth configure-docker [REGION]-docker.pkg.dev      # Replace [REGION] with the region your repository is hosted in (e.g., `us-central1`, `europe-west1`, etc.).
```

4. Tag and Push Container Images to GAR

**Tag your Container image:**

```bash
docker tag [IMAGE_NAME] [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY]/[IMAGE_NAME]:[TAG]
```

**Push it to Artifact Registry:**

```bash
docker push [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY]/[IMAGE_NAME]:[TAG]
```

**Verify the image:**

- Navigate to Artifacts Registry in the GCP Console: https://console.cloud.google.com/marketplace/product/google/artifactregistry.
- Confirm that the image is visible in the registry.

#### Integrate GAR with Dataloop


```python

import dtlpy as dl

# Retrieve your Dataloop project by ID
project = dl.projects.get(project_id='your_project_id')

# Get the organization associated with the project
org = dl.organizations.get(organization_id=project.org['id'])

# Generate integration options for GAR (Google Artifact Registry)
# Fill in your service account name, GAR email identity, and location (e.g., 'us-central1')
options = org.integrations.generate_gar_options(
    service_account='',  # The name of your GAR-linked GCP service account
    email='',            # The GCP IAM email used for authentication (e.g., service-account@project.iam.gserviceaccount.com)
    location=''          # The GAR region (e.g., 'us-central1')
)

# Create the integration object in Dataloop
integration = org.integrations.create(
    integrations_type=dl.IntegrationType.PRIVATE_REGISTRY,  # Defines this as a private registry integration
    name='gar-reg',  # Name of the integration (customizable)
    metadata={"provider": "gcp"},  # Indicates that the provider is Google Cloud
    options=options  # Pass the generated GAR options
)
```

Discover all the artifacts secrets in our [curator's guide](https://docs.dataloop.ai/docs/google-artifacts-registry)!


### Azure Container Registry (ACR) Integration

The Azure Container Registry (ACR) enables seamless integration with the Dataloop platform for managing containerized components such as custom plugins, microservices, and machine learning models to be used in the applications, pipelines, etc. of the dataloop platform. ACR supports OCI-compliant container images, providing a secure, scalable, and Azure-native way to deploy and manage assets within your AI data pipeline.

To integrate Azure Container Registry (ACR) with the Dataloop platform using the SDK, follow these steps:

```python
import dtlpy as dl

# Step 1: Retrieve the project by its ID
project = dl.projects.get(project_id='your_project_id')

# Step 2: Access the organization using the project's org ID
org = dl.organizations.get(organization_id=project.org['id'])

# Step 3: Generate ACR integration options
options = org.integrations.generate_azure_container_registry_options(
    username='',  # Your Azure Container Registry username (usually the admin user)
    password='',  # Corresponding password or access token
    location=''   # Azure region where your ACR is hosted (e.g., 'eastus')
)

# Step 4: Create the ACR integration in Dataloop
integration = org.integrations.create(
    integrations_type=dl.IntegrationType.PRIVATE_REGISTRY,  # Defines it as a private registry integration
    name='azure-reg',  # Name the integration for easy reference
    metadata={"provider": "Azure"},  # Specify Azure as the provider
    options=options  # Pass in the generated credentials and configuration
)
```

Learn more about the [ACR](https://docs.dataloop.ai/docs/azure-container-registry) in our user documentation.


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
