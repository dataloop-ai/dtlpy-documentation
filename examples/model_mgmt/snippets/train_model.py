import dtlpy as dl

project = dl.projects.get(project_id="$PROJECT_ID")
pretrained_model = project.models.get(model_name='pretrained-resnet50')
dataset = dl.datasets.get(dataset_id='datasetId')

model = pretrained_model.clone(model_name='my pretrained',
                               description='pretrained cloned in to my project',
                               dataset=dataset,
                               project_id="$PROJECT_ID")

model.train()
