# Creating Pipelines: Building Automated Workflows 🔄

This tutorial will help you master pipeline creation in Dataloop, covering all node types and their advanced features.

## Prerequisites 🎯

First, log in to the platform:

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
```

Get your project and required resources:

```python
project = dl.projects.get(project_name='My Project')
dataset = project.datasets.get(dataset_name='My Dataset')
recipe = dataset.recipes.list()[0]
service = project.services.get(service_name='My Service')
function_name = 'My Function'
```

## Creating a Pipeline 🚀

Create a new pipeline in your project:

```python
pipeline = project.pipelines.create(name='my-pipeline')
```

## Node Types and Configuration 🛠️

### 1. Dataset Node

The Dataset Node serves as a data source or sink in your pipeline:

```python
dataset_node = dl.DatasetNode(
    name='My Dataset Node',
    project_id=project.id,
    dataset_id=dataset.id,
    dataset_folder='/specific/folder',  # Optional - work in specific folder
    load_existing_data=True,  # Optional - load existing items
    data_filters=dl.Filters(field='dir', values='/folder'),  # Optional - filter items
    position=(1, 1)
)
```

### 2. Task Node

The Task Node creates annotation or QA tasks:

```python
task_node = dl.TaskNode(
    name='My Task',
    project_id=project.id,
    dataset_id=dataset.id,
    recipe_id=recipe.id,
    recipe_title=recipe.title,
    task_owner='owner@domain.com',
    workload=[dl.WorkloadUnit(assignee_id='assignee@domain.com', load=100)],
    task_type='annotation',  # or 'qa'
    position=(2, 1),
    due_date=(datetime.datetime.now() + datetime.timedelta(days=7)).timestamp() * 1000,
    # Optional parameters
    priority=dl.TaskPriority.MEDIUM,
    groups=['team1', 'team2'],  # Optional - assign to specific groups
    # Consensus parameters (optional)
    consensus_task_type=dl.ConsensusTaskType.REGULAR,
    consensus_percentage=20,  # Percentage of items for consensus
    consensus_assignees=2  # Number of assignees per consensus item
)
```

### 3. Function Node

The Function Node executes service functions:

```python
function_node = dl.FunctionNode(
    name=service.name,
    service=service,
    function_name=function_name,
    position=(3, 1),
    project_id=project.id,  # Optional - defaults to service project
    project_name='MyProject'  # Optional - defaults to service project
)
```

### 4. Code Node

The Code Node allows inline code execution:

```python
def process_item(item, string):
    """Custom processing logic"""
    item.metadata['user'] = {'userInput': string}
    item.update()
    return item

code_node = dl.CodeNode(
    name='Process Item',
    project_id=project.id,
    method=process_item,
    position=(4, 1),
    project_name=project.name
)
```

## Building the Pipeline Flow 🔗

### 1. Adding Nodes

Add nodes to your pipeline and connect them in sequence:

```python
pipeline.nodes.add(node=dataset_node).connect(task_node).connect(function_node).connect(code_node)
```

### 2. Advanced Node Connections

Connect nodes with filters and specific ports:

```python
# Connect with filters
task_node.connect(
    node=function_node,
    filters=dl.Filters(field='status', values='completed'),
    action='complete'  # Trigger on specific action
)

# Connect specific ports
source_port = task_node.outputs[0]  # Get first output port
target_port = function_node.inputs[0]  # Get first input port
task_node.connect(
    node=function_node,
    source_port=source_port,
    target_port=target_port
)
```

### 3. Adding Triggers

Add event or cron triggers to start nodes:

```python
# Event trigger (e.g., on item creation)
dataset_node.add_trigger(
    trigger_type=dl.TriggerType.EVENT,
    resource=dl.TriggerResource.ITEM,
    actions=dl.TriggerAction.CREATED,
    filters=dl.Filters(field='dir', values='/incoming')
)

# Cron trigger (scheduled execution)
dataset_node.add_trigger(
    trigger_type=dl.TriggerType.CRON,
    cron='0 0 * * *'  # Run daily at midnight
)
```

## Finalizing and Managing the Pipeline 📋

### 1. Update and Install

Save your changes and deploy the pipeline:

```python
pipeline.update()
pipeline.install()
```

### 2. Pipeline Management

```python
# Open in web UI
pipeline.open_in_web()

# Delete pipeline
project.pipelines.delete(pipeline_id=pipeline.id)
```

## Best Practices 💡

1. **Node Positioning**
   - Use meaningful positions for visual clarity
   - Keep flow direction consistent (usually left to right)
   - Avoid overlapping nodes

2. **Error Handling**
   - Add error handling in code nodes
   - Use filters to control flow based on success/failure
   - Monitor node execution status

3. **Resource Management**
   - Clean up completed executions
   - Monitor resource usage
   - Use appropriate timeouts

4. **Documentation**
   - Add clear node names and descriptions
   - Document expected inputs and outputs
   - Maintain pipeline version history

Need help? Check our [Pipeline documentation](https://docs.dataloop.ai/docs/pipelines-overview) for more details! 🚀
