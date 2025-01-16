# Integrations  
  
If you already have your data managed and organized on a cloud storage service, such as GCS, you may want to  
utilize that with Dataloop, and not upload the binaries and create duplicates.  
  
  
### GCP integration  
  
Access & Permissions - Creating an integration with GCP requires allowing dataloop specific permissions for accessing the resource  
  
To learn more about setting up integrations, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/storage-gcp)  
  
### Create integration With Google Cloud Provider  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name=org_name)
with open(r"C:\gcsfile.json", 'r') as f:
    gcs_json = json.load(f)
gcs_to_string = json.dumps(gcs_json)
organization.integrations.create(name='gcsintegration',
                                 integrations_type=dl.ExternalStorage.GCS,
                                 options={'key': '',
                                          'secret': '',
                                          'content': gcs_to_string})
```

### Cross Project Integration

Follow these steps:  

1. Create a Cloud Storage Bucket on your GCP account.
2. Create an IAM policy on your GCP account.
3. Create the integration and get an IAM user from Dataloop.
To learn more about setting up integrations, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/cross-project-integration).


### Private Key Integration

Follow these steps:  

1. Create a Cloud Storage Bucket on your GCP account.
2. Create an IAM role on your GCP account.
3. Create a Service Account on your GCP account.
4. Create a Private Key for the Service Account on your GCP account.
To learn more about setting up integrations, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/private-key-integration).


### Google Artifacts Registry Integration

Follow these steps:  

1. Create and Configure a GCP Google Artifacts Registry on your GCP account.
2. Integrate GAR with the Dataloop Platform.
To learn more about setting up integrations, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/google-artifacts-registry).

### Google Container Registry Integration

Follow these steps:  

1. Create and Configure a GCP Google Container Registry.
2. Integrate GCR with the Dataloop Platform.
To learn more about setting up integrations, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/google-container-registry).


