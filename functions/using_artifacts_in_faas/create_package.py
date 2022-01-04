import os.path

import dtlpy as dl

project_name = 'project_name'
package_name = 'artifacts-package'

module = dl.PackageModule(
    entry_point='main.py',
    class_name='ServiceRunner',
    init_inputs=[dl.FunctionIO(type=dl.PackageInputType.STRING, name="weight_path")],
    functions=[
        dl.PackageFunction(
            name='run',
            inputs=[
                dl.FunctionIO(type="Item", name="item")
            ],
            description=''
        )
    ])

project = dl.projects.get(project_name=project_name)

package = project.packages.push(
    package_name=package_name,
    modules=[module],
    src_path=os.path.join(os.getcwd(), 'functions', 'using_artifacts_in_faas'))

package.artifacts.upload(filepath=os.path.join(os.getcwd(), 'functions', 'using_artifacts_in_faas', 'external_file.py'),
                         package=package,
                         package_name=package.name)

service = package.services.deploy(package=package,
                                  runtime=dl.KubernetesRuntime(concurrency=1,
                                                               autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                   min_replicas=0,
                                                                   max_replicas=1,
                                                                   queue_length=10))
                                  )
