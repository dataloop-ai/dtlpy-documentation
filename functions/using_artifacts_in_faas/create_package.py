import os.path

import dtlpy as dl

project_name = 'COCO ors'
package_name = 'artifacts-package'

module = dl.PackageModule(
    entry_point='main.py',
    class_name='ServiceRunner',
    init_inputs=[dl.FunctionIO(type=dl.PackageInputType.STRING, name="artifact_filename")],
    functions=[
        dl.PackageFunction(
            name='run',
            description='Function example for using artifacts'
        )
    ])

project = dl.projects.get(project_name=project_name)

package = project.packages.push(
    package_name=package_name,
    modules=[module],
    src_path=os.path.join('functions', 'using_artifacts_in_faas'))

artifact_zip_file = os.path.join('assets', 'artifacts', 'monkey-612x612.zip')
package.artifacts.upload(filepath=artifact_zip_file,
                         package=package,
                         package_name=package.name)

service = package.services.deploy(package=package,
                                  init_input=dl.FunctionIO(type=dl.PackageInputType.STRING,
                                                           name='artifact_filename',
                                                           value='monkey-612x612.zip'),
                                  runtime=dl.KubernetesRuntime(concurrency=1,
                                                               autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                   min_replicas=0,
                                                                   max_replicas=1,
                                                                   queue_length=10))
                                  )
