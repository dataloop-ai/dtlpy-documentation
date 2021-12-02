import dtlpy as dl

if dl.token_expired():
    dl.login()

# Set your names and keys
organization_name = 'my-org'
project_name = 'my-project-name'
dataset_name = 'my_dataset_name'
integrations_name = 'S3integration'
driver_name = 'my_driver_name'
aws_key = ''
aws_secret_key = ''
bucket_name = ''
region = ''

organization = dl.organizations.get(organization_name=organization_name)
# Create an secret integrations
integrations = organization.integrations.create(name=integrations_name, integrations_type=dl.ExternalStorage.S3,
                                                options={'key': aws_key, 'secret': aws_secret_key})

project = dl.projects.get(project_name=project_name)

project.drivers.create(name=driver_name,
                       driver_type=dl.ExternalStorage.S3,
                       integration_id=integrations.id,
                       bucket_name=bucket_name,
                       project_id=project.id,
                       allow_external_delete=True,
                       region=region,
                       storage_class="",
                       path="")

# create a dataset from a driver name, you can also create by the driver ID
dataset = project.datasets.create(driver=driver_name, dataset_name=dataset_name)

dataset.sync()