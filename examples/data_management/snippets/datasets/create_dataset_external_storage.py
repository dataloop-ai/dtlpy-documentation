import dtlpy as dl

project = dl.projects.get(project_name='my_project')
dataset = project.datasets.create(dataset_name='my_dataset',
                                  driver='my_driver')
dataset.sync()