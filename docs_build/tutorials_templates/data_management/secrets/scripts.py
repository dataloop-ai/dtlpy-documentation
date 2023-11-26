def section1():
    import dtlpy as dl
    organization = dl.organizations.get(organization_name='my-org')
    organization.integrations.create(name='KeyValueSecret',
                                     integrations_type=dl.IntegrationType.KEY_VALUE,
                                     options={'key': "my_key", 'value': "my_value"})