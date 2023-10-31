# Secrets  
  
If you already have your data managed and organized on a cloud storage service, such as S3, you may want to  
utilize that with Dataloop, and not upload the binaries and create duplicates.  
  
  
### Create A key value secret  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(name='KeyValueSecret', integrations_type=dl.IntegrationType.KEY_VALUE,
                                 options={'key': "my_key", 'value': "my_value"})
```
