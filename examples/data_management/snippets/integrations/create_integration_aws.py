import dtlpy as dl

organization = dl.organizations.get(organization_name='my_org')
organization.integrations.create(name='S3integration',
                                 integrations_type=dl.ExternalStorage.S3,
                                 options={'key': 'my_key', 'secret': 'my_secret'})
