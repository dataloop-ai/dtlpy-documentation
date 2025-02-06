# Secrets  
  
Our secrets manager is a powerful tool designed to provide secure and efficient management of secrets.  
By creating and storing secrets and integrating them with Pipelines and FAAS, our platform offers a comprehensive solution for all your secret management needs.  
  
  
## Create A key value secret  

```python
import dtlpy as dl
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(name='KeyValueSecret',
                                 integrations_type=dl.IntegrationType.KEY_VALUE,
                                 options={'key': "my_key", 'value': "my_value"})
```
## Using Secrets  
Key-value secrets can be used in any FaaS, check [this tutorial](https://developers.dataloop.ai/tutorials/faas/advance/chapter/#using-secrets-in-a-function) for more information.  
