# CLIP (Contrastive Language-Image Pre-Training) Model Adapter Tutorial

This notebook provides a comprehensive guide on fine-tuning a CLIP model using the Dataloop platform and its Python SDK. CLIP models are powerful for tasks involving understanding the relationship between images and text, such as zero-shot image classification, image-text retrieval, and generating image embeddings for semantic search.

Fine-tuning allows you to adapt a pre-trained CLIP model to your specific dataset and domain, potentially improving its performance on tasks relevant to your data. This tutorial demonstrates the complete workflow from data preparation through model deployment.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **Project Access:** Ability to create projects and install apps from the Dataloop Marketplace.
* **Basic ML Knowledge:** Understanding of machine learning concepts and multimodal models.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Environment Setup](#environment-setup)
3. [Prepare Dataset for Fine-Tuning](#prepare-dataset)
4. [Fine-Tune and Deploy CLIP Model](#finetune-deploy-clip)
5. [Conclusion and Next Steps](#conclusion)

Let's get started!

## <a id='dependencies-setup'></a>1. Dependencies & Setup

First, ensure that the necessary Python libraries are installed. This notebook requires `dtlpy` for interacting with the Dataloop platform and `pandas` for data manipulation. The following cell will install or upgrade them.


```python
!pip install dtlpy pandas --upgrade --quiet
```

## <a id='environment-setup'></a>2. Environment Setup

### Import Required Libraries

Now, we import all the Python libraries that will be used throughout this tutorial.


```python
import time
import random
import string
import dtlpy as dl
import pandas as pd

from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

print(f"Dataloop SDK Version: {dl.__version__}")
```

### Set Up Dataloop Environment

We need to set up our Dataloop environment and get our project. You'll need to replace project and dataset names with your own values.

> **_NOTE:_** This tutorial assumes you are working in a new project which does NOT have the CLIP model previously installed. If it's an existing project and you already have CLIP installed, you will need to get the appropriate app and base CLIP model entity for the rest of the code to work correctly.


```python
if dl.token_expired():
    dl.login()

# Define a unique name for your project or change it to your own project name
user_email = dl.info()['user_email']
user_prefix = user_email.split('@')[0].replace('.', '').replace('-', '') # Simple prefix from email
project_name = f'{user_prefix}-clip-tutorial'

# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=project_name)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=project_name)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")
```

**Action Required:** In the cell above, you can modify `"{user_prefix}-clip-tutorial"` with the desired name for your Dataloop project. If a project with this name already exists, the SDK will retrieve it; otherwise, a new project will be created.

## <a id='prepare-dataset'></a>3. Prepare Dataset for Fine-Tuning

Fine-tuning a CLIP model requires a dataset of images paired with relevant textual descriptions. This section covers two ways to prepare such a dataset:
1. **Option A:** Use a publicly available dataset from the Dataloop Marketplace (Mars Surface Images with Captions).
2. **Option B:** Upload your own custom dataset of images and descriptions.

### 3.1 Option A: Use Public Dataset (Mars Surface Images)

For this tutorial we will install the Mars Surface Images Datasets from the Dataloop Marketplace. This dataset includes images with descriptions pre-loaded in the item metadata.

#### 3.1.1 Install Mars Surface Images DPK

This Dataloop Package (DPK) contains datasets related to Mars surface imagery, including one with captions.


```python
dpk = dl.dpks.get(dpk_name="mars-surface-images")
try:
    app = project.apps.install(
        app_name=dpk.display_name, 
        dpk=dpk, 
        custom_installation=dpk.to_json()
    )
    print(f"Installed {dpk.display_name} app: {app.name}")
except dl.exceptions.BadRequest as e:
    print(f"{dpk.display_name} app already installed, getting existing app")
    app = project.apps.get(app_name=dpk.display_name)
```

⚠️ You may need to wait a few minutes after installing the app until the dataset has completed loading into your project.


```python
# Wait for the dataset to load
print("Waiting for dataset to load...")
time.sleep(150)
print("Dataset should now be available")
```

#### 3.1.2 Get Captioned Dataset and Split for ML

After installing the DPK, the "Mars Surface Images with Captions" dataset should be available in your project. We will retrieve this dataset and split its items into training, validation, and test subsets. The Dataloop SDK provides a convenient method to do this by automatically tagging items. This splitting is crucial for proper model training and evaluation.


```python
dataset = project.datasets.get(dataset_name="Mars Surface Images with Captions")
print(f"Retrieved dataset: {dataset.name} (ID: {dataset.id})")
print(f"Dataset contains {dataset.items_count} items")

SUBSET_PERCENTAGES = {'train': 80, 'validation': 10, 'test': 10}
dataset.split_ml_subsets(percentages=SUBSET_PERCENTAGES)
print(f"Dataset split completed with percentages: {SUBSET_PERCENTAGES}")
```

### 3.2 Option B: (Alternative) Upload and Prepare Your Custom Dataset

If you have your own dataset of images and corresponding text descriptions, you can use the function below to create a new Dataloop dataset and upload your images with descriptions.

The function expects a Pandas DataFrame (`pairs_df`) with two columns:
- `'filepath'`: The local path to each image file.
- `'description'`: The text description for that image.

It also assumes that for each image file (e.g., `items/image1.jpg`), there is a corresponding JSON annotation file (e.g., `json/image1.json`) if you have existing annotations to upload. If not, the `local_annotations_path` part can be adapted.


```python
def create_new_dataset(dataset_name, pairs_df, subset_percentages={'train': 80, 'validation': 10, 'test': 10}):
    """
    Creates a new dataset from a DataFrame containing image paths and descriptions

    Args:
        dataset_name (str): Name of the dataset to create
        pairs_df (pd.DataFrame): DataFrame containing 'filepath' and 'description' columns
        subset_percentages (dict): Dictionary containing the percentages for each subset
        default is 80% train, 10% validation, 10% test
        can be changed to any other percentages as long as the sum is 100
    
    Returns:
        dl.Dataset: The created dataset
    """

    try:
        dataset = project.datasets.create(dataset_name=dataset_name)
    except dl.exceptions.BadRequest:
        # Generate 5 random alphanumeric characters
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        dataset = project.datasets.create(dataset_name=f"{dataset_name}_{suffix}")

    def upload_item(row):
        file_path = row["filepath"]
        annots_path = file_path.replace("items", "json") # This assumes a specific structure for annotation files
        
        # Upload item with annotations
        item = dataset.items.upload(
            local_path=file_path,
            local_annotations_path=annots_path,
            item_metadata=dl.ExportMetadata.FROM_JSON,
            overwrite=True,
        )

        # Set description and update
        item.set_description(text=row["description"])
        item.update()

    # Use ThreadPoolExecutor to upload items in parallel with progress bar
    with ThreadPoolExecutor() as executor:
        from tqdm import tqdm
        list(tqdm(
            executor.map(upload_item, [row for _, row in pairs_df.iterrows()]),
            total=len(pairs_df),
            desc="Uploading items",
            unit="item",
            bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]'
        ))

    # Since model training requires labels, we create a dummy label for the recipe
    dataset.add_labels(label_list=['free-text'])
    
    # Split the dataset into ML subsets
    dataset.split_ml_subsets(percentages=subset_percentages)

    return dataset

# Example usage (commented out):
# pairs_df = pd.DataFrame({
#     'filepath': ['path/to/image1.jpg', 'path/to/image2.jpg'],
#     'description': ['Description for image 1', 'Description for image 2']
# })
# custom_dataset = create_new_dataset('my-custom-clip-dataset', pairs_df)

print("Custom dataset creation function defined. Use it if you have your own image-text pairs.")
```

## <a id='finetune-deploy-clip'></a>4. Fine-Tune and Deploy CLIP Model

With the dataset prepared, we can now proceed to fine-tune the CLIP model.

### 4.1 Install CLIP Model Package (DPK)

First, we install the CLIP model DPK from the Dataloop Marketplace. This package provides the necessary components for CLIP model training and inference.


```python
clip_model_dpk = dl.dpks.get(dpk_name="clip-model-pretrained")
try:
    model_app = project.apps.install(
        app_name=clip_model_dpk.display_name, 
        dpk=clip_model_dpk, 
        custom_installation=clip_model_dpk.to_json()
    )
    print(f"Installed {clip_model_dpk.display_name} app: {model_app.name}, ID: {model_app.id}")
except dl.exceptions.BadRequest as e:
    print(f"{clip_model_dpk.display_name} app already installed, getting existing app")
    model_app = project.apps.get(app_name=clip_model_dpk.display_name)
    print(f"Retrieved existing app: {model_app.name}, ID: {model_app.id}")
```

### 4.2 Configure and Clone Pretrained CLIP Model

Next, we retrieve the base pre-trained CLIP model entity ("openai-clip") provided by the DPK. We'll then configure its metadata, specifying which subsets of our `dataset` to use for training and validation.

You can also adjust model hyperparameters like learning rate, batch size, and number of epochs in the `base_model.configuration` dictionary. The example settings below are a starting point.


```python
base_model = project.models.get(model_name="openai-clip")
print(f"Retrieved base CLIP model: {base_model.name} (ID: {base_model.id})")

# Configure model metadata and subsets
# Use the correct field names for ML subset tags
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
val_filters = dl.Filters(field="metadata.system.tags.validation", values=True)

# Add subsets to the model using the correct method
base_model.add_subset(subset_name="train", subset_filter=train_filters)
base_model.add_subset(subset_name="validation", subset_filter=val_filters)

# Set model configuration (hyperparameters)
base_model.configuration = {
    "model_name": "ViT-B/32",      # CLIP model architecture (e.g., ViT-B/32, RN50)
    "embeddings_size": 512,       # Output embedding dimension for ViT-B/32
    "num_epochs": 10,             # Number of training epochs (adjust based on dataset size and convergence)
    "batch_size": 64,             # Batch size for training (adjust based on GPU memory)
    "learning_rate": 5e-6,        # Learning rate (often smaller for fine-tuning)
    "early_stopping": True,       # Enable early stopping
    "early_stopping_epochs": 3,   # Number of epochs with no improvement before stopping
    "weight_decay": 0.01          # Weight decay for regularization (optional)
}
base_model.output_type = "text" # For CLIP, this usually indicates it's working with text-image pairs

# Update the model to save the subset configurations
base_model.update(system_metadata=True)

print(f"Base model configured with:")
print(f"  Architecture: {base_model.configuration['model_name']}")
print(f"  Epochs: {base_model.configuration['num_epochs']}")
print(f"  Batch size: {base_model.configuration['batch_size']}")
print(f"  Learning rate: {base_model.configuration['learning_rate']}")
```

### 4.3 Train the Model

Now we clone the configured base model. This creates a new model entity in your project that will be fine-tuned. We associate our `dataset` with this new model and then start the training process.

> **NOTE**: The training process can take a significant amount of time, depending on your dataset size, model configuration, and the available compute resources (GPU type).


```python
# Ensure 'dataset' is defined from the dataset preparation step
if 'dataset' not in locals() or dataset is None:
    raise ValueError("Error: 'dataset' is not defined. Please run the dataset preparation section first.")

# Create a unique name for the fine-tuned model
finetuned_model_name = base_model.name + "-finetuned-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
print(f"Cloning model to create: '{finetuned_model_name}' using dataset '{dataset.name}'")

# Clone the base model
finetuned_model = base_model.clone(model_name=finetuned_model_name, dataset=dataset)
print(f"Model cloned successfully: '{finetuned_model.name}' (ID: {finetuned_model.id})")

# Start training
print(f"Starting training for model: '{finetuned_model.name}'. This may take a while...")
execution = finetuned_model.train()
print(f"Training initiated. Execution ID: {execution.id}")
print(f"You can monitor progress in the Dataloop platform at: {finetuned_model.platform_url}")
```

### 4.4 Monitor Training Progress

The cell below will periodically check the status of the training execution. You can also monitor the training progress, view logs, and see performance metrics directly in the Dataloop platform by navigating to your project, then Models, finding your `finetuned_model`, and checking its 'Executions' or 'Training' tabs.


```python
# Wait for training to complete
print(f"Waiting for training execution {execution.id} to complete...")
start_time = time.time()

execution_status = dl.executions.get(execution_id=execution.id).get_latest_status().get('status')

while execution_status not in [dl.ExecutionStatus.SUCCESS, dl.ExecutionStatus.FAILED, dl.ExecutionStatus.CANCELED]:
    elapsed_time = time.time() - start_time
    print(f"Training in progress (Status: {execution_status}, Elapsed: {elapsed_time/60:.1f} min)... checking again in 5 minutes")
    time.sleep(300)  # Sleep for 5 minutes
    execution_status = dl.executions.get(execution_id=execution.id).get_latest_status().get('status') # Refresh execution status

# Check final status
total_time = time.time() - start_time
if execution_status == dl.ExecutionStatus.SUCCESS:
    print(f"🎉 Training completed successfully! (Total time: {total_time/60:.1f} minutes)")
    print(f"Model ID: {finetuned_model.id}")
    # Update the local model object with the latest status and artifacts from the platform
    finetuned_model = project.models.get(model_id=finetuned_model.id)
elif execution_status == dl.ExecutionStatus.FAILED:
    print(f"❌ Training failed. Execution ID: {execution.id}. Check logs in Dataloop platform for details.")
else:
    print(f"Training ended with status: {execution_status}. Execution ID: {execution.id}.")
```

### 4.5 Deploy the Fine-Tuned Model

Once the model has successfully trained, you can deploy it as a service. This makes the model available for inference tasks, such as generating embeddings for new images.


```python
if 'finetuned_model' in locals() and finetuned_model is not None and execution_status == dl.ExecutionStatus.SUCCESS:
    print(f"Deploying fine-tuned model: '{finetuned_model.name}' (ID: {finetuned_model.id})")
    
    # The service will be created with default settings (e.g., 1 replica, default GPU if needed by model)
    # You can customize deployment configuration if necessary via finetuned_model.deploy(service_config={...})
    service = finetuned_model.deploy()
    print(f"Deployment initiated. Service ID: {service.id}")
    
    # Get the latest version of the model entity, which now includes deployment details
    finetuned_model = project.models.get(model_id=finetuned_model.id)
    
    # Wait for deployment to complete
    print("Waiting for deployment to complete...")
    while finetuned_model.status not in [dl.ModelStatus.DEPLOYED, dl.ModelStatus.FAILED]:
        print(f"Model '{finetuned_model.name}' is deploying (Status: {finetuned_model.status}). Waiting for service to be ready...")
        time.sleep(180)  # Wait 3 minutes between checks
        finetuned_model = project.models.get(model_id=finetuned_model.id)
    
    if finetuned_model.status == dl.ModelStatus.DEPLOYED:
        print(f"🎉 Model successfully deployed!")
        print(f"Model URL: {finetuned_model.platform_url}")
    else:
        print(f"❌ Deployment failed. Model status: {finetuned_model.status}")
else:
    print("Skipping deployment: Model training was not successful or 'finetuned_model' is not defined.")
```

### 4.6 Embed Datasets using the Fine-Tuned Model

After the fine-tuned model is deployed and its service is ready, you can use it to generate embeddings for images in any dataset. These embeddings capture the semantic content of the images as understood by your fine-tuned model and can be used for tasks like semantic search or similarity comparison.

We will typically want to embed the original image dataset (e.g., "Mars Surface Images with Captions" or your custom image dataset), though you can also embed other datasets with your finetuned model.


```python
if 'finetuned_model' in locals() and finetuned_model.status == dl.ModelStatus.DEPLOYED:
    # IMPORTANT: Select the dataset you want to embed. This should be your ORIGINAL image dataset,
    # not the prompt_dataset used for training.

    # You can embed the original image dataset or another dataset with the fine-tuned model.
    # For example, if you used the Mars dataset and want to embed the uncaptioned dataset (that the model was *not* trained on):
    try:
        dataset_to_embed = project.datasets.get(dataset_name="Mars Surface Images Unannotated")
        print(f"Found unannotated dataset: {dataset_to_embed.name}")
    except dl.exceptions.NotFound:
        # If the unannotated dataset doesn't exist, use the training dataset
        dataset_to_embed = dataset
        print(f"Using training dataset for embedding: {dataset_to_embed.name}")
    
    # Or, if you used a custom dataset named 'MyCustomImageData' and want to embed it:
    # dataset_to_embed = project.datasets.get(dataset_name='MyCustomImageData')

    if dataset_to_embed:
        print(f"Starting embedding for dataset: '{dataset_to_embed.name}' (ID: {dataset_to_embed.id}) using model '{finetuned_model.name}'.")
        embedding_execution = finetuned_model.embed_datasets(dataset_ids=[dataset_to_embed.id])
        print(f"Embedding process initiated. Execution ID: {embedding_execution.id}. This may take some time.")
        print(f"You can monitor the embedding progress in the Dataloop platform.")
        
        # You can wait for this execution to complete similarly to the training execution if needed.
        # embedding_execution.wait() or a loop with time.sleep()
    else:
        print("Error: 'dataset_to_embed' is not defined. Please specify the correct original image dataset.")
else:
    print(f"Skipping embedding: Model is not successfully deployed. Current status: {finetuned_model.status if 'finetuned_model' in locals() else 'Model not defined'}")
```

## <a id='conclusion'></a>5. Conclusion and Next Steps

Congratulations! You have successfully walked through the process of fine-tuning a CLIP model using the Dataloop platform.

### Summary of What You've Accomplished:
- **Environment Setup:** Connected to Dataloop and configured your project for CLIP model fine-tuning
- **Dataset Preparation:** Prepared a dataset of images and descriptions, either by using a public dataset or learning how to upload custom data
- **Model Installation:** Installed the CLIP model package from the Dataloop Marketplace
- **Model Configuration:** Configured and cloned a pretrained CLIP model with appropriate hyperparameters
- **Model Training:** Fine-tuned the model on your dataset with proper monitoring and error handling
- **Model Deployment:** Deployed the fine-tuned model as a service for inference
- **Embedding Generation:** Generated embeddings for an image dataset using your fine-tuned model

### Next Steps:
- **Experiment with Hyperparameters:** Adjust learning rate, batch size, number of epochs, and CLIP model architecture (e.g., `ViT-L/14` if available and supported) to potentially improve performance
- **Evaluate Your Model:** While this tutorial focuses on the fine-tuning process, a crucial next step is to evaluate your fine-tuned model's performance on a held-out test set for tasks like image-text retrieval or zero-shot classification
- **Use Embeddings:** Explore applications of the generated embeddings, such as building a semantic image search engine or performing image clustering
- **Advanced Fine-tuning:** Experiment with different fine-tuning strategies, such as freezing certain layers or using different learning rates for different parts of the model
- **Multi-modal Applications:** Build applications that leverage both image and text understanding capabilities of your fine-tuned CLIP model
- **Integration with Pipelines:** Incorporate your CLIP model into automated workflows for content analysis, recommendation systems, or quality assessment

### Additional Resources:
- **[Dataloop Model Management](https://developers.dataloop.ai/tutorials/model_management):** Learn more about managing and versioning models
- **[CLIP Research Paper](https://arxiv.org/abs/2103.00020):** Understand the theoretical foundations of CLIP
- **[Dataloop Developer Documentation](https://developers.dataloop.ai/):** Explore many more features for MLOps, data management, and AI development

This tutorial demonstrates the power of combining state-of-the-art multimodal models with a comprehensive MLOps platform. Your fine-tuned CLIP model is now ready to power intelligent image-text applications!
