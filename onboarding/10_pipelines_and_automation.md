# Pipelines and Automation: Building Smart Workflows 🔄

Learn how to create and manage pipelines in Dataloop - your key to automating workflows and data processing.

## Dataloop Login 🔐

> ```python
> import dtlpy as dl
> from dtlpy.entities.node import PipelineNodeIO
> from dotenv import load_dotenv
> import os
>
> # Load environment variables from .env file
> load_dotenv()
>
> # Access your API key securely
> api_key = os.getenv('DTLPY_API_KEY')
>
> print(f"API key: {api_key[:20]}...  ")
>
> # Initialize Dataloop with the API key
> dl.login_api_key(api_key=api_key)
> ```

## Project and Dataset Setup

> ```python
> # Set your project and dataset names
> project_name = "onboarding-project-9"
>
> try:
>     # Try to get existing project
>     project = dl.projects.get(project_name=project_name)
>     print(f"Project '{project_name}' already exists")
> except Exception:
>     project = dl.projects.create(project_name=project_name)
>     # Create project if it doesn't exist
>     print(f"Created project '{project_name}'")
> ```

> ```python
> project.print()
> ```

## Getting Started with Pipelines 🚀

### 1. Pipeline Flow Diagram

> ```
> ┌─────────────────┐       ┌─────────────────────┐
> │   DatasetNode   │       │  FunctionNode (ML)  │
> │ (source-dataset)│ ----> │ (mobilenet-predict) │
> │  Position: (1,1)│       │   Position: (2,1)   │
> └─────────────────┘       └─────────────────────┘
> ```

### 2. Creating a Pipeline

> ```python
> # Create a new pipeline
> pipeline = project.pipelines.create(name='My-First-Pipeline')
>
> # Print pipeline details
> print(pipeline)
> ```

### 3. Getting Existing Pipelines

> ```python
> # Get pipeline by ID
> pipeline = project.pipelines.get(pipeline_id=pipeline.id)
>
> # List all pipelines in project
> project.pipelines.list()
> ```

### 4. Pipeline Ingredients

> ```python
> # Create datasets ─────────────────────────────────────────────
> dataset_source = project.datasets.create(dataset_name='ds-model-source')
> ```

> ```python
> # Check if model is already installed on roject
> model_name = "mobilenet"
> try:
>     model = project.models.get(model_name=model_name)
> except Exception:
>     model_dpk = dl.dpks.get(dpk_name="mobilenet")
>     print(f"App '{model_dpk.name}' not found, installing...")
>     model_app = project.apps.install(dpk=model_dpk)
>     model = project.models.get(model_name=model_name)
> ```

> ```python
> # Deploy model with default configuration
> model_service = model.deploy()
> service_id = model_service.id
>
> # Print service details
> model_service.print()
> ```

### 3. Pipeline Constructions

> ```python
> # Dataset source
> dataset_node = dl.DatasetNode(
>     name='source-dataset',
>     project_id=project.id,
>     dataset_id=dataset_source.id,
>     position=(1, 1),
> )
>
> # Create ML predict node
> # Since Dataloop has no dedicated ML node class, we convert a FunctionNode:
> # - Set node_type to ML
> # - Link to the model via metadata.modelId
> # - Link to the installed app for UI function picker resolution
> # - Use standard Item -> Item ports
> # - function_name is a model lifecycle action: train | predict | evaluate | embed
> app = next(a for a in project.apps.list().all() if a.dpk_name == 'mobilenet')
> item_port = PipelineNodeIO(
>     input_type=dl.PackageInputType.ITEM, name='item', display_name='item', actions=[],
> )
>
> predict_node = dl.FunctionNode(
>     name='mobilenet-predict',
>     service=model_service,
>     function_name='predict',
>     project_id=project.id,
>     position=(2, 1),
> )
> predict_node.node_type = dl.PipelineNodeType.ML
> predict_node.metadata['modelId'] = model.id
> predict_node.app_id, predict_node.app_name, predict_node.dpk_name = app.id, app.name, app.dpk_name
> predict_node.inputs = [item_port]
> predict_node.outputs = [item_port]
>
> print(f'Predict node ready: model={model.name!r}  app={app.name!r}')
> ```

### 4. Pipeline Installation

> ```python
> # Connect nodes and install pipeline
> pipeline.nodes.add(node=dataset_node).connect(node=predict_node)
> pipeline.update()
> pipeline.install()
> print(f'Pipeline ready: {pipeline.name} ({pipeline.id})')
> ```

### You just created your first pipeline!

> ```python
> # explore the new pipeline in Web UI
> pipeline.open_in_web()
> ```

### 3. Pipeline Execution

> ```python
> item = dataset_source.items.upload(
>     local_path=r"C:\Users\Yigal_Pinhasi\OneDrive - Dell Technologies\Pictures\dogs\dog3.jpg",
>     remote_path='/'
> )
>
> print(f"Uploaded: {item.name} ({item.id})")
>
> pipeline_execution = pipeline.pipeline_executions.create(
>     pipeline_id=pipeline.id,
>     execution_input=[dl.FunctionIO(type=dl.PackageInputType.ITEM, value=item.id, name='item')]
> )
> print(f"Execution started: {pipeline_execution.id}")
>
> pipeline.open_in_web()
> ```

## Pipeline Management 📋

### 1. Basic Operations

> ```python
> # Delete a pipeline
> is_deleted = project.pipelines.delete(pipeline_id='<pipeline_id>')
>
> # Open pipeline in web UI
> project.pipelines.open_in_web(pipeline_id='<pipeline_id>')
>
> # Pause pipeline
> project.pipelines.pause(pipeline='pipeline_entity')
>
> # Reset pipeline
> project.pipelines.reset(pipeline='pipeline_entity')
> ```

### 2. Pipeline Monitoring

> ```python
> # Get pipeline statistics
> project.pipelines.stats(pipeline='pipeline_entity')
>
> # Get pipeline execution object
> pipeline_executions = pipeline.pipeline_executions.get(pipeline_id='pipeline_id')
>
> # List project pipeline executions
> pipeline.pipeline_executions.list()
> ```

## Best Practices 👑

### 1. Pipeline Organization
- Use clear, descriptive pipeline names
- Document pipeline purpose and configuration
- Keep track of pipeline versions
- Monitor pipeline executions

### 2. Error Prevention

> ```python
> # Validate pipeline before operations
> try:
>     pipeline = project.pipelines.get(pipeline_id='pipeline_id')
>     # Proceed with operations
> except dl.exceptions.NotFound:
>     print("Pipeline not found!")
> ```

### 3. Resource Management
- Monitor pipeline statistics regularly
- Clean up unused pipelines
- Document pipeline configurations
- Test pipelines before production use

## Pro Tips 💡

1. **Pipeline Design**
   - Plan pipeline flow before creation
   - Use meaningful node names
   - Document pipeline inputs and outputs
   - Consider error handling at each step

2. **Execution Management**
   - Monitor pipeline executions
   - Handle execution errors gracefully
   - Keep track of execution statistics
   - Document common issues and solutions

3. **Pipeline Maintenance**
   - Regularly check pipeline status
   - Update pipeline configurations as needed
   - Monitor resource usage
   - Document pipeline changes


Ready to explore integrations and APIs? Let's move on to the next chapter! 🚀
