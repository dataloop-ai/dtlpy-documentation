import dtlpy as dl

##############################################
# Clone a pre-trained model without finetune #
##############################################

global_package = dl.packages.get(package_name='resnet')
pretrained_model = global_package.models.get(model_name='pretrained-resnet50')

my_project = dl.projects.get(project_id="$PROJECT_ID")
model = pretrained_model.clone(model_name='my pretrained',
                               description='cloned pretrained in my project',
                               project_id=my_project.id)

###############################
# Clone and fine-tune a model #
###############################
dataset = my_project.datasets.get(dataset_name='Finetuning')

train_filter = dl.Filters('dir', '/train')
val_filter = dl.Filters('dir', '/validation')

model = pretrained_model.clone(model_name='finetuned-resnet',
                               description='cloned for finetune in my project',
                               project_id=my_project.id,
                               dataset=dataset,
                               train_filter=train_filter,
                               validation_filter=val_filter)
