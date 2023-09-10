import dtlpy as dl


class Scripts:
    def func1(self):
        import dtlpy as dl
        project = dl.projects.get(project_name='My-Project')
        project.integrations.create(integrations_type=dl.ExternalStorage.S3,
                                    name='S3ntegration',
                                    options={"key": "Access key ID", "secret": "Secret access key"})
