# Model Management: Your AI Model's Lifecycle 🤖

Learn how to manage your machine learning models in Dataloop - from development to deployment and monitoring.

## Dataloop Login 🔐

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

## Project and Dataset Setup

```python
# Create your project and dataset (or get if they already exist)

# Set your project and dataset names
project_name = "onboarding-project-1"
dataset_name = "onboarding-dataset-1"

try:
    # Try to get existing project
    project = dl.projects.get(project_name=project_name)
    print(f"Project '{project_name}' already exists")
except Exception:
    project = dl.projects.create(project_name=project_name)
    # Create project if it doesn't exist
    print(f"Created project '{project_name}'")

try:
    # Try to get existing dataset
    dataset = project.datasets.get(dataset_name=dataset_name)
    print(f"Dataset '{dataset_name}' already exists")

except Exception:
    # Create dataset if it doesn't exist
    dataset = project.datasets.create(dataset_name=dataset_name)
    print(f"Created dataset '{dataset_name}'")
```

### Dataset repopulate

```python
# Clear the dataset and repopulate it with new items without metadata attribution
# You can skip or comment out this cell if it's not needed

# Empty dataset - delete all dataset items
for item in dataset.items.list().all():
    item.delete()

# Upload entire directory
dataset.items.upload(
    # Set the local folder path 
    local_path='/path/to/folder',
    remote_path='/batch-upload',
)

dataset.items.list().print()
```

## Getting Started with Models 🚀

### 1. Basic Model Setup

```python
# Check if model is already installed on project
model_name = "mobilenet"
try:
    model = project.models.get(model_name=model_name)
except Exception:
    model_dpk = dl.dpks.get(dpk_name="mobilenet")
    print(f"App '{model_dpk.name}' not found, installing...")
    model_app = project.apps.install(dpk=model_dpk)
    model = project.models.get(model_name=model_name)
```

```python
model.print()
project.models.list().print()
```

### 2. Model Configuration

```python
model.configuration

print(model.configuration)

# Set model configuration
model.configuration = {
    'weights_filename': 'weights.pth',
    'input_size': 640,
    'batch_size': 32,
    'num_classes': 3,
    'confidence_threshold': 0.5
}
model.update()

print(model.configuration)
```

### 3. Model Cloning

```python
model_cloned = model.clone(
# Clone a model for fine-tuning
    model_name='my-model-v2',
    dataset=dataset,
    project_id=project.id,
    labels=['car', 'truck', 'bus']  # Updated labels
)
```

```python
project.models.list().print()
```

### 4. Upload/Download Model Artifacts

```python
# Upload
model_cloned.artifacts.upload(
    filepath='/path/to/weights.pth',
    artifact_name='model_weights'
)

# Download
model_cloned.artifacts.download(
    local_path='/path/to/download'
)
```

## Model Deployment 🌟

### 1. Basic Deployment

```python
# Deploy model with default configuration
deployment = model.deploy()

# Deploy with custom configuration
deployment = model.deploy(
    service_config={
        'runtime': {
            'gpu': True,
            'numReplicas': 1,
            'concurrency': 1,
            'podType': dl.InstanceCatalog.GPU_T4_M
        }
    }
)
```

### 2. Advanced Deployment Options

```python
# Deploy with auto-scaling
deployment = model.deploy(
    service_config={
        'runtime': {
            'podType': dl.InstanceCatalog.GPU_T4_S,
            'autoscaler': {
                'type': 'rabbitmq',
                'minReplicas': 0,
                'maxReplicas': 3,
                'queueLength': 10
            }
        },
        'executionTimeout': 60 * 10,  # 10 minutes
        'initTimeout': 60 * 5  # 5 minutes
    }
)
```

```python
project.services.list().print()
```

## Model Inference 🎯

### 1. Single Item Prediction

```python
# Get an item
item = dataset.items.list().items[0]

# Run prediction
prediction = model.predict(item_ids=[item.id])

# Wait for results
prediction.wait()
prediction_status = prediction.status
```

```python
# Explore tagged item in Dataloop Dashboard
dataset.open_in_web()
```

