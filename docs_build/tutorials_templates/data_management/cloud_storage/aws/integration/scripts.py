def section1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    organization = dl.organizations.get(organization_name='my-org')
    organization.integrations.create(name='S3integration', integrations_type=dl.ExternalStorage.S3,
                                     options={'key': "my_key", 'secret': "my_secret"})