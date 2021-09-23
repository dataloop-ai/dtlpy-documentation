import dtlpy as dl
import os
import json


def create_and_deploy_faas(project_id, package_name):
    module = dl.PackageModule(
        entry_point='pipeline_faas.py',
        class_name='ServiceRunner',
        functions=[
            dl.PackageFunction(
                name='automate',
                inputs=[
                    dl.FunctionIO(type="Item", name="item")
                ],
                outputs=[
                    dl.FunctionIO(type="Item", name="item")
                ],
                description=''
            )
        ])
    project = dl.projects.get(project_id=project_id)
    package = project.packages.push(
        package_name=package_name,
        modules=[module],
        src_path=os.path.join(os.getcwd(), "pipelines")
    )

    # deploy the service for the first time
    service = package.services.deploy(package=package,
                                      runtime=dl.KubernetesRuntime(concurrency=1,
                                                                   autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                       min_replicas=0,
                                                                       max_replicas=1,
                                                                       queue_length=10),
                                                                   pod_type=dl.InstanceCatalog.REGULAR_XS)
                                      )
    return service


def create_pipeline_from_json(service: dl.Service, dataset: dl.Dataset) -> dl.Pipeline:
    pipeline_template_path = os.path.join(os.getcwd(), "pipelines/pipeline_template.json")
    recipe_id = dataset.metadata.get('system', dict())['recipes'][0]
    recipe = dl.recipes.get(recipe_id=recipe_id)
    with open(pipeline_template_path, 'r') as f:
        pipeline_json = json.load(f)

    pipeline_json['name'] = 'pipeline-faas-example'
    pipeline_json['projectId'] = service.project.id

    pipeline_json['nodes'][0]['namespace']['serviceName'] = service.name
    pipeline_json['nodes'][0]['namespace']['packageName'] = service.package.name
    pipeline_json['nodes'][0]['namespace']['projectName'] = service.project.name
    pipeline_json['nodes'][0]['projectId'] = service.project.id

    pipeline_json['nodes'][1]['metadata']['recipeTitle'] = recipe.title
    pipeline_json['nodes'][1]['metadata']['recipeId'] = recipe.id

    pipeline_json['nodes'][2]['namespace']['projectName'] = service.project.name

    pipeline = service.project.pipelines.create(pipeline_json=pipeline_json)
    return pipeline
