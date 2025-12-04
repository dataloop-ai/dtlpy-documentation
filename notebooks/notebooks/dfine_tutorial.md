# D-FINE Object Detection Model with Dataloop Platform Tutorial

This notebook provides a comprehensive guide on using the D-FINE (Diverse Fine-grained Distribution Refinement) object detection model with the Dataloop platform. D-FINE is a real-time object detection model designed for diverse applications such as autonomous driving, surveillance systems, robotics, and retail analytics.

The D-FINE model uses two key components: Fine-grained Distribution Refinement (FDR) for enhanced localization accuracy, and Global Optimal Localization Self-Distillation (GO-LSD) for improved training efficiency. You'll learn how to fine-tune this powerful model on your custom datasets and deploy it for real-time inference.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Python 3.7+ with pip for installing required packages.
* **Basic Knowledge:** Familiarity with object detection concepts and machine learning workflows is helpful.

### Navigate through the following sections:
1. **[Install Dependencies](#install-dependencies)** - Setting up required Python libraries
2. **[Import Required Libraries](#import-libraries)** - Loading necessary modules
3. **[Set Up Dataloop Environment](#setup-environment)** - Connecting to the platform
4. **[Install D-FINE Model Package](#install-dfine-dpk)** - Loading the model from marketplace
5. **[Load Base D-FINE Model](#configure-dfine-model)** - Configuring the base model
6. **[Prepare Dataset](#prepare-dataset)** - Setting up training data
7. **[Configure Model for Training](#configure-model-training)** - Setting training parameters
8. **[Clone Model and Start Training](#clone-train-model)** - Fine-tuning the model
9. **[Deploy Model as Service](#deploy-service)** - Setting up inference endpoint
10. **[Test Deployed Model](#test-deployed)** - Running predictions
11. **[Extract Embeddings](#extract-embeddings)** - Generating feature vectors
12. **[Conclusion](#conclusion)** - Summary and next steps

<a id="install-dependencies"></a>
## 1. Install Dependencies

First, ensure that the necessary Python libraries are installed. This notebook requires `dtlpy` for interacting with the Dataloop platform and standard Python libraries for data processing and visualization.

**Note:** The D-FINE model dependencies (transformers, torch, etc.) will be managed by the Dataloop model adapter.


```python
!pip install dtlpy --upgrade --quiet
```

<a id="import-libraries"></a>
## 2. Import Required Libraries

Now, we import all the Python libraries that will be used throughout this tutorial.


```python
import dtlpy as dl
import time
```

<a id="setup-environment"></a>
## 3. Set Up Dataloop Environment

Connect to the Dataloop platform and create or get an existing project to work with.


```python
dl.setenv("prod")
if dl.token_expired():
    dl.login()

PROJECT_NAME = "My Dfine Finetune Project"
project = dl.projects.create(project_name=PROJECT_NAME)
print(f"Working with project: {project.name} (ID: {project.id})")
```

**Action Required:** In the cell above, replace `"My Dfine Finetune Project"` with the desired name for your Dataloop project. If a project with this name already exists, the SDK will retrieve it; otherwise, a new project will be created.

<a id="install-dfine-dpk"></a>
## 4. Install D-FINE Model Package

Install the D-FINE model package from the Dataloop marketplace. This will provide the model adapter and all necessary dependencies.

**Note:** If a D-FINE DPK is not yet available in the marketplace, we'll create a model entity directly and use the model adapter pattern. This section shows both approaches.


```python
print("Loading D-FINE app from marketplace...")
dfine_dpk = dl.dpks.get(dpk_name="dfine-xlarge-obj2coco-huggingface-app")
dfine_app = project.apps.install(dpk=dfine_dpk)
print(f"D-FINE App installed: {dfine_app.name} (ID: {dfine_app.id})")
```

<a id="configure-dfine-model"></a>
## 5. Load Base D-FINE Model

Load the D-FINE model entity from the installed app. This model will serve as the base for fine-tuning.


```python
base_model = project.models.get(model_name='dfine-xlarge-obj2coco-huggingface-model')
```

<a id="prepare-dataset"></a>
## 6. Prepare Dataset

Now prepare a dataset with images for object detection. We'll install one from the marketplace and split the dataset for ML subsets.


```python
# Install dataset from marketplace
dataset_dpk = dl.dpks.get(dpk_name="military-assets-dataset")
dataset_app = project.apps.install(dpk=dataset_dpk)
print(f"Dataset app installed: {dataset_app.name}")

# Wait for dataset to fully load
dataset = project.datasets.get(dataset_name="Military Assets Dataset")
while dataset.items.list().items_count < 200:
    print(f"Loading dataset... ({dataset.items.list().items_count}/200 items)")
    time.sleep(60)
    dataset = project.datasets.get(dataset_name="Military Assets Dataset")

print(f"Dataset ready with {dataset.items.list().items_count} items")

# Split into train/validation/test subsets
dataset.split_ml_subsets(percentages={'train': 80, 'validation': 10, 'test': 10})
```

<a id="configure-model-training"></a>
## 7. Configure Model for Training

Configure the model metadata with dataset subsets and training parameters. The subset filters tell the model which items to use for training and validation.


```python
# Configure model metadata and subsets
base_model.metadata["system"] = {}
base_model.metadata["system"]["subsets"] = {}

train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
val_filters = dl.Filters(field="metadata.system.tags.validation", values=True)

base_model.metadata["system"]["subsets"]["train"] = train_filters.prepare()
base_model.metadata["system"]["subsets"]["validation"] = val_filters.prepare()

# Set model configuration (optional)
base_model.configuration = {
  "image_size": 640,
  "confidence_threshold": 0.25,
  "image_processor_path": "ustc-community/dfine-xlarge-obj2coco",
  "pooling_method": "max",
  "augmentation_config": {
    "rotate_limit": 15,
    "rotate_p": 0.5,
    "perspective_p": 0.1,
    "horizontal_flip_p": 0.5,
    "brightness_contrast_p": 0.5,
    "hue_saturation_p": 0.1
  },
  "train_configs": {
    "per_device_train_batch_size": 8,
    "per_device_eval_batch_size": 8,
    "gradient_accumulation_steps": 1,
    "learning_rate": 0.00005,
    "weight_decay": 0,
    "num_train_epochs": 3,
    "warmup_steps": 300,
    "max_grad_norm": 0.1,
    "logging_steps": 50,
    "save_strategy": "epoch",
    "eval_strategy": "epoch",
    "fp16": False,
    "metric_for_best_model": "eval_loss",
    "greater_is_better": False
  }
}
```

<a id="clone-train-model"></a>
## 8. Clone Model and Start Training

Clone the base model to create a new model entity linked to your dataset, then start the training process. The cloned model will inherit the configuration from the base model.


```python
# Clone base model and start training
finetuned_model = base_model.clone(
    model_name=base_model.name + "-finetuned",
    dataset=dataset
)
print(f"Created model: {finetuned_model.name} (ID: {finetuned_model.id})")

# Train and wait for completion
execution = finetuned_model.train()
print(f"Training started (execution: {execution.id})")

execution.wait()
finetuned_model = project.models.get(model_id=finetuned_model.id)
print(f"Training complete. Model status: {finetuned_model.status}")
```

<a id="deploy-service"></a>
## 9. Deploy Model as Service

Deploy the trained model as a service on the Dataloop platform to enable real-time inference. This allows you to run predictions on-demand through API calls.


```python
# Deploy the trained model as a service
service = finetuned_model.deploy()
print(f"Deployment started (service: {service.id})")

# Wait for deployment to complete
while finetuned_model.status != dl.ModelStatus.DEPLOYED:
    time.sleep(30)
    finetuned_model = project.models.get(model_id=finetuned_model.id)

print(f"Model deployed. Service: {service.name}")
```

<a id="test-deployed"></a>
## 10. Test Deployed Model

Test the deployed model service by running predictions on images. Since the model is now deployed, predictions will run through the service.


```python
# Run predictions on test items
test_filters = dl.Filters(field="metadata.system.tags.test", values=True)
test_items = list(dataset.items.list(filters=test_filters).all())[:3]

execution = finetuned_model.predict(item_ids=[item.id for item in test_items])
print(f"Running predictions on {len(test_items)} items...", end="", flush=True)

# Wait for execution with progress updates using Dataloop's in_progress() method
while execution.in_progress():
    status = execution.get_latest_status()['status']
    print(f" {status}...", end="", flush=True)
    time.sleep(5)
    execution = dl.executions.get(execution_id=execution.id)

print(" done")

# Show results
test_item = dataset.items.get(item_id=test_items[0].id)
annotations = test_item.annotations.list()
print(f"Item: {test_item.name} - {len(annotations)} detections")
for ann in annotations[:5]:
    if ann.type == dl.AnnotationType.BOX:
        print(f"  - {ann.label}")
```

<a id="extract-embeddings"></a>
## 11. Extract Embeddings (Optional)

The D-FINE model can extract feature embeddings from images, which can be used for similarity search and retrieval tasks. This section shows how to extract embeddings from the deployed model.


```python
# FOR DEBUGGING - Reconnect to existing resources if needed
FINETUNED_MODEL_NAME="dfine-xlarge-obj2coco-huggingface-model-finetuned-7e89f"
import dtlpy as dl
import time
if dl.token_expired():
    dl.login()
dl.setenv("prod")
project = dl.projects.get("My Dfine Finetune Project")
base_model = project.models.get(model_name='dfine-xlarge-obj2coco-huggingface-model')
try:
    finetuned_model = project.models.get(model_name=FINETUNED_MODEL_NAME)
except Exception:
    print("No finetuned model created yet, create first")
dataset = project.datasets.get(dataset_name="Military Assets Dataset")
```


```python
# The model.embed() method extracts feature vectors from items and stores them
# in a feature set associated with the model. 

# Get test items to extract embeddings from
test_filters = dl.Filters(field="metadata.system.tags.test", values=True)
test_items = list(dataset.items.list(filters=test_filters).all())[:5]  # Get 5 test items

print(f"Extracting embeddings for {len(test_items)} items...")

# Extract embeddings using the model's embed method
# This creates an execution that processes items and stores embeddings in a feature set
item_ids = [item.id for item in test_items]
execution = finetuned_model.embed(item_ids=item_ids)

# Wait for the embedding extraction to complete
execution.wait()
print(f"Embedding extraction completed. Execution status: {execution.status[-1]['status']}")

# Access the feature set associated with this model
# Each model has one feature set that stores all generated embeddings
feature_set = finetuned_model.feature_set
print(f"\nFeature Set Details:")
print(f"  Name: {feature_set.name}")
print(f"  Size (dimensions): {feature_set.size}")
print(f"  Entity type: {feature_set.entity_type}")

# List features in the feature set
features_page = feature_set.features.list()
print(f"  Total features: {features_page.items_count}")

# Show sample feature vectors
for feature in list(features_page.all())[:3]:
    print(f"\n  Feature ID: {feature.id}")
    print(f"  Entity ID: {feature.entity_id}")
    print(f"  Vector (first 5 values): {feature.value[:5]}...")
```

<a id="conclusion"></a>
## 12. Conclusion

Congratulations! You have successfully fine-tuned the D-FINE object detection model with a custom dataset on the Dataloop platform.

### What We Accomplished

1. **Installed the D-FINE model package** from the Dataloop marketplace
2. **Configured the model** with custom training parameters
3. **Prepared and split a dataset** for training, validation, and testing
4. **Trained the model** on your custom dataset
5. **Deployed the model as a service** for real-time inference
6. **Tested the deployed model** with predictions
7. **Extracted embeddings** for similarity search applications

### Next Steps

- **Monitor Model Performance:** Check the model metrics and training logs in the Dataloop UI
- **Improve Model Accuracy:** Experiment with different hyperparameters, data augmentation settings, or training epochs
- **Scale Deployment:** Adjust service configuration (replicas, pod types) based on your inference workload
- **Production Integration:** Use the deployed service API to integrate object detection into your applications

### Additional Resources

- [Dataloop Developer Documentation](https://developers.dataloop.ai/)
- [Dataloop Model Management Guide](https://developers.dataloop.ai/tutorials/model_management/)
- [Dataloop Service Deployment Guide](https://developers.dataloop.ai/tutorials/model_management/deploy/)
