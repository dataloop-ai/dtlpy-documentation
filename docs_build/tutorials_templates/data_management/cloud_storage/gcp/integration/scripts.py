def section1():
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