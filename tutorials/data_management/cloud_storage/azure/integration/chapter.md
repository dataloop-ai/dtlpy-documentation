# Integrations  
  
If you already have your data managed and organized on a cloud storage service, such as Azure Blob Storage, you may want to  
utilize that with Dataloop, and not upload the binaries and create duplicates.  
  
### Microsoft Azure integration  
  
Access & Permissions - Creating an integration with Azure requires allowing dataloop specific permissions for accessing the resource  
  
To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/storage-azure)  
  
  
### Create integration With Microsoft Azure  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(name='azureintegration',
                                 integrations_type=dl.ExternalStorage.AZUREBLOB,
                                 options={'key': 'my_key',
                                          'secret': 'my_secret',
                                          'clientId': 'my_clientId',
                                          'tenantId': 'my_tenantId'})
```