### 2. Batch Predictions

```python
# Create filters for items
filters = dl.Filters()

# Set filter value
filters.add(field='dir', values='/folder/to/predict')

dataset.items.list(filters=filters).print()
# Run batch prediction
items = dataset.items.list(filters=filters)
item_ids = [item.id for item in items.all()]

batch_prediction = model.predict(
    item_ids=item_ids,
    dataset_id=dataset.id
)

batch_prediction_status = batch_prediction.wait()
```

```python
# View prediction annotations results from annotations
print("=== Prediction Results ===")


# Get the items with their annotations
for item_id in item_ids:
    item = dataset.items.get(item_id=item_id)
    print(f"\nItem: {item.name} (ID: {item.id})")
    
    # Get annotations for this item
    annotations = list(item.annotations.list())
    print(f"Number of annotations: {len(annotations)}")


    for annotation in annotations:
        print(f"Label: {annotation.label}, type:{annotation.type}")
```

```python
# explore the dataset annotations in Dataloop platform
dataset.open_in_web()
```

## Model Training 🎓

### 1. Basic Training

```python
import datetime
# Clone the base model for training
model_cloned = model.clone(
    model_name='my-model-v2',
    dataset=dataset,
    project_id=project.id
)
```

```python
# label the dataset 
# Get unique labels from existing annotations
labels = set()
for item in dataset.items.list().all():
    for annotation in item.annotations.list():
        labels.add(annotation.label)
 
print("Existing labels:", labels)
 
# Add these labels to dataset recipe
label_list = list(labels)

# Check if model_cloned has a dataset
print(f"Dataset ID: {model_cloned.dataset_id}")

dataset.add_labels(label_list=label_list)

# If None, set it and update
model_cloned.dataset_id = dataset.id
model_cloned.update()
```

```python
# Split dataset into ML subsets
filters = dl.Filters(field='type', values='file')

# Randomly split dataset items into train/validation/test subsets
# by tagging each item's system metadata (metadata.system.tags.train/validation/test)
# This is required before training so the model knows which items to use for each phase
dataset.split_ml_subsets(
    items_query=filters,
    percentages={'train': 80, 'validation': 20, 'test': 0}
)

# Create filters based on ML subset tags
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
validation_filters = dl.Filters(field="metadata.system.tags.validation", values=True)
 
# Add subsets to the model
model_cloned.add_subset(subset_name="train", subset_filter=train_filters)
model_cloned.add_subset(subset_name="validation", subset_filter=validation_filters)
 
model_cloned.configuration = {
    'batch_size': 16,
    'num_epochs': 5,
    'lr': 0.0001,
    'optimizer': 'adam'
}

# Update with system metadata
model_cloned.update(system_metadata=True)
 
# Now train
train_execution = model_cloned.train()
print(f"Training started - Execution ID: {train_execution.id}")

# Monitor training
train_execution = train_execution.wait()
print(f"Training status: {train_execution.latest_status['status']}")
```

### 2. Advanced Training Options

```python
# Train with data splitting and validation
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
validation_filters = dl.Filters(field="metadata.system.tags.validation", values=True)

cloned_model = model.clone(
    model_name='cloned-model',
    dataset=dataset,
    train_filter=train_filters,
    validation_filter=validation_filters,
    configuration={
        'epochs': 100,
        'batch_size': 32,
        'learning_rate': 0.001,
        'early_stopping': {
            'patience': 5,
            'min_delta': 0.001
        },
        'augmentation': {
            'horizontal_flip': True,
            'rotation_range': 20,
            'zoom_range': 0.2
        }
    }
)
train_execution = cloned_model.train()
train_status = train_execution.wait()
print(f"Training status: {train_status.latest_status['status']}")
```

### 3. Training Monitoring

Log in to the Dataloop platform and check the training status and metrics.

## Best Practices 👑

### 1. Model Organization

- Use clear naming conventions
- Document model changes
- Track experiment configurations
- Maintain version history

Ready to explore FaaS (Functions as a Service)? Let's move on to the next chapter! 🚀
