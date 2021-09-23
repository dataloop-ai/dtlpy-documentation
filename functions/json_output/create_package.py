import dtlpy as dl

package_name = 'json-as-output'
project_name = 'COCO ors'
src_path = 'functions/json_output'
project = dl.projects.get(project_name=project_name)
################
# push package #
################
module = dl.PackageModule(functions=[dl.PackageFunction(name='item_to_json',
                                                        inputs=dl.FunctionIO(type='Item', name='item'),
                                                        outputs=dl.FunctionIO(type='Json', name='item_id_obj')),
                                     dl.PackageFunction(name='json_to_item',
                                                        inputs=dl.FunctionIO(type='Json', name='json_obj'),
                                                        outputs=dl.FunctionIO(type='Item', name='item'))
                                     ])
package = project.packages.push(package_name=package_name,
                                modules=module,
                                src_path=src_path)

# package = project.packages.get(package_name=package_name)

##################
# create service #
##################
service = package.services.deploy(service_name=package.name,
                                  runtime=dl.KubernetesRuntime(pod_type=dl.InstanceCatalog.REGULAR_XS))

# service = package.services.get(package_name)
# service.package_revision = package.version
# service.update()
