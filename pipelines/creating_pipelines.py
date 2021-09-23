import dtlpy as dl
from pipelines.utils import create_and_deploy_faas, create_pipeline_from_json

dl.login()
####################################
# Initialize environment variables #
####################################
project_name = 'My Project'
package_name = 'pipeline-faas-example-package'
dataset_name = 'pipeline-faas-example-dataset'

project = dl.projects.get(project_name=project_name)
dataset = project.datasets.create(dataset_name=dataset_name)
print('Initialized params project_name:{}, dataset_name:{}'.format(project.name,dataset.name))
#############################################
# Publish new package and deploy as service #
#############################################
service = create_and_deploy_faas(project.id, package_name)
print('Service was created service_name:{}'.format(service.name))
##########################################
# Generate pipeline with relevant params #
##########################################
pipeline = create_pipeline_from_json(service, dataset)
print('Pipeline was created pipeline_name:{}'.format(pipeline.name))
###########################
# Installing the pipeline #
###########################
print('Installing pipeline')
pipeline.install()
print('Opening pipeline in console...')
pipeline.open_in_web()


###############
# Cleaning up #
###############
# dataset.delete()
# service.delete()
# pipeline.delete()