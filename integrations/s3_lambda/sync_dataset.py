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

organization = dl.organizations.get(organization_name='my-org')
# Create an secret integrations
organization.add_integrations(name=integrations_name, integrations_type='s3',
                              options={'key': aws_key, 'secret': aws_secret_key})


# Create drivers in the platform using this tutorial. https://dataloop.ai/docs/storage#creating-storage-driver

project = dl.projects.get(project_name=project_name)

# create a dataset from a driver name, you can also create by the driver ID
dataset = project.datasets.create(driver=driver_name, dataset_name=dataset_name)

dataset.sync()
