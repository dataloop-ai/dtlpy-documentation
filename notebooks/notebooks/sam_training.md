# SAM2 (Segment Anything Model 2) Tutorial

This notebook provides a comprehensive guide on how to use SAM2 (Segment Anything Model 2), a powerful image segmentation model by Meta AI, with the Dataloop platform and its Python SDK. We will cover the full workflow from setup to model training and evaluation.

SAM2 represents a significant advancement in image segmentation, offering improved accuracy and efficiency for various computer vision tasks. This tutorial will help you leverage SAM2's capabilities within the Dataloop ecosystem for your segmentation projects.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **Dataset Access:** A Dataloop project and dataset with images for segmentation tasks.
* **GPU Resources:** Recommended for training and inference (though CPU is supported for basic operations).

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Environment Setup and Dataloop Connection](#environment-setup)
3. [Project and Dataset Configuration](#project-dataset-config)
4. [Load and Visualize Data](#load-visualize-data)
5. [SAM2 Prediction](#sam2-prediction)
6. [SAM2 Training](#sam2-training)
7. [Model Evaluation](#model-evaluation)
8. [Conclusion and Next Steps](#conclusion)

For more details about SAM2 in the Dataloop platform, refer to the [Dataloop SAM Github repository](https://github.com/dataloop-ai-apps/grounded-sam-adapter/tree/main/adapters/sam_adapter).

## <a id='dependencies-setup'></a>1. Dependencies & Setup

First, let's ensure all required Python packages are installed. The cell below will install `dtlpy` for Dataloop SDK interaction, along with `matplotlib`, `numpy`, and `Pillow` for data handling and visualization.


```python
!pip install dtlpy matplotlib numpy Pillow --upgrade --quiet
```

## <a id='environment-setup'></a>2. Environment Setup and Dataloop Connection

### Import Required Libraries

With dependencies installed, we'll import the necessary libraries and establish a connection to the Dataloop platform. If your Dataloop token is expired or not found, you will be prompted to log in.


```python
# Import necessary libraries
import dtlpy as dl
import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# Login to the Dataloop platform
# This will check if your current token is valid and prompt for login if necessary.
if dl.token_expired():
    dl.login()
print('Successfully logged into Dataloop')
```

## <a id='project-dataset-config'></a>3. Project and Dataset Configuration

Now, we need to specify the Dataloop project and dataset you'll be working with.

**Action Required:** In the code cell below, please replace `'your_project_name'` and `'your_dataset_name'` with the names of your Dataloop project and dataset, respectively. The dataset should contain images, which can be with or without existing annotations.


```python
# Get the project
# IMPORTANT: Modify 'your_project_name' to your specific Dataloop project name.
project = dl.projects.get(project_name='your_project_name')
print(f'Connected to project: {project.name}')

# Get the dataset
# IMPORTANT: Modify 'your_dataset_name' to your specific Dataloop dataset name.
dataset = project.datasets.get(dataset_name='your_dataset_name')
print(f'Connected to dataset: {dataset.name}')
```

## <a id='load-visualize-data'></a>4. Load and Visualize Data

Let's select a random image from our dataset and visualize it. If the image has existing annotations, we'll display those as well. This helps in understanding the data we're working with.

### 4.1 Select Random Item

We'll randomly select an item from the dataset to work with throughout this tutorial.


```python
# Get a random item from the dataset
items_list = list(dataset.items.list().all)
if items_list:
    item = items_list[random.randint(0, len(items_list) - 1)]
    print(f"Selected random item: {item.name} (ID: {item.id})") 
else:
    print("No items found in the dataset!")
    item = None
```

### 4.2 Helper Function for Visualization

This function will help us display images and their annotations in a consistent format throughout the tutorial.


```python
def display_item_with_annotations(item):
    """
    Display an image item and its annotations
    
    Args:
        item: A Dataloop item object
    """
    if not item:
        print("No item to display")
        return
        
    # Download the image locally
    buffer = item.download(save_locally=False)
    
    # Convert buffer to image
    image = Image.open(io.BytesIO(buffer))
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.title(f"Image: {item.name}")
    plt.show()
    
    # Get annotations for the item
    annotations = item.annotations.list()
    if annotations.items:
        print(f"Found {len(annotations.items)} annotations")
        
        # Display image with annotations
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        
        # Plot each annotation
        for annotation in annotations.items:
            if hasattr(annotation, 'coordinates'):
                coords = np.array(annotation.coordinates)
                if annotation.type == 'box':
                    x, y, w, h = coords
                    plt.gca().add_patch(plt.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=2))
                    plt.text(x, y, annotation.label, color='white', backgroundcolor='red', fontsize=8)
                elif annotation.type == 'polygon':
                    plt.plot(coords[:, 0], coords[:, 1], 'r-', linewidth=2)
                    plt.text(coords[0, 0], coords[0, 1], annotation.label, color='white', backgroundcolor='red', fontsize=8)
                elif annotation.type == 'point':
                    plt.scatter(coords[0], coords[1], c='red', s=50)
                    plt.text(coords[0], coords[1], annotation.label, color='white', backgroundcolor='red', fontsize=8)
                elif annotation.type == 'segmentation':
                    # Assuming annotation.geo is a Dataloop geo object for segmentation
                    # The geo_to_mask method requires image height and width
                    mask = annotation.geo.geo_to_mask((image.height, image.width)) 
                    plt.imshow(mask, alpha=0.5, cmap='jet')
                    
        plt.axis('off')
        plt.title("Image with Annotations")
        plt.show()
    else:
        print("No annotations found for this item")
```

### 4.3 Visualize Selected Item

Display the randomly selected item and its annotations both in the notebook and optionally in the Dataloop platform.


```python
# Show the item and item annotations in the notebook
display_item_with_annotations(item)
```


```python
# Show the item and item annotations in the platform
# This will open the item in your web browser, in the Dataloop annotation studio.
item.open_in_web()
```

## <a id='sam2-prediction'></a>5. SAM2 Prediction

We will now use a pre-trained SAM2 model available on the Dataloop platform to perform image segmentation. SAM2 in Dataloop supports multiple prediction modes:

### SAM2 Prediction Modes:

1. **Zero-shot Segmentation (No Annotations Provided):**
   - If no specific annotations (like boxes or points) are on the item, a bounding box encompassing the entire image is implicitly passed to the model.
   - The model typically returns a binary mask for the most prominent object it identifies in the image.

2. **Box-guided Segmentation:**
   - Users can provide bounding box annotations around specific areas of interest.
   - The model generates segmentation masks for objects within these specified bounding boxes.

3. **Point-based Segmentation:**
   - Users can input point annotations indicating specific locations inside different objects.
   - The model returns a segmentation mask for each object that contains an indicated point.

4. **Multi-points Segmentation (Advanced):**
   - Users can provide multiple points, labeled as "inside" (positive) or "outside" (negative) the object of interest.
   - The model uses these labeled points to generate more refined segmentation masks.
   - This mode may require specific model configuration, such as `multi_points_prediction=true`.

### 5.1 Install and Configure SAM2 Model

First, we need to get the SAM2 DPK (Dataloop Package), install it as an app in our project (if not already installed), and then retrieve the associated model.


```python
# Get the SAM2 DPK (Dataloop Package)
sam2_dpk = dl.dpks.get(dpk_name='sam2')

# Install the SAM2 app from the DPK if not already installed in the project
try:
    sam2_app = project.apps.install(app_name=sam2_dpk.display_name, dpk=sam2_dpk, custom_installation=sam2_dpk.to_json())
except dl.exceptions.BadRequest as e: # Catch error if app is already installed
    print(f"App {sam2_dpk.display_name} already installed, getting existing app instance.")
    sam2_app = project.apps.get(app_name=sam2_dpk.display_name)

# Get the SAM2 model associated with the installed app
# Models are typically created when an app is installed or can be managed separately.
filters = dl.Filters(resource=dl.FiltersResource.MODEL)
filters.add(field='app.id', values=sam2_app.id)
model = project.models.list(filters=filters)[0][0]
```

### 5.2 Deploy and Configure Model

Ensure the model is deployed before making predictions. If the model is not deployed, the following cell will attempt to deploy it. The model's configuration is also displayed for reference.


```python
print(f'\nLoaded model: {model.name}')

# Check model status and deploy if not already deployed
if model.status != 'deployed':
    print('Deploying model...')
    model.deploy() # This deploys the model with default settings
print(f'Model status: {model.status}')

# Display model configuration for reference
print('\nModel configuration:')
for key, value in model.configuration.items():
    print(f'{key}: {value}')
```

### 5.3 Run Prediction

Now, let's make a prediction on the randomly selected item. If the item has no annotations, SAM2 will perform zero-shot segmentation. If it has box or point annotations, those will guide the segmentation.


```python
# Make prediction
prediction = model.predict(item_ids=[item.id])
prediction.wait() # Wait for the prediction process to complete
print('Prediction completed successfully')

# Get updated item with predictions
# The item in the dataset will now have new annotations generated by the model.
updated_item = dataset.items.get(item_id=item.id)
```

### 5.4 Visualize Prediction Results

Let's visualize the item with the newly added prediction annotations.


```python
# Show the item and item annotations (including predictions) in the notebook
display_item_with_annotations(updated_item)
```


```python
# Show the item and item annotations (including predictions) in the platform
updated_item.open_in_web()
```

### 5.5 Experiment: Prediction with Prompts

The predictions above show the model's segmentation results, which will typically be mask annotations. You can experiment with different prediction modes by:

- Providing bounding boxes for box-guided segmentation (as we'll try next).
- Using point-based segmentation by adding point annotations to an item before prediction.
- Testing multi-point predictions with appropriately labeled points, if supported by your model configuration.

Remember to check the [SAM2 model documentation](https://github.com/dataloop-ai-apps/grounded-sam-adapter/tree/main/adapters/sam_adapter) for detailed configuration options and best practices for different modes.

#### Option 1: Adding a Bounding Box via the Dataloop UI

1. Run the cell below to open the selected item in the Dataloop annotation studio.
2. Use the bounding box tool in the UI to draw a box around an object of interest.
3. Assign a label to the box (e.g., "target_object").
4. Save the annotation.
5. Once saved, continue to the cells below to run prediction on this modified item.


```python
# Run this cell to open the item in the Dataloop UI for manual annotation
# After adding and saving a bounding box in the UI, come back to this notebook.
item.open_in_web()
```

#### Option 2: Adding a Bounding Box Programmatically

Alternatively, use the Dataloop SDK to add a bounding box annotation to the item. Adjust the coordinates and label as needed. Note that the coordinates `(left, top, right, bottom)` are in pixels.


```python
# Define and upload a bounding box annotation
image_annotation = dl.AnnotationCollection()
image_annotation.add(annotation_definition=dl.Box(left=float(100),  # left coordinate in pixels from the left edge of the image
                                                top=float(100),    # top coordinate in pixels from the top edge of the image
                                                right=float(200),  # right coordinate in pixels from the left edge of the image
                                                bottom=float(200), # bottom coordinate in pixels from the top edge of the image
                                                label='your_label' # Assign a meaningful label to your prompt box
                                                ))
item.annotations.upload(image_annotation)
```

### 5.6 Run Prediction with Prompts

Now, let's run a prediction on the item, which now includes a bounding box prompt (either added via UI or code). We first refetch the item to ensure we have the latest version with the prompt annotation.


```python
# Fetch the item again to get any annotations added via UI or code
annotated_item = dataset.items.get(item_id=item.id)

# Make prediction using the item with the prompt
prediction = model.predict(item_ids=[annotated_item.id])
prediction.wait()
print('Prediction completed successfully')

# Get updated item with predictions based on the prompt
updated_item = dataset.items.get(item_id=item.id)
```

### 5.7 Visualize Prompt-Guided Results

Visualize the result of the prompt-guided prediction.


```python
# Show the item and its annotations (including new predictions) in the notebook
display_item_with_annotations(updated_item)
```


```python
# Show the item and its annotations in the platform
updated_item.open_in_web()
```

## <a id='sam2-training'></a>6. SAM2 Training

To fine-tune SAM2 on your own dataset, we first need to clone the pre-trained model. This creates a new model artifact that you own and can modify. We will then associate our dataset with this cloned model for training.

### 6.1 Clone Model for Training

Clone the base SAM2 model to create a trainable version. It's good practice to give the cloned model a descriptive name.


```python
# Clone the base SAM2 model to create a trainable version
# It's good practice to give the cloned model a descriptive name.
clone_model = model.clone(model_name=f"{model.name}-finetuned", # Or provide a new name like f"{model.name}-finetune"
                          dataset=dataset, # Associate the dataset for training context
                          description='Cloned model for training')

print('Model cloned successfully')
```

### 6.2 Configure Training Parameters

We can inspect and modify the configuration of this cloned model. For example, training parameters like the number of epochs, batch size, or learning rate can be adjusted.


```python
# Display the configuration of the cloned model
print('\nCloned model configuration:')
for key, value in clone_model.configuration.items():
    print(f'{key}: {value}')
```

### 6.3 Update Training Configuration

For instance, let's say we want to change the number of training epochs. You can do this directly in the Dataloop platform UI by opening the model's page, or programmatically via the SDK.

To change configuration in the UI, run the cell below to open the cloned model's page in your browser. Navigate to the configuration settings and make your edits (e.g., set 'num_epochs' or 'epochs' to 10).


```python
# Option 1: Open the cloned model in the Dataloop UI to modify configuration
clone_model.open_in_web()
```

Alternatively, update the configuration using the SDK. The exact key for the number of epochs might vary (e.g., `num_epochs`, `epochs`). Check your model's specific configuration.


```python
# Option 2: Modify configuration programmatically (e.g., number of epochs)
# Make sure the key 'num_epochs' (or similar, like 'epochs') exists in your model's configuration.
clone_model.configuration['num_epochs'] = 10 # Set desired number of epochs
clone_model.update() # Save the changes
```

### 6.4 Verify Configuration Changes

Let's verify the configuration change by displaying it again. If you changed it via UI, re-fetch the model first.


```python
clone_model = dl.models.get(model_id=clone_model.id)
```


```python
# Display model configuration again to confirm changes
print('\nUpdated model configuration:')
for key, value in clone_model.configuration.items():
    print(f'{key}: {value}')
```

### 6.5 Prepare Data Subsets for Training

For effective model training, it's crucial to split your dataset into training, validation, and (optionally) test subsets. Dataloop provides tools to manage these splits. Here, we'll split our dataset items based on percentages. The items will be tagged accordingly (e.g., 'train', 'validation', 'test').

For more information on dataset splitting and subsets, refer to the [Dataloop documentation on ML Subsets](https://developers.dataloop.ai/tutorials/data_management/datasets_and_versioning/chapter#ml-subsets-your-datasets-secret-sauce-).


```python
# Add subsets to the dataset
# This operation tags items with 'train', 'validation', or 'test'.
filters = dl.Filters(field='type', values='file') # Filter to select only 'file' type items (e.g., images)
dataset.split_ml_subsets(
    # Define the query to filter items (only files in this case)
    items_query=filters,
    # Split the dataset into train (60%), validation (20%), and test (20%) subsets
    # These will be used for training, validating, and testing the model respectively
    # Adjust percentages as needed for your dataset size and requirements.
    percentages={'train': 60, 'validation': 20, 'test': 20}
)
```

### 6.6 Configure Model Subsets and Start Training

Next, we need to inform the cloned model which items belong to the training and validation sets. We do this by creating filters based on the subset tags (e.g., `metadata.system.tags.train`) and adding these subsets to the model. Then, we initiate the training process.


```python
# Create filters to select items tagged as 'train' and 'validation'
# These tags are automatically added by the split_ml_subsets method.
train_filters = dl.Filters(field="metadata.system.tags.train", values=True)
validation_filters = dl.Filters(field="metadata.system.tags.validation", values=True)

# Add the train subset to the model, specifying the dataset and the filter
# This tells the model which items to use for training
clone_model.add_subset(subset_name="train", subset_filter=train_filters) # dataset_id is taken from clone_model.dataset_id if not specified

# Add the validation subset to the model
# This tells the model which items to use for validation during training
clone_model.add_subset(subset_name="validation", subset_filter=validation_filters)

# Update the model to save the subset configurations
# The system_metadata=True parameter ensures system metadata (like subset definitions) is updated.
clone_model.update(system_metadata=True)

# Start the model training process
# This will use the items defined in the 'train' and 'validation' subsets.
# This returns an execution object that can be used to track training progress.
execution = clone_model.train()

# Print confirmation message
print('Model training started successfully')
print(f"Training initiated. Execution ID: {execution.id}")
```

### 6.7 Wait for Training Completion

Training can take a significant amount of time, depending on the dataset size, model complexity, and hardware resources. The `execution.wait()` call will block the notebook until training is finished or fails.


```python
# Wait for the training execution to complete
execution.wait() 
print('Model training finished successfully')
```

### 6.8 Monitor Training Progress

You can navigate to the 'Training' tab on the model's page in the Dataloop UI to view detailed progress, logs, and performance metrics as the training runs. The cell below will open this page for you.


```python
# Open the model page in the Dataloop platform to monitor training
clone_model.open_in_web()
```

## <a id='model-evaluation'></a>7. Model Evaluation

After the training process is complete, it's essential to evaluate the performance of your fine-tuned model. We'll use the 'test' subset of our data, which the model has not seen during training or validation, for this purpose. The evaluation process runs predictions on the test set and compares them to ground truth annotations to calculate metrics.

### 7.1 Start Model Evaluation

Create filters to select items tagged as 'test' and start the evaluation process.


```python
# Create filters to select items tagged as 'test'
# This filter will identify all items in the dataset that have been tagged for testing.
test_filters = dl.Filters(field='metadata.system.tags.test', values=True)

# Start the model evaluation process on the test subset
# - dataset_id: Specifies which dataset to use for evaluation (taken from clone_model.dataset_id by default if associated).
# - filters: Applies the test filters to only evaluate on test items.
execution = clone_model.evaluate(dataset_id=dataset.id, # Explicitly providing dataset.id
                                 filters=test_filters)

# Print confirmation message
print('Model evaluation started successfully')
```

### 7.2 Wait for Evaluation Completion

Similar to training, evaluation can take some time. The `execution.wait()` call will block until it's complete.


```python
# Wait for the evaluation execution to complete
execution.wait()
print('Model evaluation finished successfully')
```

### 7.3 View Evaluation Results

Once the evaluation is finished, you can access detailed performance metrics in the Dataloop platform. These are typically found under a 'Metrics' or 'Precision-Recall' tab on the model's page.


```python
clone_model.open_in_web()
```

## <a id='conclusion'></a>8. Conclusion and Next Steps

Congratulations! You have successfully walked through the process of using SAM2 with Dataloop, including:

### Summary of What You've Accomplished:
- Set up your environment and connected to Dataloop
- Configured your project and dataset for segmentation tasks
- Visualized data and annotations using helper functions
- Performed predictions with a pre-trained SAM2 model using various prompting techniques
- Fine-tuned SAM2 on your custom dataset with proper data splitting
- Evaluated the performance of your fine-tuned model on test data

### Next Steps:
- **Explore Advanced Configurations:** Dive deeper into the SAM2 model's configuration options for both prediction and training to optimize performance for your specific use case
- **Iterate on Training:** Adjust training parameters (epochs, learning rate, batch size), dataset composition, and augmentation strategies to improve your fine-tuned model
- **Deploy Your Trained Model:** Once satisfied with your fine-tuned model, deploy it as a service to use it for inference on new, unseen data within your Dataloop workflows or external applications
- **Analyze Evaluation Metrics:** Thoroughly review the evaluation metrics in the Dataloop platform to understand your model's strengths and weaknesses
- **Integration with Pipelines:** Incorporate your trained SAM2 model into automated annotation pipelines for production use

This notebook provides a foundational guide. The Dataloop platform offers many more features for comprehensive AI data management and model development. We encourage you to explore the [Dataloop documentation](https://dataloop.ai/docs) for more advanced topics and functionalities.
