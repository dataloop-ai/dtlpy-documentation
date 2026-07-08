# Model Management: Your AI Model's Lifecycle 🤖

Learn how to manage your machine learning models in Dataloop - from development to deployment and monitoring.

## Project Setup ⚙️

### Dataloop Login 🔐

> ```python
> import dtlpy as dl
> import datetime
>
> # Interactive login — opens a browser window
> if dl.token_expired():
>     dl.login()
> ```

### Project and Dataset Setup

> ```python
> # Set your project and dataset names
> project_name = "onboarding-project"
> dataset_name = "onboarding-dataset"
>
> try:
>     # Try to get existing project
>     project = dl.projects.get(project_name=project_name)
>     print(f"Project '{project_name}' already exists")
> except dl.exceptions.NotFound:
>     project = dl.projects.create(project_name=project_name)
>     # Create project if it doesn't exist
>     print(f"Created project '{project_name}'")
>
> try:
>     # Try to get existing dataset
>     dataset = project.datasets.get(dataset_name=dataset_name)
>     print(f"Dataset '{dataset_name}' already exists")
>
> except dl.exceptions.NotFound:
>     # Create dataset if it doesn't exist
>     dataset = project.datasets.create(dataset_name=dataset_name)
>     print(f"Created dataset '{dataset_name}'")
> ```

> ```python
> dataset.open_in_web()
> ```

### Repopulating the Dataset

> ```python
> # Clear the dataset and repopulate it with new items without metadata attribution
> # You can skip or comment out this cell if it's not needed
>
> # Empty dataset - delete all dataset items
> for item in dataset.items.list().all():
>     item.delete()
>
> # Upload entire directory
> dataset.items.upload(
>     # Set the local folder path
>     local_path='/path/to/folder',
>     remote_path='/batch-upload',
> )
>
> dataset.items.list().print()
> ```

> ```python
> item = dataset.items.list().items[0]
> item.print()
> ```

## Getting Started with Models 🚀

### 1. Basic Model Setup

> ```python
> # Check if model is already installed on project
> model_name = "mobilenet"
> try:
>     model = project.models.get(model_name=model_name)
> except dl.exceptions.NotFound:
>     model_dpk = dl.dpks.get(dpk_name="mobilenet")
>     print(f"App '{model_dpk.name}' not found, installing...")
>     model_app = project.apps.install(dpk=model_dpk)
>     model = project.models.get(model_name=model_name)
> model.print()
> project.models.list().print()
> ```

### 2. Model Cloning

> ```python
> # Clone a model for fine-tuning
> model_cloned = model.clone(
>     model_name='my-model-v2',
>     project_id=project.id,
>     dataset=dataset,
>     labels=['car', 'truck', 'bus']  # Updated labels
> )
> ```

### 3. Model Configuration

> ```python
> # Set model.configuration
> model_cloned.configuration['input_size'] = 640
> model_cloned.configuration['batch_size'] = 32
> model_cloned.update()
>
> # See model configuration after update
> print(model_cloned.configuration)
> ```

### 4. Upload/Download Model Artifacts

> ```python
> # Upload
> model_cloned.artifacts.upload(
>     filepath='/path/to/weights.pth',
> )
>
> # Download
> model_cloned.artifacts.download(
>     local_path='/path/to/download/artifacts'
> )
>
> project.models.list().print()
> ```

## Model Deployment 🌟

### 1. Basic Deployment

> ```python
> # Deploy model with default configuration
> deployment = model.deploy()
>
> # Deploy with custom configuration
> deployment = model.deploy(
>     service_config={
>         'runtime': {
>             'numReplicas': 1,
>             'concurrency': 1,
>             'podType': dl.INSTANCE_CATALOG_REGULAR_S,
>             'runnerImage': 'gcr.io/viewo-g/piper/agent/runner/apps/torch-models:0.1.8'
>         }
>     }
> )
> ```

### 2. Advanced Deployment Options

> ```python
> # Deploy with auto-scaling
> deployment = model.deploy(
>     service_config={
>         'runtime': {
>             'podType': dl.INSTANCE_CATALOG_REGULAR_S,
>             'autoscaler': {
>                 'type': 'rabbitmq',
>                 'minReplicas': 0,
>                 'maxReplicas': 3,
>                 'queueLength': 10
>             }
>         },
>         'executionTimeout': 60 * 10,  # 10 minutes
>         'initTimeout': 60 * 5  # 5 minutes
>     }
> )
> # Print services after deployment
> project.services.list().print()
> ```

## Model Inference 🎯

### 1. Single Item Prediction

> ```python
> # Get an item
> item = dataset.items.list().items[0]
>
> # Run prediction
> model = project.models.get(model_name=model.name)
> prediction = model.predict(item_ids=[item.id])
>
> # Wait for results (service to start and complete prediction)
> prediction.wait()
> prediction_status = prediction.status
> ```

