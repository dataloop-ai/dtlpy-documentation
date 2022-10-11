import dtlpy as dl

package = dl.packages.get(package_name='resnet')
model = package.models.get(model_name='pretrained-resnet')

dataset = dl.datasets.get(dataset_id='datasetId')

model.evaluate(dataset=dataset)
