def section1():
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