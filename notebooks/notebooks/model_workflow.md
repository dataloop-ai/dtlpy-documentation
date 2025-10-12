# End-to-End Model Workflow Tutorial

This notebook provides a comprehensive, step-by-step guide for a complete model training workflow on the Dataloop platform. You'll learn how to set up datasets, create annotation tasks, train models, and deploy them for inference - all within a unified MLOps environment.

This tutorial demonstrates the full machine learning lifecycle from data preparation through model deployment, showcasing how Dataloop integrates data management, annotation workflows, and model training into a seamless experience.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **Project Access:** Ability to create projects and install apps from the Dataloop Marketplace.
* **Basic ML Knowledge:** Understanding of machine learning concepts and model training workflows.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Project & Dataset Preparation](#dataset-preparation)
3. [Labeling Task Creation & Annotation](#labeling-task)
4. [Model Training & Deployment](#model-training)
5. [Conclusion and Next Steps](#conclusion)

## <a id='dependencies-setup'></a>1. Dependencies & Setup

### Install Dependencies

First, let's ensure that the necessary Python libraries are installed. This notebook requires `dtlpy` for interacting with the Dataloop platform. The following cell will install or upgrade the library quietly.


```python
!pip install dtlpy --upgrade --quiet
```

### Import Required Libraries

Now, we import all the Python libraries that will be used throughout this tutorial.


```python
import dtlpy as dl
from tqdm import tqdm
import pathlib
import time

print(f"Dataloop SDK Version: {dl.__version__}")
```

### Set Up Dataloop Environment

To begin, we need to connect to the Dataloop platform. If you're not already logged in, running the cell below will prompt you to do so. Then, we'll either create a new project or get an existing one to work with.


```python
if dl.token_expired():
   dl.login() # Opens browser for login
   print(f"Logged in successfully to {dl.client_api.environment}")
else:
   print(f"Session active for {dl.client_api.info()['user_email']} in {dl.client_api.environment}")
```


```python
# Define a unique name for your project or use the one you already have
user_email = dl.info()['user_email']
user_prefix = user_email.split('@')[0].replace('.', '').replace('-', '') # Simple prefix from email
project_name = f'{user_prefix}-model-workflow'

# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=project_name)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=project_name)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")

print(f"\n> **Action Required:** Project name is set to '{project_name}'. Modify if needed.")
```

## <a id='dataset-preparation'></a>2. Project & Dataset Preparation

### Install Dataset from Marketplace

For model training (like ResNet), we need a dataset with multiple classes. Here we will install the "Agricultural Seedlings Dataset" from the Dataloop App Marketplace. This Dataloop App (DPK) not only provides the dataset but also pre-installs the ResNet model package, which we will use later.

The code below will install the app, retrieve the created dataset, and wait for the app's setup services to complete.


```python
# Install the ML Compare Solution DPK which includes the Agricultural Seedlings Dataset
dpk = dl.dpks.get(dpk_name="ml-compare-solution")
app = project.apps.install(dpk=dpk)
print(f"Seedlings Datasets installed: [Name: {app.name}, ID: {app.id}]")

# Get the annotated dataset that was created by the app
dataset = project.datasets.get(dataset_name="V2 Plant Seedlings - Annotated")
print(f"Got Annotated Dataset: [Name: {dataset.name}, ID: {dataset.id}]")

# Wait for app services to complete setup
filters = dl.Filters(resource=dl.FiltersResource.SERVICE, field="appId", values=app.id)
services = project.services.list(filters=filters)
if isinstance(services, dl.entities.PagedEntities):
    services = services.all()

service: dl.Service
print("Waiting for app services to finish, please wait...")
for service in services:
    service_executions = service.executions.list()
    if isinstance(service_executions, dl.entities.PagedEntities):
        service_executions = service_executions.all()
    for service_execution in tqdm(service_executions, desc=f"Service {service.name}"):
        service_execution.wait()
print("App services finished")
```

### Split Dataset for Training

For effective model training, it's crucial to split your dataset into training, validation, and test subsets. The Dataloop SDK provides a convenient method to do this by automatically tagging items. We will use an 80/10/10 split.


```python
SUBSET_PERCENTAGES = {'train': 80, 'validation': 10, 'test': 10}
dataset.split_ml_subsets(percentages=SUBSET_PERCENTAGES)
print(f"Dataset split completed with {SUBSET_PERCENTAGES}")
print(f"Total items in dataset: {dataset.items_count}")
```

## <a id='labeling-task'></a>3. Labeling Task Creation & Annotation

### Select Items and Create Task

In a real-world scenario, you might have a large dataset that needs annotation. Here, we'll simulate this by selecting a few items from each of our newly created subsets (train, validation, and test) and placing them into a labeling task.


```python
# Create filters for each subset
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
valid_filters = dl.Filters(field="metadata.system.tags.validation", values=True)
test_filters = dl.Filters(field="metadata.system.tags.test", values=True)

# Select a small number of items from each subset for the task
train_items = list(dataset.items.list(filters=train_filters).all())[:2]
valid_items = list(dataset.items.list(filters=valid_filters).all())[:2]
test_items = list(dataset.items.list(filters=test_filters).all())[:2]

print(f"Selected items for task:")
print(f"Train items: {[item.filename for item in train_items]}")
print(f"Valid items: {[item.filename for item in valid_items]}")
print(f"Test items: {[item.filename for item in test_items]}")
```

### Create Annotation Task

Now we will create a new annotation task for these selected items. We will assign the task to ourselves for this tutorial. The task uses the dataset's `recipe`, which defines the set of possible labels (the ontology) for annotation.


```python
# Get current user information
your_user_email = dl.info()["user_email"]

# Define task parameters
task_name = "Model Training Task"
assignee_ids = [your_user_email]
workload = dl.Workload.generate(assignee_ids=assignee_ids)
task_owner = your_user_email
recipe = dataset.recipes.list()[0]
items = train_items + valid_items + test_items

# Create the task
task: dl.Task = project.tasks.create(
    task_name=task_name, 
    assignee_ids=assignee_ids,
    workload=workload,
    dataset=dataset,
    task_owner=task_owner,
    recipe_id=recipe.id,
    items=items
)
print(f"Created Task: [Name: {task.name}, ID: {task.id}, Items Count: {task.total_items}]")
```

### Get Task Assignment

When a task is created, the system generates `assignments` for each assignee. Let's retrieve the assignment created for our user.


```python
assignment: dl.Assignment = task.assignments.list()[0]
print(f"Task assignment: [Name: {assignment.name}, ID: {assignment.id}]")
```

### Annotate and Complete the Task Items

The next stage involves creating annotations for the dataset items and marking them as completed. For this tutorial, we'll programmatically add classification annotations. The label for each annotation will be derived from the item's parent folder name.

We'll use the script below to add annotations that are properly linked to both the task and assignment. Once annotated, we'll update the status of each item to `completed` to indicate it is ready for the training phase.


```python
# We will use the following labels for our annotations
available_labels = list(dataset.labels_flat_dict.keys())
print(f"Available labels in dataset: {available_labels}")
```

### Programmatically Annotate Items

Now we will iterate through all items in the task, add annotations, and mark them as complete.


```python
# Get all items in the task
items = task.get_items()
if isinstance(items, dl.entities.PagedEntities):
    items = items.all()
items = list(items)

print(f"Processing {len(items)} items in the task...")

item: dl.Item
for item in tqdm(items, desc="Annotating items"):
    # Delete existing annotations on the item
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)  # Filter is required to delete all annotations
    item.annotations.delete(filters=filters)

    # Creating new classification annotation based on the item folder name
    builder = item.annotations.builder()
    label = pathlib.Path(item.filename).parent.name
    classification = dl.Classification(label=label, description=f"Created by assignment {assignment.id}")

    # Linking the annotations to the task
    metadata = {
        "system": {
            "recipeId": recipe.id,
            "taskId": task.id,
            "assignmentId": assignment.id
        }
    }

    # Adding the annotations to the item
    builder.add(
        annotation_definition=classification,
        metadata=metadata
    )
    item.annotations.upload(builder)
    
    # Mark item as completed
    item.update_status(
        status="completed", 
        assignment_id=assignment.id, 
        task_id=task.id
    )
    print(f"Processed Item: [ID: {item.id}, Filename: {item.filename}, Label: {label}]")

print(f"\nCompleted annotation of {len(items)} items")
```

## <a id='model-training'></a>4. Model Training & Deployment

### Configure Base Model

With our data annotated, we can now begin the training process. We will retrieve the pre-trained ResNet model that was installed with the dataset DPK. We then configure it by specifying which data subsets to use for training and validation, and by setting key hyperparameters like the number of epochs and batch size.


```python
# Get the pre-trained ResNet model
base_model = project.models.get(model_name="pretrained-resnet")
print(f"Retrieved base model: {base_model.name} (ID: {base_model.id})")

# Configure model metadata and subsets
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
val_filters = dl.Filters(field="metadata.system.tags.validation", values=True)

base_model.add_subset("train", train_filters)
base_model.add_subset("validation", val_filters)

# Set model configuration for ResNet training
base_model.configuration = {
    "num_epochs": 5,
    "batch_size": 32,
}

print(f"Base model configured: {base_model.name}")
print(f"Training configuration: {base_model.configuration}")
```

### Clone and Train Model

To fine-tune a model, we first `clone` the pre-trained model. This creates a new, trainable model entity in your project. We associate our dataset and its labels with this new model and then start the training process.

> **NOTE**: The training process can take a significant amount of time, depending on your dataset size, model configuration, and the available compute resources (GPU type).


```python
# Clone the base model for fine-tuning
finetuned_model_name = base_model.name + "-finetuned"
labels = [label.tag for label in dataset.labels]
finetuned_model = base_model.clone(model_name=finetuned_model_name, dataset=dataset, labels=labels)
print(f"Created new model for finetuning: [Name: {finetuned_model.name}, ID: {finetuned_model.id}]")
print(f"Model will be trained on labels: {labels}")
```

### Start Model Training

Now we'll initiate the training process and get the execution details.


```python
print(f"Starting training for model: {finetuned_model.name}")
execution = finetuned_model.train()
print(f"Training execution started: [ID: {execution.id}, Status: {execution.status}]")
print(f"You can monitor training progress in the Dataloop platform at: {finetuned_model.platform_url}")
```

### Wait for Training Completion

The cell below will periodically check the status of the training execution and wait for it to complete. You can also monitor the training progress, view logs, and see performance metrics directly in the Dataloop platform by navigating to your model's page.


```python
# Wait for training to complete
print("Waiting for training to complete...")
start_time = time.time()

while execution.in_progress():
    elapsed_time = time.time() - start_time
    print(f"Training in progress... (Elapsed: {elapsed_time/60:.1f} minutes) - checking again in 2 minutes")
    time.sleep(120)  # Sleep for 2 minutes
    execution = dl.executions.get(execution_id=execution.id)

# Check final status
final_status = execution.get_latest_status()['status']
total_time = time.time() - start_time

if final_status == "success":
    print(f"Training completed successfully! (Total time: {total_time/60:.1f} minutes)")
    print(f"Model ID: {finetuned_model.id}")
elif final_status == "failed":
    print(f"Training failed. Execution ID: {execution.id}. Check logs in Dataloop platform for details.")
else:
    print(f"Training ended with status: {final_status}. Execution ID: {execution.id}.")
```

### Deploy the Trained Model

Once training is complete, the final step is to deploy the fine-tuned model. Deployment creates a live service endpoint that can be used for inference on new, unseen data.


```python
# Check if training was successful before deploying
if final_status == "success":
    # Get the updated model entity
    finetuned_model = project.models.get(model_id=finetuned_model.id)
    
    print(f"Deploying model: {finetuned_model.name}")
    # Deploy the model
    service = finetuned_model.deploy()
    print(f"Model deployed successfully: [Name: {service.name}, ID: {service.id}]")
    print(f"Service status: {service.status}")
    
    # Wait for deployment to complete
    print("Waiting for deployment to complete...")
    while finetuned_model.status not in [dl.ModelStatus.DEPLOYED, dl.ModelStatus.FAILED]:
        print(f"Model status: {finetuned_model.status} - waiting...")
        time.sleep(30)
        finetuned_model = project.models.get(model_id=finetuned_model.id)
    
    print(f"Final model status: {finetuned_model.status}")
    if finetuned_model.status == dl.ModelStatus.DEPLOYED:
        print(f"🎉 Model successfully deployed and ready for inference!")
        print(f"Model URL: {finetuned_model.platform_url}")
else:
    print("Skipping deployment due to training failure.")
```

## <a id='conclusion'></a>5. Conclusion and Next Steps

Congratulations! You have successfully walked through the entire process of an end-to-end model workflow on Dataloop.

### Summary of What You've Accomplished:
- **Environment Setup:** Connected to Dataloop and configured your project for machine learning workflows
- **Dataset Preparation:** Installed a dataset from the Marketplace and prepared it for training by creating ML subsets (train/validation/test)
- **Annotation Workflow:** Created a labeling task for a subset of data and programmatically annotated items with proper task linkage
- **Model Configuration:** Retrieved and configured a pre-trained ResNet model with appropriate training parameters
- **Model Training:** Cloned the base model, fine-tuned it on your annotated data, and monitored the training process
- **Model Deployment:** Successfully deployed the trained model as a live service for inference
- **MLOps Integration:** Experienced the complete machine learning lifecycle within a unified platform

### Next Steps:
From here, you can explore more advanced concepts:
- **Model Inference:** Use your deployed model to make predictions on new items and evaluate its performance
- **Pipeline Automation:** Create a full pipeline that automates this entire workflow for continuous model improvement
- **Active Learning:** Explore active learning loops to intelligently select which items to annotate next based on model uncertainty
- **Model Monitoring:** Set up monitoring and alerting for your deployed models to track performance over time
- **A/B Testing:** Deploy multiple model versions and compare their performance on real data
- **Advanced Workflows:** Integrate multiple models, create ensemble methods, or build complex multi-stage pipelines
- **Custom Models:** Bring your own model architectures using Dataloop's model adapter framework

### Additional Resources:
- **[Active Learning Pipeline Tutorial](https://docs.dataloop.ai/docs/active-learning-pipeline):** Learn how to create intelligent annotation workflows
- **[Model Management Documentation](https://developers.dataloop.ai/tutorials/model_management):** Explore advanced model management features
- **[Pipeline Builder](https://developers.dataloop.ai/tutorials/pipelines):** Create automated ML workflows
- **[Custom Model Adapters](https://developers.dataloop.ai/tutorials/model_management):** Integrate your own models into Dataloop

This tutorial demonstrates the power of having an integrated MLOps platform where data management, annotation, training, and deployment work seamlessly together. You're now ready to build production-ready machine learning workflows on Dataloop!
