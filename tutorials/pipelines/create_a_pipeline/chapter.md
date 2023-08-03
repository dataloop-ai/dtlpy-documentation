# Pipeline Tutorial  
This tutorial will help you get started with pipelines.  
  
First, log in to the platform by running the following Python code in the terminal or your IDE:  
  

```python
import dtlpy as dl
if dl.token_expired():
  dl.login()
```
Your browser will open a login screen, allowing you to enter your credentials or log in with Google. Once the "Login Successful" tab appears, you are allowed to close it.  
  
This tutorial requires a project, dataset and an up and running service. You can begin by retreiving the required inputs:  
  

```python
project = dl.projects.get(project_name='My Project')
dataset = project.datasets.get(dataset_name='My Dataset')
recipe = dataset.recipes.list()[0]
service = project.services.get(service_name='My Service')
function_name = 'My Function'
```
Next, create pipeline in your specified project:  
  

```python
pipeline = project.pipelines.create(name='my-pipeline')
```
You can create nodes based on your requirement and process flow. Below are examples of Dataset, Task and Function nodes where the position argument specifies the node placement.  
  

```python
dataset_node = dl.DatasetNode(name='My Dataset Node', dataset_id=dataset.id,
                            project_id=project.id, position=(1, 1))
```
For the task node, email IDs of the task owner as well as the assignees and their respective loads.  
  

```python
task_node = dl.TaskNode(name='My Task',project_id=project.id,dataset_id=dataset.id,
                    recipe_id=recipe.id,recipe_title=recipe.title,task_owner='owner',
                    workload=[dl.WorkloadUnit(assignee_id='assignee_id', load=100)], position=(2, 1))
```
As for the Function Node, the service name and function to be executed must be specified.  
  

```python
function_node = dl.FunctionNode(name=service.name, position=(3, 1), service=service,
                              function_name=function_name)
```
Once the required nodes are created, they can be added to the pipeline in the correct order:  
  

```python
pipeline.nodes.add(node=dataset_node).connect(task_node).connect(function_node)
```
If a trigger is required, it can be added to a specific node:  
  

```python
# Adding an Event trigger to the dataset node (Default settings: upon item creation)
dataset_node.add_trigger(trigger_type=dl.TriggerType.EVENT)
```
Finally, the pipeline is updated and installed:  
  

```python
pipeline.update()
pipeline.install()
```
To view the newly installed pipeline in the UI:  
  

```python
pipeline.open_in_web()
```
