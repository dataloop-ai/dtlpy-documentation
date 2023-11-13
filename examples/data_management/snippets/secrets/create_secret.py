import dtlpy as dl

organization = dl.organizations.get(organization_name='my_org')
organization.integrations.create(name='my_secret',
                                 integrations_type=dl.IntegrationType.KEY_VALUE,
                                 options={'key': 'my_key', 'value': 'my_value'})
