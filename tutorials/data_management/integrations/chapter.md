# Integrations  
Integrations allow Dataloop organizations to securely configure secrets for accessing external resources within their projects. These resources include cloud storage services (GCP, S3, Azure), Secure Token Service (STS), and Docker registry services like AWS Elastic Container Registry (ECR), Google Container Registry (GCR), Google Artifact Registry (GAR), and more.  
  
With a cloud-storage driver, setting up an integration to a cloud provider is the first step,  
enabling the access token to the service.  
  
To add a new integration:  
  

```python
import dtlpy as dl
project = dl.projects.get(project_name='My-Project')
project.integrations.create(integrations_type=dl.ExternalStorage.S3,
                            name='S3ntegration',
                            options={"key": "Access key ID", "secret": "Secret access key"})
```
For more information visit the next page (Cloud Storage), where you can learn more about create storage drivers.  
  
