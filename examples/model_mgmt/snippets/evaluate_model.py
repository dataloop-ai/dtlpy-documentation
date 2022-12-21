import dtlpy as dl

package = dl.packages.get(package_name='resnet')
pretrained_model = package.models.get(model_name='pretrained-resnet')

model = pretrained_model.clone(model_name='my first exp',
                               description='with higher lr',
                               project_id="projectId")

model.train()
