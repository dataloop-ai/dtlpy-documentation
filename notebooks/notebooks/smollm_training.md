# SmolLM Fine-Tuning with QLoRA

This notebook provides a comprehensive guide on fine-tuning the [HuggingFaceTB/SmolLM-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM-1.7B-Instruct) model using the Dataloop platform and its Python SDK. SmolLM-1.7B-Instruct is a compact yet powerful language model optimized for instruction-following tasks, making it ideal for chatbots, question answering, and text generation applications.

Fine-tuning allows you to adapt the pre-trained SmolLM model to your specific dataset and domain, improving its performance on tasks relevant to your use case. This tutorial demonstrates the complete workflow from data preparation through model deployment.

### What is QLoRA?

**QLoRA (Quantized Low-Rank Adaptation)** is an efficient fine-tuning technique that enables training large language models with significantly reduced memory requirements. It combines:

- **4-bit Quantization:** The base model is loaded in 4-bit precision, dramatically reducing GPU memory usage
- **LoRA (Low-Rank Adaptation):** Instead of updating all model weights, LoRA adds small trainable adapter layers to specific modules (like attention layers), keeping the original weights frozen
- **Paged Optimizers:** Memory-efficient optimizers that handle GPU memory spikes gracefully

This approach allows fine-tuning billion-parameter models on consumer GPUs while maintaining quality comparable to full fine-tuning.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.8+ installed with pip.
* **Project Access:** Ability to create projects and install apps from the Dataloop Marketplace.
* **Basic ML Knowledge:** Understanding of machine learning concepts and language models.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Environment Setup](#environment-setup)
3. [Prepare Dataset for Fine-Tuning](#prepare-dataset)
4. [Fine-Tune and Deploy SmolLM Model](#finetune-deploy-smollm)
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

> **_NOTE:_** This tutorial assumes you are working in a new project which does NOT have the SmolLM model previously installed. If it's an existing project and you already have SmolLM installed, you will need to get the appropriate app and base SmolLM model entity for the rest of the code to work correctly.


```python
if dl.token_expired():
    dl.login()

# Define a unique name for your project or change it to your own project name
user_email = dl.info()['user_email']
user_prefix = user_email.split('@')[0].replace('.', '').replace('-', '') # Simple prefix from email
project_name = f'{user_prefix}-Smollm-tutorial'

# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=project_name)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=project_name)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")
```

**Action Required:** In the cell above, you can modify `"{user_prefix}-Smollm-tutorial"` with the desired name for your Dataloop project. If a project with this name already exists, the SDK will retrieve it; otherwise, a new project will be created.

## <a id='prepare-dataset'></a>3. Prepare Prompts Dataset for Fine-Tuning

Fine-tuning a SmolLM model requires a **Prompts Dataset** containing prompt items with the desired responses as annotations. You will need to create and upload your own dataset of prompt items.

In Dataloop, prompts are special item types that represent text-based inputs for language models:
- **Prompt Item**: Contains the user's input/question/instruction
- **Response Annotation**: Contains the expected model response as an annotation on the prompt

> 💡 **In this example**, we will demonstrate how to create an annotated prompt dataset from a typical labeled dataset, converting your existing labeled data into a format suitable for LLM fine-tuning in Dataloop.

> 📖 **Learn more about Prompts:** [Prompt Items Documentation](https://developers.dataloop.ai/tutorials/annotations/prompts/chapter)

### 3.1 Prepare Your Training Data

If your dataset looks like the example below, you can use the code in the next cell to upload it as prompt items:

```json
[
    {
        "messages": [
            {"role": "user", "content": "What is a DPK in Dataloop?"},
            {"role": "assistant", "content": "A DPK (Dataloop Package Kit) is a deployable unit in Dataloop that contains code, models, and configurations. It packages your ML pipelines, model adapters, and services into a single deployable artifact that can be versioned, shared, and deployed across different environments."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What is the dataloop.json manifest file?"},
            {"role": "assistant", "content": "The dataloop.json is a manifest file that defines a Dataloop package (DPK). It contains metadata like the package name, version, modules, services, and model configurations. It specifies entry points, runtime requirements, compute resources, and how the package should be deployed and executed on the Dataloop platform."}
        ]
    }
]
```

To use the code below prepare two JSON files:
- **`train_dataloop.json`**: Training data (majority of your examples)
- **`val_dataloop.json`**: Validation data (held-out examples for evaluation)


```python
import json
import os
import dtlpy as dl

# ============ CONFIGURATION ============
DATASET_NAME = "smollm-training-prompts"  # Change this to your desired dataset name
TRAIN_JSON = "train_dataloop.json"
VAL_JSON = "val_dataloop.json"
# ========================================

# Create or get dataset
try:
    dataset = project.datasets.create(dataset_name=DATASET_NAME)
    print(f"Created new dataset: '{dataset.name}' (ID: {dataset.id})")
except dl.exceptions.BadRequest:
    dataset = project.datasets.get(dataset_name=DATASET_NAME)
    print(f"Retrieved existing dataset: '{dataset.name}' (ID: {dataset.id})")


def create_prompt_item_from_messages(name: str, messages: list, dataset: dl.Dataset) -> dl.Item:
    """Create a Dataloop PromptItem from chat messages. Assistant response becomes the annotation."""
    prompt_item = dl.PromptItem(name=name)
    
    # Create prompt for user messages
    prompt = dl.Prompt(key="1")
    assistant_content = None
    
    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")
        
        if role == "assistant":
            # Save for annotation
            assistant_content = content
        elif role == "user":
            # Add user message as prompt element
            prompt.add_element(
                mimetype=dl.PromptType.TEXT,
                value=content
            )
    
    prompt_item.prompts.append(prompt)
    
    # Upload prompt item
    uploaded_item = dataset.items.upload(prompt_item)
    
    # Add assistant response as annotation using PromptItem.add()
    if assistant_content:
        # Get PromptItem from uploaded item
        prompt_item_uploaded = dl.PromptItem.from_item(uploaded_item)
        prompt_item_uploaded.add(
            message={
                "role": "assistant",
                "content": [{"mimetype": dl.PromptType.TEXT, "value": assistant_content}]
            },
            prompt_key="1"
        )
    
    return uploaded_item


def upload_prompt_items(train_path: str, val_path: str):
    """Upload training and validation prompt items to the dataset."""
    
    # Process and upload training data
    if os.path.exists(train_path):
        with open(train_path, "r", encoding="utf-8") as f:
            train_data = json.load(f)
        
        print(f"Uploading {len(train_data)} training prompt items...")
        for i, item in enumerate(train_data):
            uploaded = create_prompt_item_from_messages(
                name=f"train_prompt_{i:04d}",
                messages=item.get("messages", []),
                dataset=dataset
            )
            # Add train tag
            uploaded.metadata["system"]["tags"] = {"train": True}
            uploaded.update(system_metadata=True)
        print(f"Uploaded {len(train_data)} training items")
    else:
        print(f"Training file not found: {train_path}")
    
    # Process and upload validation data
    if os.path.exists(val_path):
        with open(val_path, "r", encoding="utf-8") as f:
            val_data = json.load(f)
        
        print(f"Uploading {len(val_data)} validation prompt items...")
        for i, item in enumerate(val_data):
            uploaded = create_prompt_item_from_messages(
                name=f"val_prompt_{i:04d}",
                messages=item.get("messages", []),
                dataset=dataset
            )
            # Add validation tag
            uploaded.metadata["system"]["tags"] = {"validation": True}
            uploaded.update(system_metadata=True)
        print(f"Uploaded {len(val_data)} validation items")
    else:
        print(f"Validation file not found: {val_path}")
    
    print(f"\n Done! Dataset '{dataset.name}' now contains {dataset.items_count} items")


# Run the upload
upload_prompt_items(TRAIN_JSON, VAL_JSON)
```

## <a id='finetune-deploy-smollm'></a>4. Fine-Tune and Deploy SmolLm  Model

With the dataset prepared, we can now proceed to fine-tune the SmolLm model.

### 4.1 Install SmolLm Model Package (DPK)

First, we install the SmolLm model DPK from the Dataloop Marketplace. This package provides the necessary components for SmolLm model training and inference.


```python
smollm_model_dpk = dl.dpks.get(dpk_name="smollm-instruct-fine-tune")
try:
    model_app = project.apps.install(
        app_name=smollm_model_dpk.display_name, 
        dpk=smollm_model_dpk, 
        custom_installation=smollm_model_dpk.to_json()
    )
    print(f"Installed {smollm_model_dpk.display_name} app: {model_app.name}, ID: {model_app.id}")
except dl.exceptions.BadRequest as e:
    print(f"{smollm_model_dpk.display_name} app already installed, getting existing app")
    model_app = project.apps.get(app_name=smollm_model_dpk.display_name)
    print(f"Retrieved existing app: {model_app.name}, ID: {model_app.id}")
```

### 4.2 Configure and Clone Pretrained SmolLm Model

Next, we retrieve the base pre-trained SmolLm model entity ("HuggingFaceTB/SmolLM-1.7B-Instruct") provided by the DPK. We'll then configure its metadata, specifying which subsets of our `dataset` to use for training and validation.

You can also adjust model hyperparameters like LoRa parameters, learning rate, and number of epochs in the `base_model.configuration` dictionary. The example settings below are a starting point.


```python
base_model = project.models.get(model_name="HuggingFaceTB/SmolLM-1.7B-Instruct")
print(f"Retrieved base SmolLm model: {base_model.name} (ID: {base_model.id})")

# Configure model metadata and subsets
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
val_filters = dl.Filters(field="metadata.system.tags.validation", values=True)

# Add subsets to the model
base_model.add_subset(subset_name="train", subset_filter=train_filters)
base_model.add_subset(subset_name="validation", subset_filter=val_filters)

# Set model configuration (hyperparameters for SmolLM fine-tuning with LoRA)
base_model.configuration = {
    # LoRA (Low-Rank Adaptation) parameters
    "r": 8,                                    # LoRA rank
    "lora_alpha": 16,                          # LoRA scaling factor
    "lora_dropout": 0.05,                      # Dropout for LoRA layers
    "task_type": "CAUSAL_LM",                  # Task type for causal language modeling
    "target_modules": ["q_proj", "v_proj", "k_proj", "o_proj"],  # Layers to apply LoRA
    
    # Training parameters
    "num_train_epochs": 5,                    # Number of training epochs
    "per_device_train_batch_size": 1,          # Batch size per device
    "gradient_accumulation_steps": 16,         # Effective batch size = 1 * 16 = 16
    "learning_rate": 2e-4,                     # Learning rate
    "warmup_ratio": 0.03,                      # Warmup steps as ratio of total
    "lr_scheduler_type": "constant",           # Learning rate scheduler
    "max_grad_norm": 0.3,                      # Gradient clipping
    
    # Optimization
    "optim": "paged_adamw_32bit",              # Optimizer
    "bf16": True,                              # Use bfloat16 precision
    "gradient_checkpointing": True,            # Memory optimization
    "group_by_length": True,                   # Group similar length sequences
    
    # Logging and saving
    "logging_steps": 10,                       # Log every N steps
    "save_steps": 10,                          # Save checkpoint every N steps
    "save_total_limit": 3,                     # Keep only last 3 checkpoints
}

# Update the model to save configurations
base_model.update(system_metadata=True)

print(f"Base model configured with:")
print(f"  LoRA rank (r): {base_model.configuration['r']}")
print(f"  LoRA alpha: {base_model.configuration['lora_alpha']}")
print(f"  Epochs: {base_model.configuration['num_train_epochs']}")
print(f"  Batch size: {base_model.configuration['per_device_train_batch_size']}")
print(f"  Gradient accumulation: {base_model.configuration['gradient_accumulation_steps']}")
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

Once the model has successfully trained, you can deploy it as a service. This makes the model available for inference tasks, such as text generation and conversational AI.


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

### 4.6 Test the Fine-Tuned SmolLM Model

After the fine-tuned model is deployed and its service is ready, you can test it by sending prompts and receiving generated responses. This allows you to verify that the model has learned from your training data and responds appropriately to queries in your domain.


```python
if 'finetuned_model' in locals() and finetuned_model.status == dl.ModelStatus.DEPLOYED:
    # Create a test prompt to ask the fine-tuned model
    test_question = "What is a DPK in Dataloop?"  # Change this to test with your own questions
    
    # Create a PromptItem for testing
    test_prompt = dl.PromptItem(name="test_prompt")
    prompt = dl.Prompt(key="1")
    prompt.add_element(mimetype=dl.PromptType.TEXT, value=test_question)
    test_prompt.prompts.append(prompt)
    test_item = dataset.items.upload(test_prompt,overwrite=True)
    
    print(f"Testing fine-tuned model: '{finetuned_model.name}'")
    print(f"Question: {test_question}")
    print("-" * 50)
    
    # Execute prediction on the deployed model
    execution = finetuned_model.predict(item_ids=[test_item])
    execution.wait()
    
    # Get the response
    # Wait for execution to complete
    while True:
        execution = dl.executions.get(execution_id=execution.id)
        status = execution.latest_status['status']
        if status in ['success', 'failed']:
            break
        print(f"Status: {status}, waiting...")
        time.sleep(10)

    # Check final status
    if execution.latest_status['status'] == dl.ExecutionStatus.SUCCESS.value:
        print(f"✅ Execution Excecuted Successfully!")
        print(execution.output)
    else:
        print(f"❌ Prediction failed. Status: {execution.status}")
        print(f"Check logs in Dataloop platform for details.")
else:
    print(f"Skipping test: Model is not deployed. Status: {finetuned_model.status if 'finetuned_model' in locals() else 'Model not defined'}")

print("\n" + "="*50)
print("SmolLM Fine-Tuning Complete!")
print("="*50)
```

## <a id='conclusion'></a>5. Conclusion and Next Steps

Congratulations! You have successfully walked through the process of fine-tuning a SmolLM model using the Dataloop platform.

### Summary of What You've Accomplished:
- **Environment Setup:** Connected to Dataloop and configured your project for SmolLM model fine-tuning
- **Dataset Preparation:** Created a prompts dataset with prompt items and response annotations from your training data
- **Model Installation:** Installed the SmolLM model app from the Dataloop Marketplace
- **Model Configuration:** Configured the pretrained SmolLM model with LoRA and appropriate hyperparameters
- **Model Training:** Fine-tuned the model on your prompts dataset with proper monitoring
- **Model Deployment:** Deployed the fine-tuned model as a service for inference
- **Model Testing:** Tested the fine-tuned model with sample prompts

### Next Steps:
- **Expand Your Dataset:** Add more diverse prompt-response pairs to improve model performance on your specific domain
- **Experiment with Hyperparameters:** Adjust LoRA rank, learning rate, number of epochs, and batch size to optimize results
- **Evaluate Your Model:** Systematically evaluate the fine-tuned model's performance on held-out test prompts
- **Advanced Fine-tuning:** Experiment with different LoRA configurations or target modules for better performance
- **Build Applications:** Integrate your fine-tuned SmolLM into chatbots, assistants, or other NLP applications
- **Integration with Pipelines:** Incorporate your SmolLM model into automated workflows for content generation or Q&A systems

### Additional Resources:
- **[Dataloop Model Management](https://developers.dataloop.ai/tutorials/model_management):** Learn more about managing and versioning models
- **[LoRA Paper](https://arxiv.org/abs/2106.09685):** Understanding Low-Rank Adaptation for efficient fine-tuning
- **[Dataloop Developer Documentation](https://developers.dataloop.ai/):** Explore many more features for MLOps, data management, and AI development

This tutorial demonstrates how to efficiently fine-tune small language models for your specific use case. Your fine-tuned SmolLM model is now ready to power intelligent conversational applications!
