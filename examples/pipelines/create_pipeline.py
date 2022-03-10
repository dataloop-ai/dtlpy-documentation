import dtlpy as dl


def metadata_function_first(item: dl.Item):
    item.metadata['user']['first'] = 'Hello'
    item.update(system_metadata=True)
    return item


def metadata_function_second(item: dl.Item):
    item.metadata['user']['second'] = 'World'
    item.update(system_metadata=True)
    return item


def create_pipeline(project_name, dataset_name, service_name=None, function_name=None):
    project = dl.projects.get(project_name=project_name)
    dataset = project.datasets.get(dataset_name=dataset_name)
    print('Initialized params project_name:{}, dataset_name:{}'.format(project.name, dataset.name))
    #############################################
    # Publish new package and deploy as service #
    #############################################
    if service_name is not None:
        service = project.services.get(service_name=service_name)
        print('Using existing service name: {}'.format(service.name))
    else:
        function_name = 'metadata_function_second'
        service = project.services.deploy(func=metadata_function_second,
                                          service_name='metadata-function-second')
        print('Service was created service_name:{}'.format(service.name))
    ##########################################
    # Generate pipeline with relevant params #
    ##########################################
    recipe = dataset.recipes.list()[0]
    pipeline = project.pipelines.create(name='pipeline-faas-example-dataset')

    code_node = dl.CodeNode(
        name='My Function',
        position=(1, 1),
        project_id=project.id,
        method=metadata_function_first,
        project_name=project.name
    )

    task_node = dl.TaskNode(
        name='My Task',
        recipe_id=recipe.id,
        recipe_title=recipe.title,
        task_owner='owner',
        workload=[dl.WorkloadUnit(assignee_id='assignee_id', load=100)],
        position=(2, 1),
        project_id=project.id,
        dataset_id=dataset.id,
    )

    function_node = dl.FunctionNode(
        name=service.name,
        position=(3, 1),
        service=service,
        function_name=function_name
    )
    pipeline.nodes.add(node=code_node).connect(node=task_node).connect(node=function_node)
    code_node.add_trigger()
    pipeline.update()

    print('Pipeline was created pipeline_name:{}'.format(pipeline.name))
    ###########################
    # Installing the pipeline #
    ###########################
    print('Installing pipeline')
    pipeline.install()
    print('Opening pipeline in console...')
    pipeline.open_in_web()

    ###############
    # Cleaning up #
    ###############
    # dataset.delete()
    # service.delete()
    # pipeline.delete()


if __name__ == "__main__":
    project_name = 'My Project pipeline example'
    dataset_name = 'pipeline-faas-example-dataset'
    service_name = None  # or existing service name in the project
    function_name = 'run'  # when using existing service
    create_pipeline(project_name=project_name,
                    service_name=service_name,
                    dataset_name=dataset_name,
                    function_name=function_name)
