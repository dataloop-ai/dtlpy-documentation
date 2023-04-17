import dtlpy as dl
if dl.token_expired():
    dl.login()
def section1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    organization = dl.organizations.get(organization_name='my-org')
    organization.integrations.create(name='S3integration', integrations_type=dl.ExternalStorage.S3,
                                     options={'key': "my_key", 'secret': "my_secret"})



def section2():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()

    # Fetch your project id
    project = dl.projects.get(project_id='<YOUR_PROJECT_ID>')

    # Create a partial AWS Cross Account integration (before you add the IAM user to the Trust relationship of the role)
    integration: dl.Integration = project.integrations.create(integrations_type=dl.IntegrationType.AWS_CROSS_ACCOUNT,
                                                              name='<YOUR_INTEGRATION_NAME>')

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


def section3():

    # After Adding the user ARN to your role trust relationship, continue and update the integration
    integration.update(new_options={'roleArn': '<YOUR_IAMֹֹֹֹֹ_ROLE_ֹֹARN>'})

    # checking the integration was created correctly
    for metadata in integration.meatadata:
        if metadata['name'] == 'status':
            if metadata['value'] != 'trust-established':
                raise ValueError('ERROR: Integration was not setup correctly - please check the trust relationship in your IAM Role')