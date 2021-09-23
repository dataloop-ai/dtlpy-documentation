import dtlpy as dl

dl.setenv('prod')

package_name = 'logs-function'
project_name = 'COCO ors'

project = dl.projects.get(project_name=project_name)

###############
# push plugin #
###############

modules = dl.PackageModule(name='default',
                           entry_point='main.py',
                           functions=[dl.PackageFunction(name='run',
                                                         inputs=dl.FunctionIO(type='Item', name='item'))])
package = project.packages.push(package_name=package_name,
                                modules=modules,
                                src_path='functions/view_service_logs')
package = project.packages.get(package_name=package_name)
package.print()

#####################
# create deployment #
#####################
service = package.services.deploy(service_name=package.name,
                                  package=package,
                                  runtime={'gpu': False,
                                           'numReplicas': 1,
                                           'concurrency': 32,
                                           },
                                  module_name='default'
                                  )
print('Service deployed successfully!')
service = package.services.get(service_name=package.name)
service.package_revision = package.version
service.update()

######################
# execute a Function #
######################
service = package.services.get(service_name='dummy-function')
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
execution = service.execute(execution_input=[dl.FunctionIO(type='Item',
                                                           value={'item_id': item.id},
                                                           name='item')],
                            function_name='run')

# stream logs with follow
execution.logs(follow=True)
