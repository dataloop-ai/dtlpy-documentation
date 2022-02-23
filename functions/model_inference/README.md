# Model Inference Simple Example

## Some Names and Gets

```
import dtlpy as dl
package_name = 'inceptionv3'
project_name = 'My Project'
src_path = 'functions/model_inference'
project = dl.projects.get(project_name=project_name)

```

## Deploy the Package

```
modules = [dl.PackageModule(class_name='ModelRunner',
                            entry_point='main.py',
                            functions=[
                                dl.PackageFunction(
                                    inputs=[dl.FunctionIO(type="Item", name="item")],
                                    outputs=[dl.FunctionIO(type="Item", name="item")],
                                    name='inference',
                                    display_name='InceptionV3',
                                    description='Inference on a pretrained imagenet model')
                            ])]
package = project.packages.push(package_name=package_name,
                                modules=modules,
                                src_path=src_path)
```

## Deploy the Service

We'll run the inference on a CPU, with a TensorFlow docker image.

```
service = package.services.deploy(service_name=package.name,
                                  runtime=dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_REGULAR_XS,
                                                               runner_image='tensorflow/tensorflow:2.7.0'))
```

To update an existing service with a new pushed package run the following code:

```
service = package.services.get(service_name=package.name)
service.package_revision = package.version
service.update()
```

# Run an Execution

```
item = dl.items.get(item_id='61eac3aa6c58a66411a416f4')
ex = service.execute(function_name='inference',
                    execution_input=dl.FunctionIO(type=dl.PackageInputType.ITEM, value=item.id, name='item'))
ex = ex.wait()
print(ex.latest_status)
item.open_in_web()               
```