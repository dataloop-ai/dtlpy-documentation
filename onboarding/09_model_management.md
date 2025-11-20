# Model Management: Your AI Model's Lifecycle 🤖

Learn how to manage your machine learning models in Dataloop - from development to deployment and monitoring.

## Getting Started with Models 🚀

### 1. Basic Model Setup

```python
import dtlpy as dl

# Get your project
project = dl.projects.get(project_name='my-project')

# Create a new model
model = project.models.create(
    model_name='my-awesome-model',
    description='A state-of-the-art object detection model',
    tags=['detection', 'production'],
    dataset_id='dataset-id',  # Optional - link to training dataset
    labels=['car', 'person', 'bike'],  # Model's output labels
    model_artifacts=[dl.LinkArtifact(link='s3://my-bucket/weights.pth')]
)
```

### 2. Model Configuration

```python
# Set model configuration
model.configuration = {
    'weights_filename': 'weights.pth',
    'input_size': 640,
    'batch_size': 32,
    'num_classes': 3,
    'confidence_threshold': 0.5
}
model.update()
```

### 3. Upload/Download Model Artifacts

```python

# Upload
model.artifacts.upload(
    filepath='/path/to/weights.pth',
    artifact_name='model_weights'
)

# Download
model.artifacts.download(
    local_path='/path/to/download'
)
```

### 4. Model Cloning

```python
# Clone a model for fine-tuning
new_model = model.clone(
    model_name='my-model-v2',
    dataset_id='new-dataset-id',
    project_id=project.id,
    labels=['car', 'truck', 'bus']  # Updated labels
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
            'podType': dl.InstanceCatalog.GPU_K80_S
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
            'podType': dl.InstanceCatalog.GPU_K80_S,
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

## Model Inference 🎯

### 1. Single Item Prediction

```python
# Get an item
item = dataset.items.get(item_id='item-id')

# Run prediction
prediction = model.predict(item_ids=[item.id])

# Wait for results
prediction.wait()
prediction_status = prediction.status
```

### 2. Batch Predictions

```python
# Create filters for items
filters = dl.Filters()
filters.add(field='dir', values='/folder/to/predict')

# Run batch prediction
filters = dl.Filters(field='dir', values='/folder/to/predict')
items = dataset.items.list(filters=filters)
batch_prediction = model.predict(
    item_ids=[item.id for item in items],
    dataset_id=dataset.id
)

batch_prediction.wait()
```

## Model Training 🎓

### 1. Basic Training

```python
# Prepare training configuration
model.configuration = {
    'epochs': 100,
    'batch_size': 32,
    'learning_rate': 0.001,
    'optimizer': 'adam'
}

# Start training
model.train()
```

### 2. Advanced Training Options

```python
# Train with data splitting and validation
train_filters = dl.Filters(field='dir', values='/train')
val_filters = dl.Filters(field='dir', values='/validation')

cloned_model = model.clone(
    model_name='cloned-model',
    dataset_id=dataset.id,
    train_filter=train_filters,
    validation_filter=val_filters,
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
