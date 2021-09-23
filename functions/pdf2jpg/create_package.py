import dtlpy as dl

package_name = 'pdf2jpg'
project_name = 'COCO ors'
src_path = 'functions/pdf2jpg'
input_directory = '/incoming'

project = dl.projects.get(project_name=project_name)

####################
# Push the Package #
####################

modules = [dl.PackageModule(name='pdf2jpg',
                            class_name='ServiceRunner',
                            entry_point='main.py',
                            functions=[
                                dl.PackageFunction(
                                    inputs=[dl.FunctionIO(type="Item", name="item")],
                                    outputs=[dl.FunctionIO(type="Item", name="item")],
                                    name='run',
                                    display_name='PDF to JPG',
                                    description='convert PDF to JPG')
                            ])]
package = project.packages.push(package_name=package_name,
                                modules=modules,
                                src_path=src_path)
package = project.packages.get(package_name=package_name)
package.print()

######################
# Create the Service #
######################
service = package.services.deploy(service_name=package.name,
                                  runtime=dl.KubernetesRuntime(concurrency=32,
                                                               runner_image='gcr.io/viewo-g/piper/agent/cpu/pdf2jpg:1'),
                                  module_name='pdf2jpg')

print('Service deployed successfully!')
# service = package.services.get(service_name=package.name)
# service.package_revision = package.version
# service.update()

######################
# Create the Trigger #
######################
trigger = service.triggers.create(name=package.name,
                                  execution_mode=dl.TriggerExecutionMode.ONCE,
                                  resource=dl.TriggerResource.ITEM,
                                  actions=dl.TriggerAction.CREATED,
                                  filters=dl.Filters(field='dir', values=input_directory))
print('Trigger was created successfully!')
