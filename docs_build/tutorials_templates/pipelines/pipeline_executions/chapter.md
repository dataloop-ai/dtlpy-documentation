# Pipeline Executions (Pipeline Cycles): Running Your AI Workflows 🔄

Learn how to execute and manage pipeline runs in Dataloop - from basic execution to advanced node-specific operations.

## Basic Pipeline Execution 🚀

### Execute a Pipeline

```python
import dtlpy as dl

# Get your pipeline
pipeline = project.pipelines.get(pipeline_id='pipeline_id')

# Execute with specific inputs
execution = pipeline.execute(
    execution_input={'item': 'item_id'}
)
```

### Batch Execution

```python
# Execute pipeline on multiple items
execution = pipeline.execute_batch(
    execution_inputs=dl.FunctionIO(
        type=dl.PackageInputType.STRING,
        value='test',
        name='string'
    ),
    filters=dl.Filters(
        field='dir',
        values='/test',
        context={'datasets': ['dataset_id']}
    )
)
```

## Advanced Execution Features 🎯

### Node-Specific Execution

```python
# Execute specific node in pipeline
execution = pipeline.execute(
    node_id='target_node_id',
    execution_input={'item': 'item_id'}
)

# Check execution status
if execution.status == dl.ExecutionStatus.SUCCESS:
    print("Node execution completed successfully!")
```

### Service-Based Execution

```python
# Get pipeline service
service_name = pipeline.nodes[0].namespace.service_name
service = dl.services.get(service_name=service_name)

# Execute service batch
service_execution = service.execute_batch(
    execution_inputs=dl.FunctionIO(
        type=dl.PackageInputType.STRING,
        value='test',
        name='string'
    ),
    filters=dl.Filters(
        field='dir',
        values='/test',
        context={'datasets': ['dataset_id']}
    )
)
```

## Monitoring Executions 📊

### Track Execution Status

```python
# Get execution details
execution = pipeline.pipeline_executions.get(
    pipeline_execution_id='execution_id'
)

# Check status
print(f"Execution status: {execution.status}")

# List all executions
executions = pipeline.pipeline_executions.list()
print(f"Total executions: {executions.items_count}")
```

### Monitor Node Status

```python
def monitor_execution(pipeline, execution_id, timeout=60):
    """Monitor pipeline execution with timeout"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(1)
        execution = pipeline.pipeline_executions.get(
            pipeline_execution_id=execution_id
        )
        
        if execution.status == 'success':
            print("Execution completed successfully!")
            return True
        elif execution.status == 'failed':
            print("Execution failed!")
            return False
            
    print("Execution timed out!")
    return False
```

## Customizing Pipeline Nodes 🛠️

### Update Node Configuration

```python
# Update node runner image
def update_node_runner(pipeline, node_type, image):
    for node in pipeline.nodes:
        if node.node_type == node_type:
            if 'serviceConfig' not in node.metadata:
                node.metadata['serviceConfig'] = {}
            if 'runtime' not in node.metadata['serviceConfig']:
                node.metadata['serviceConfig']['runtime'] = {}
            node.metadata['serviceConfig']['runtime']['runnerImage'] = image
            return pipeline.update()
```

### Add Custom Code Node

```python
# Create a code node
def create_code_node(project, position=(4, 4)):
    def run(item, string):
        # Custom processing logic
        item.metadata['user'] = {'userInput': string}
        item.update()
        return item

    code_node = dl.CodeNode(
        name='codeNode',
        position=position,
        project_id=project.id,
        method=run,
        project_name=project.name
    )
    return code_node
```

## Best Practices 👑

1. **Error Handling**
   ```python
   try:
       execution = pipeline.execute(execution_input={'item': item_id})
   except dl.exceptions.PipelineError as e:
       print(f"Pipeline execution failed: {e}")
   ```

2. **Resource Cleanup**
   ```python
   # Clean up completed executions
   old_executions = pipeline.pipeline_executions.list()
   for execution in old_executions:
       if execution.status in ['success', 'failed']:
           # Archive or handle old executions
           pass
   ```

3. **Execution Monitoring**
   ```python
   def wait_for_completion(execution, timeout=300):
       start_time = time.time()
       while time.time() - start_time < timeout:
           if execution.status == dl.ExecutionStatus.SUCCESS:
               return True
           elif execution.status == dl.ExecutionStatus.FAILED:
               return False
           time.sleep(5)
       return False
   ```

## Pro Tips 💡

1. **Batch Processing**
   - Use filters to process multiple items efficiently
   - Monitor batch execution progress
   - Handle failures gracefully

2. **Performance Optimization**
   - Execute specific nodes when possible
   - Use appropriate timeouts
   - Monitor resource usage

3. **Debugging**
   - Check node-specific logs
   - Monitor execution status
   - Track input/output flow

Need help? Check our [Pipeline documentation](https://docs.dataloop.ai/docs/pipelines-overview) for more details! 🚀
