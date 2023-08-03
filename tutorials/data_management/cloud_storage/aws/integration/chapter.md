# Integrations  
  
If you already have your data managed and organized on a cloud storage service, such as S3, you may want to  
utilize that with Dataloop, and not upload the binaries and create duplicates.  
  
### Amazon Web Services integration  
  
Access & Permissions - Creating an integration with AWS requires allowing dataloop specific permissions for accessing the resource  
  
To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/aws-cross-account-integration)  
  
  
### Create AWS Access-Key integration  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(name='S3integration', integrations_type=dl.ExternalStorage.S3,
                                 options={'key': "my_key", 'secret': "my_secret"})
```
### Create AWS Cross Account integration  
  
Follow these steps:  
1. Create an S3 bucket on your AWS account  
2. Create an IAM policy on your AWS account  
3. Create the integration and get an IAM user from Dataloop  
To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/aws-cross-account-integration)  
  
To create the integration and get the IAM user follow this code snippet  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
# Fetch your project id
project = dl.projects.get(project_id='<YOUR_PROJECT_ID>')
# Create a partial AWS Cross Account integration (before you add the IAM user to the Trust relationship of the role)
integration: dl.Integration = project.integrations.create(integrations_type=dl.IntegrationType.AWS_CROSS_ACCOUNT,
                                                          name='<YOUR_INTEGRATION_NAME>', option={})
# value of the IAM user ARN
for metadata in integration.meatadata:
    if metadata['name'] == 'userArn':
        # value of the IAM user ARN
        iam_user_arn_value = metadata['value']
    elif metadata['name'] == 'status':
        # value of the integration - should be 'waiting-trust'
        integration_status = metadata['value']
# Go to your Role Trust relationship and add this IAM user ARN
print('The IAM User ARN is: ', iam_user_arn_value)
print('The Integration status is: ', integration_status)
```
  
4. Create an IAM role that can access the bucket on your AWS account  
5. Add The IAM user to the trust relationship of the role  
To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/aws-cross-account-integration)  
  
To update the integration and provide the IAM role ARN follow this code snippet  

```python
# After Adding the user ARN to your role trust relationship, continue and update the integration
integration.update(new_options={'roleArn': '<YOUR_IAMֹֹֹֹֹ_ROLE_ֹֹARN>'})
updated_integration = project.integrations.get(integrations_id=integration.id)
# checking the integration status was updated
for metadata in updated_integration.meatadata:
    if metadata['name'] == 'status':
        if metadata['value'] != 'trust-established':
            raise ValueError('ERROR: Integration was not setup correctly - please check the trust relationship in your IAM Role')
```
