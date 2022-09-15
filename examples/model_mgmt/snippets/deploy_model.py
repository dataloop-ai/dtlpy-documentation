import dtlpy as dl

package = dl.packages.get(package_name='resnet')
pretrained_model = package.models.get(model_name='pretrained-resnet')

model = pretrained_model.clone(model_name='my pretrained',
                               description='pretrained cloned in to my project',
                               project_id="projectId")

model.deploy()
