# Integrations  
Integrations enable Dataloop organizations to define secrets for accessing external resources  
in their project including cloud storage (GCP, S3, or Azure), Secure Token Service (STS),  
container registry services (ECR/GCR), and others.  
  
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
  
