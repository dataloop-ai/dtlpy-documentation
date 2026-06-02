# Pipelines and Automation: Building Smart Workflows 🔄

Learn how to create and manage pipelines in Dataloop - your key to automating workflows and data processing.

## Project Setup ⚙️

### Dataloop Login 🔐

```python
import dtlpy as dl
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key securely
api_key = os.getenv('DTLPY_API_KEY')

print(f"API key: {api_key[:20]}...  ")

# Initialize Dataloop with the API key
dl.login_api_key(api_key=api_key)
```
### Project Setup

```python
# Set your project and dataset names
project_name = "onboarding-project"

try:
    # Try to get existing project
    project = dl.projects.get(project_name=project_name)
    print(f"Project '{project_name}' already exists")
except Exception:
    project = dl.projects.create(project_name=project_name)
    # Create project if it doesn't exist
    print(f"Created project '{project_name}'")
```

## Getting Started with Pipelines 🚀

Build the **`rag-pdf-processor`** pipeline programmatically using the Dataloop SDK.

## Pipeline Flow
```
[Source Dataset (ds-source)]  →  [PDF to Chunks]  →  [Chunks Dataset (ds-chunk)]
```

| Node | Type | Description |
|------|------|-------------|
| Source Dataset | Storage | Reads PDF items from the source dataset |
| PDF to Chunks | Custom (RAG PDF Processor) | Splits PDFs into text chunks |
| Chunks Dataset | Storage | Stores the generated chunk items |

## Building the Pipeline 🔨

### 1. Creating a Pipeline

```python
# Create a new pipeline
pipeline = project.pipelines.create(name='My-First-Pipeline')

# Print pipeline details
print(pipeline)
```

### 2. Getting Existing Pipelines

```python
# Get pipeline by ID
pipeline = project.pipelines.get(pipeline_id=pipeline.id)

# List all pipelines in project
project.pipelines.list()
```

### 3. Building Pipeline

Learn how to construct a pipeline by adding nodes, connecting them with filters, and installing the pipeline to process PDF files into chunks.

#### 1. Preparing the Pipeline Ingredients

```python
# Create datasets ─────────────────────────────────────────────
dataset_pdf = project.datasets.create(dataset_name='pdf-source')
dataset_pdf_chunk = project.datasets.create(dataset_name='pdf-chunks')
```

```python
# Install RAG PDF Processor DPK ──────────────────────────────
dpk = dl.dpks.get(dpk_name='rag-pdf-processor')

try:
    app = project.apps.install(dpk=dpk)
    print(f"App installed: {app.name}")
except Exception as e:
    if 'already installed' in str(e):
        print(f"App already installed, getting existing...")
        app = project.apps.get(app_name=dpk.display_name)
        print(f"App found: {app.name}")
    else:
        raise e
```

```python
# After installing the app, find the PDF processor service in the project.
# DPK services may be deployed with a different name than the original project.

pdf_service = None

# Try by exact name first
try:
    pdf_service = project.services.get(service_name='pdf-processor-service')
    print(f"Service found: {pdf_service.name} ({pdf_service.id})")
except Exception:
    # Search all project services by package name
    print("Searching project services...")
    for svc in project.services.list().items:
        print(f"  - {svc.name}  (package: {svc.package_name})")
        if svc.package_name == 'rag-pdf-processor':
            pdf_service = svc

if pdf_service:
    print(f"\nUsing service: {pdf_service.name} ({pdf_service.id})")
else:
    raise Exception(
        "PDF processor service not found in project.\n"
        "The app installed but did not deploy its service automatically.\n"
        "Go to the project in the Web UI → Apps → RAG PDF Processor → and check its services."
    )

```

#### 2. Pipeline Construction

```python
import dtlpy as dl


# Build pipeline ──────────────────────────────────────────────
# PDF dataset source
dataset_node = dl.DatasetNode(
    name='PDF Source',
    project_id=project.id,
    dataset_id=dataset_pdf.id,
    position=(1, 1)
)

# PDF to Chunks function
function_node = dl.FunctionNode(
    name='PDF to Chunks',
    service=pdf_service,
    function_name='run',
    position=(2, 1),
    project_id=project.id
)

# Chunks output dataset
output_node = dl.DatasetNode(
    name='Chunks Output',
    project_id=project.id,
    dataset_id=dataset_pdf_chunk.id,
    position=(3, 1)
)


# Connect: source → function (PDF only) → output
pdf_filter = dl.Filters()
pdf_filter.add(field='metadata.system.mimetype', values='application/pdf')

pipeline.nodes.add(node=dataset_node).connect(
    node=function_node,
    filters=pdf_filter
).connect(
    node=output_node
)

pipeline.update()
pipeline.install()
print(f"Pipeline ready: {pipeline.name} ({pipeline.id})")
```

#### 3. You just created your first pipeline! 🎉

```python
# explore the new pipeline in Web UI
pipeline.open_in_web()
```

### 4. Pipeline Execution

```python
# Upload a PDF and execute ────────────────────────────────────

item = dataset_pdf.items.upload(
    local_path=r'local_path_to_your_pdf',
    remote_path='/'
)
print(f"Uploaded: {item.name} ({item.id})")

pipeline_execution = pipeline.pipeline_executions.create(
    pipeline_id=pipeline.id,
    execution_input=[dl.FunctionIO(type=dl.PackageInputType.ITEM, value=item.id, name='item')]
)

print(f"Execution started: {pipeline_execution.id}")
```

## Pipeline Management 📋

### 1. Basic Operations

```python
# Delete a pipeline
is_deleted = project.pipelines.delete(pipeline_id='<pipeline_id>')

# Open pipeline in web UI
project.pipelines.open_in_web(pipeline_id='<pipeline_id>')

# Pause pipeline
project.pipelines.pause(pipeline='pipeline_entity')

# Reset pipeline
project.pipelines.reset(pipeline='pipeline_entity')
```

### 2. Pipeline Monitoring

```python
# Get pipeline statistics
project.pipelines.stats(pipeline='pipeline_entity')

# Get pipeline execution object
pipeline_executions = pipeline.pipeline_executions.get(pipeline_id='pipeline_id')

# List project pipeline executions
pipeline.pipeline_executions.list()
```

## Best Practices 👑

### 1. Pipeline Organization
- Use clear, descriptive pipeline names
- Document pipeline purpose and configuration
- Keep track of pipeline versions
- Monitor pipeline executions

### 2. Error Prevention

```python
# Validate pipeline before operations
try:
    pipeline = project.pipelines.get(pipeline_id='pipeline_id')
    # Proceed with operations
except dl.exceptions.NotFound:
    print("Pipeline not found!")
```

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
