import dtlpy as dl

organization = dl.organizations.get(organization_name='my_org')
organization.integrations.create(name='azureintegration',
                                 integrations_type=dl.ExternalStorage.AZUREBLOB,
                                 options={'key': 'my_key',
                                          'secret': 'my_secret',
                                          'clientId': 'my_clientId',
                                          'tenantId': 'my_tenantId'})
