import dtlpy as dl

class Scripts:
    def func1(self):
        import dtlpy as dl
        if dl.token_expired():
          dl.login()

    def func2(self):
        project = dl.projects.get(project_name='My Project')
        dataset = project.datasets.get(dataset_name='My Dataset')
        recipe = dataset.recipes.list()[0]
        service = project.services.get(service_name='My Service')
        function_name = 'My Function'

    def func3(self):
        pipeline = project.pipelines.create(name='my-pipeline')

    def func4(self):
        dataset_node = dl.DatasetNode(name='My Dataset Node', dataset_id=dataset.id,
                                    project_id=project.id, position=(1, 1))

    def func5(self):
        task_node = dl.TaskNode(name='My Task',project_id=project.id,dataset_id=dataset.id,
                            recipe_id=recipe.id,recipe_title=recipe.title,task_owner='owner',
                            workload=[dl.WorkloadUnit(assignee_id='assignee_id', load=100)], position=(2, 1))

    def func6(self):
        function_node = dl.FunctionNode(name=service.name, position=(3, 1), service=service,
                                      function_name=function_name)

    def func7(self):
        pipeline.nodes.add(node=dataset_node).connect(task_node).connect(function_node)

    def func8(self):
        # Adding an Event trigger to the dataset node (Default settings: upon item creation)
        dataset_node.add_trigger(trigger_type=dl.TriggerType.EVENT)

    def func9(self):
        pipeline.update()
        pipeline.install()

    def func10(self):
        pipeline.open_in_web()
