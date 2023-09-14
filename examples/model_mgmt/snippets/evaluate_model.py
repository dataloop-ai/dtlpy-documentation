import dtlpy as dl

package = dl.packages.get(package_name='resnet')
pretrained_model = package.models.get(model_name='pretrained-resnet50')

model = pretrained_model.clone(model_name='my pretrained',
                               description='pretrained cloned in to my project',
                               project_id="$PROJECT_ID")

dataset = dl.datasets.get(dataset_id='datasetId')

model.evaluate(dataset=dataset)
