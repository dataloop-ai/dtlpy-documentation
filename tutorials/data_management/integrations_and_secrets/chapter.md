# Managing Integrations and Secrets in Dataloop 🔐

Welcome to your guide to managing integrations and secrets in Dataloop! Let's learn how to securely connect your external resources and manage sensitive information.

## Understanding Integrations 🔗

Think of integrations as secure bridges between Dataloop and your external resources. They're your organization's VIP passes to safely access and manage external services! 🎫

### What Can You Connect To? 🌐

Integrations allow your Dataloop organization to securely configure and access a variety of external resources:

- Cloud Storage Services ☁️
  - Google Cloud Platform (GCP)
  - Amazon S3
  - Microsoft Azure Blob
- Container Registries 🐳
  - AWS Elastic Container Registry (ECR)
  - Google Container Registry (GCR)
  - Google Artifact Registry (GAR)
- Secure Token Service (STS) 🔑
- And more exciting services! 🚀

### Why Use Integrations? 🎯

When working with cloud services (like storage drivers), setting up an integration is your crucial first step. It's like creating a secure vault where you can:
- Store access tokens safely 🔒
- Manage service credentials efficiently 🗝️
- Enable seamless connections between services 🤝

## Setting Up Integrations 🛠️

### Cloud Storage Integration ☁️

When working with cloud storage, setting up an integration is your first step. It's where you securely store your access credentials:

```python
import dtlpy as dl

# Get your project
project = dl.projects.get(project_name='My-Project')

# Create the integration
project.integrations.create(
    integrations_type=dl.ExternalStorage.S3,  # Choose your cloud provider type
    name='my-cloud-integration',
    options={
        "key": "Access key ID",
        "secret": "Secret access key"
    }
)
```

Want to learn more about cloud storage? Check out our detailed guides:
- [Amazon Web Services (S3)](/tutorials/data_management/external_storage_drivers/aws_s3/chapter.md)
- [Microsoft Azure Blob Storage](/tutorials/data_management/external_storage_drivers/azure_blob/chapter.md)
- [Google Cloud Storage](/tutorials/data_management/external_storage_drivers/gcs/chapter.md)

## Managing Secrets 🗝️

### Understanding Secrets Manager

Our secrets manager is your vault for sensitive information. It's designed to:
- Keep your credentials secure 🔒
- Make them easily accessible in your code 🎯
- Integrate smoothly with Pipelines and FaaS 🔄

### Creating Key-Value Secrets ✨

Need to store a simple key-value pair? Here's how:

```python
import dtlpy as dl

# Get your organization
organization = dl.organizations.get(organization_name='my-org')

# Create a key-value secret
organization.integrations.create(
    name='my-secret',
    integrations_type=dl.IntegrationType.KEY_VALUE,
    options={
        'key': "my_key",
        'value': "my_value"
    }
)
```

### Using Secrets in Your Code 💻

When working with FaaS, you can use secrets to access your external resources. 
In the cloud environment, the secrets are saved as an environment variable.

```python
import dtlpy as dl
import os

def my_function(item):
    # Access your secrets
    secret = os.environ.get('my-secret')
    # Your code here
    return item
```


For more details on using secrets in functions, check out our [FaaS Security and Environment Chapter](https://developers.dataloop.ai/tutorials/faas_applications/service_configurations/chapter#-security-and-environment).

## Best Practices 🌟

1. **Naming Convention**: Use clear, descriptive names for your integrations and secrets
2. **Access Control**: Only share secrets with those who need them
3. **Regular Rotation**: Update your secrets periodically for better security
4. **Documentation**: Keep track of what each secret is used for
5. **Validation**: Always validate your integrations after setting them up

## Need More Help? 🤔

Check out our [comprehensive documentation](https://docs.dataloop.ai/docs/welcome) for more details on managing integrations and secrets.

Happy securing! 🚀