> ```python
> # Explore tagged item in Dataloop Dashboard
> dataset.open_in_web()
> ```

### 2. Batch Predictions

> ```python
> # Create filters for items
> filters = dl.Filters()
>
> # Set filter value
> filters.add(field='dir', values='/folder/to/predict')
>
> dataset.items.list(filters=filters).print()
> # Run batch prediction
> items = dataset.items.list(filters=filters)
> item_ids = [item.id for item in items.all()]
>
>
> batch_prediction = model.predict(
>     item_ids=item_ids,
>     dataset_id=dataset.id
> )
>
> batch_prediction_status = batch_prediction.wait()
> ```

> ```python
> # View prediction results from annotations
> print("=== Prediction Results ===")
>
> # Get the items with their annotations
> for item_id in item_ids:
>     item = dataset.items.get(item_id=item_id)
>     print(f"\nItem: {item.name} (ID: {item.id})")
>
>     # Get annotations for this item
>     annotations = list(item.annotations.list())
>     print(f"Number of annotations: {len(annotations)}")
>
>
>     for annotation in annotations:
>         print(f"Label: {annotation.label}, type:{annotation.type}")
> ```

## Model Training 🎓

### 1. Basic Training

> ```python
> # Training data preparation
> # The training service requires annotations without metadata.system.model.name to avoid training on model-generated predictions
> all_items = list(dataset.items.list().all())
>
> for item in all_items:
>     annotations = list(item.annotations.list())
>
>     for annotation in annotations:
>         # Remove model metadata if it exists
>         if annotation.metadata and 'system' in annotation.metadata:
>             if 'model' in annotation.metadata['system']:
>                 print(f"Removing model metadata from annotation on {item.name}")
>                 # Clear the model metadata
>                 annotation.metadata['system'].pop('model', None)
>                 annotation.update(True)
>
> # Dataset Labeling
> # Get unique labels from existing annotations
> labels = set()
> for item in dataset.items.list().all():
>     for annotation in item.annotations.list():
>         labels.add(annotation.label)
>
> print("Existing labels:", labels)
>
> # Add these labels to dataset recipe
> label_list = list(labels)
>
> dataset.add_labels(label_list=label_list)
> ```

> ```python
>
> # Clone the base model for training
> model_cloned = model.clone(
>     model_name='my-model-trained',
>     dataset=dataset,
>     project_id=project.id
> )
>
> model_cloned.labels = label_list
> # If None, set it and update
> model_cloned.dataset_id = dataset.id
> model_cloned.update()
>
> # Split dataset into ML subsets
> filters = dl.Filters(field='type', values='file')
>
> # Randomly split dataset items into train/validation/test subsets
> dataset.split_ml_subsets(
>     items_query=filters,
>     percentages={'train': 80, 'validation': 20, 'test': 0}
> )
>
> # Create filters based on ML subset tags
> train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
> validation_filters = dl.Filters(field="metadata.system.tags.validation", values=True)
>
> # Add subsets to the model
> model_cloned.add_subset(subset_name="train", subset_filter=train_filters)
> model_cloned.add_subset(subset_name="validation", subset_filter=validation_filters)
>
> print(model_cloned.configuration)
>
> model_cloned.configuration['batch_size'] = 16
> model_cloned.configuration['num_epochs'] = 3
> model_cloned.configuration['lr'] = 0.0001
>
> print(model_cloned.configuration)
>
> # Update with system metadata
> model_cloned.update(system_metadata=True)
>
> # Now train
> train_execution = model_cloned.train()
> print(f"Training started - Execution ID: {train_execution.id}")
>
> # Monitor training
> train_execution = train_execution.wait()
> print(f"Training status: {train_execution.latest_status['status']}")
> ```

### 2. Advanced Training Options

> ```python
> # Train with data splitting and validation
> train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
> validation_filters = dl.Filters(field="metadata.system.tags.validation", values=True)
>
> model_cloned_advanced = model.clone(
>     model_name='cloned-model',
>     dataset=dataset,
>     train_filter=train_filters,
>     validation_filter=validation_filters,
>     labels=label_list,
>     configuration={
>         'epochs': 5,
>         'batch_size': 32,
>         'learning_rate': 0.001,
>         'early_stopping': {
>             'patience': 5,
>             'min_delta': 0.001
>         },
>         'augmentation': {
>             'horizontal_flip': True,
>             'rotation_range': 20,
>             'zoom_range': 0.2
>         }
>     }
> )
> train_execution = model_cloned_advanced.train()
> train_status = train_execution.wait()
> print(f"Training status: {train_status.latest_status['status']}")
> ```

### 3. Training Monitoring

Log in to the Dataloop platform and check the training status and metrics.

Ready to explore Pipelines and Automation? Let's move on to the next chapter! 🚀
