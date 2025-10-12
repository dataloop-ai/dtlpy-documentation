# Getting Started with the Dataloop Python SDK (dtlpy) Tutorial

Welcome! This notebook provides a comprehensive introduction to interacting with the Dataloop platform using its Python SDK, `dtlpy`. The Dataloop SDK enables you to programmatically manage your data, annotations, models, and workflows, making it an essential tool for building scalable AI applications.

This tutorial covers the fundamental concepts and operations you'll need to get started with Dataloop, from basic authentication through advanced annotation workflows.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **Basic Python Knowledge:** Familiarity with Python programming concepts.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Projects](#projects)
3. [Datasets](#datasets)
4. [Setting the Ontology and Recipe](#setting-ontology-recipe)
5. [Items](#items)
6. [Prompt Items](#prompt-items)
7. [Annotations](#annotations)
8. [Tasks & Assignments](#tasks-assignments)
9. [Conclusion and Next Steps](#conclusion)

## <a id='dependencies-setup'></a>1. Dependencies & Setup

First, ensure you have the `dtlpy` library installed. If not, uncomment and run the following cell:

The following cell uses `pip` to install the `dtlpy` package. The `--quiet` flag suppresses installation output.


```python
!pip install dtlpy --upgrade --quiet
```

### Authentication and Connection

To interact with the Dataloop platform, you need to authenticate. The simplest way in an interactive environment like a Jupyter Notebook is using `dl.login()` which will open a browser window for you to log in via your Dataloop account (or uses saved credentials if available and valid).

Next, we import the `dtlpy` library as `dl` and the `datetime` library. We then check if the current Dataloop authentication token has expired using `dl.token_expired()`. If it has, `dl.login()` is called, which typically opens a web browser for you to log into your Dataloop account. Successful login or an active session will be confirmed with a print message.


```python
import dtlpy as dl
import datetime

if dl.token_expired():
   dl.login() # Opens browser for login
   print(f"Logged in successfully to {dl.client_api.environment}")
else:
   print(f"Session active for {dl.client_api.info()['user_email']} in {dl.client_api.environment}")
```

## <a id='projects'></a>2. Projects

Projects are the main containers for your work in Dataloop. They hold datasets, ontologies, models, tasks, pipelines, etc.

This cell defines a unique project name using your Dataloop user email to create a prefix. It then attempts to retrieve an existing project with this name using `dl.projects.get()`. If the project is not found (raising a `dl.exceptions.NotFound` error), it creates a new project with `dl.projects.create()`. This ensures you have a project to work with for this tutorial. The project's name and ID are printed upon successful retrieval or creation.


```python
# Define a unique name for your project
# Best practice: Use a combination of your username/initials and the purpose
user_email = dl.info()['user_email']
user_prefix = user_email.split('@')[0].replace('.', '').replace('-', '') # Simple prefix from email
project_name = f'{user_prefix}-sdk-getting-started'

# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=project_name)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=project_name)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")

# Print project details (optional)
# project.print()
```


```python
# You can now access the project in the web interface
# project.open_in_web()
```

The following (commented out) code demonstrates how to list all projects accessible to your Dataloop user using `dl.projects.list()` and print their details.


```python
# You can list all projects you have access to
# print("\nListing projects accessible to you:")
# my_projects = dl.projects.list()
# my_projects.print()
```

## <a id='datasets'></a>3. Datasets

Datasets reside within projects and contain your data items (images, videos, text, etc.) and their associated annotations.

Here, we define a name for our dataset. Similar to projects, we use a try-except block to get the dataset if it already exists within the `project` object (`project.datasets.get()`) or create it if it doesn't (`project.datasets.create()`). When a dataset is created, Dataloop automatically sets up a default Recipe and Ontology for it. The dataset's name and ID are printed.


```python
# Define a unique name for your dataset within the project
dataset_name = 'my-sdk-dataset'

# Check if the dataset exists within the project
# if not, create it. Dataloop automatically creates a default Recipe and Ontology.
try:
    dataset = project.datasets.get(dataset_name=dataset_name)
    print(f"Successfully retrieved dataset: '{dataset.name}' (ID: {dataset.id})")
except dl.exceptions.NotFound:
    dataset = project.datasets.create(dataset_name=dataset_name)
    print(f"Successfully created dataset: '{dataset.name}' (ID: {dataset.id}) in project '{project.name}'.")

# Print dataset details (optional)
# dataset.print()
```

This commented-out code shows how to list all datasets within the previously retrieved or created `project` using `project.datasets.list()`.


```python
# List datasets within the project we retrieved/created
# print(f"\nListing datasets in project '{project.name}'...")
# datasets = project.datasets.list()
# datasets.print()
```

## <a id='setting-ontology-recipe'></a>4. Setting the Dataset Ontology and Recipe

Before annotating, you need to define the *ontology* - the set of labels and their attributes that can be applied to your data.

In Dataloop, the relationship is:
* **Dataset:** Contains your data items.
* **Recipe:** Links a Dataset to one or more Ontologies. It defines the *schema* for annotation and QA tasks within that dataset. Every dataset must have at least one recipe.
* **Ontology:** Defines the labels (e.g., 'car', 'person', 'text bounding box') and their attributes (e.g., color, size, type).

When you create a dataset using the SDK (or UI), Dataloop automatically creates a default recipe and a default ontology for it. We will modify this default ontology to add the labels we need.

This cell handles the setup of the dataset's ontology, which defines the set of labels for annotation.
1. It retrieves the default recipe associated with our `dataset`. If, for some reason, a default recipe isn't found (which is unlikely for SDK-created datasets), it creates one and links it.
2. It then retrieves the default ontology linked to this recipe. Similarly, if an ontology isn't found, it creates an empty one and links it to the recipe.
3. A dictionary `labels_to_add` is defined with desired label names and their corresponding display colors.
4. It iterates through these labels, checking if they already exist in the `ontology.labels`. If a label doesn't exist, it's added using `ontology.add_label()`.
5. An example of adding a label with attributes (`AttributedObject`) is also shown. Attributes allow for more detailed annotation, such as boolean flags (e.g., 'Is Occluded?') or option lists (e.g., 'Object Size').
6. If any labels were added or modified, `ontology.update()` is called to save these changes to the Dataloop platform.
7. Finally, it prints the current list of labels in the ontology.


```python
# Retrieve the dataset's default recipe
# Datasets usually have one recipe by default upon creation
try:
    recipe = dataset.recipes.list()[0] # Get the first recipe (usually the default)
    print(f"Retrieved recipe: '{recipe.title}' (ID: {recipe.id})")
except IndexError:
    # This should ideally not happen for SDK-created datasets, but as a fallback:
    print("No default recipe found. Creating one...")
    recipe = dataset.recipes.create()
    dataset.metadata['system']['recipes'] = [recipe.id] # Link recipe to dataset
    dataset.update(system_metadata=True)
    print(f"Created and linked recipe: '{recipe.title}' (ID: {recipe.id})")

# Retrieve the ontology linked to the recipe
# Recipes usually have one ontology by default
try:
    ontology = recipe.ontologies.list()[0] # Get the first ontology
    print(f"Retrieved ontology: '{ontology.title}' (ID: {ontology.id}) with {len(ontology.labels)} labels initially.")
except IndexError:
    # This should also ideally not happen.
    print("No default ontology found for the recipe. Creating one...")
    ontology = recipe.ontologies.create(labels=[]) # Create empty ontology
    recipe.ontology_ids = [ontology.id] # Link ontology to recipe
    recipe.update()
    print(f"Created and linked ontology: '{ontology.title}' (ID: {ontology.id})")

# Define the labels we want to use later for annotation
labels_to_add = {
    "Object1": '#FF0000',  # Red
    "CornerPoint": '#00FF00', # Lime Green
    "IndoorScene": '#0000FF', # Blue
    "MyTextLabel": '#FFFF00' # Yellow (For potential text annotation)
}

# Add labels to the ontology if they don't exist
labels_updated = False
existing_labels = [lbl.tag for lbl in ontology.labels]

for label_name, color_hex in labels_to_add.items():
    if label_name not in existing_labels:
        print(f"Adding label '{label_name}'...")
        ontology.add_label(label_name=label_name, color=color_hex)
        labels_updated = True
    else:
        print(f"Label '{label_name}' already exists.")

# Add a simple label first, then we'll add attributes to it separately
attributes_label_name = 'AttributedObject'
if attributes_label_name not in existing_labels:
    print(f"Adding label '{attributes_label_name}'...")
    ontology.add_label(label_name=attributes_label_name, color='#FFA500')  # Orange
    labels_updated = True

# Update the ontology on the platform *only* if changes were made
if labels_updated:
    ontology = ontology.update()
    print(f"Ontology updated successfully. It now has {len(ontology.labels)} labels.")
else:
    print("No new labels needed to be added.")

# Now add attributes using the correct method
print("Adding attributes to the ontology...")

# Add a boolean attribute (Yes/No)
ontology.update_attributes(
    key='occluded',
    title='Is Occluded?',
    attribute_type=dl.AttributesTypes.YES_NO,
    scope=[attributes_label_name]  # Apply only to the AttributedObject label
)

# Add a multi-choice attribute (Radio Button)
ontology.update_attributes(
    key='size',
    title='Object Size',
    attribute_type=dl.AttributesTypes.RADIO_BUTTON,
    values=['small', 'medium', 'large'],
    scope=[attributes_label_name]  # Apply only to the AttributedObject label
)

print("Attributes added successfully!")

# Optional: Print ontology labels
print("\nCurrent Ontology Labels:")
ontology.print()
```

**Shortcut:** You can also use `dataset.add_label(...)` which automatically finds the default recipe and ontology and adds the label. This is convenient for simple cases.

```python
# Example shortcut:
# dataset.add_label(label_name='ShortcutLabel', color='#FFC0CB') 
```

## <a id='items'></a>5. Items

Items are the individual data points within a dataset (e.g., images, videos, text files, JSON).

### 5.1 Uploading Items

Let's upload sample items, an image and a text file.
Make sure you have a `data` directory with `sample.jpg` and `sample.txt` inside.

This cell prepares dummy data files for upload if they don't already exist.
1. It defines a `data_dir` ('data') and filenames for a sample image (`sample.jpg`) and text file (`sample.txt`).
2. It creates the `data_dir` if it's missing using `os.makedirs(data_dir, exist_ok=True)`.
3. If `sample.jpg` doesn't exist, it generates a small random dummy image using PIL (Pillow) and NumPy and saves it.
4. If `sample.txt` doesn't exist, it creates a simple text file with some content.


```python
import os
from PIL import Image
import numpy as np

data_dir = 'data/getting_started_with_sdk'
image_filename = 'sample.jpg'
text_filename = 'sample.txt'
image_filepath = os.path.join(data_dir, image_filename)
text_filepath = os.path.join(data_dir, text_filename)

# Create directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Create dummy image if it doesn't exist
if not os.path.exists(image_filepath):
    print(f"Creating dummy image at: {image_filepath}")
    dummy_image = Image.fromarray(np.random.randint(0, 256, (100, 150, 3), dtype=np.uint8))
    dummy_image.save(image_filepath)
else:
    print(f"Image already exists at: {image_filepath}")

# Create dummy text file if it doesn't exist
if not os.path.exists(text_filepath):
    print(f"Creating dummy text file at: {text_filepath}")
    with open(text_filepath, 'w') as f:
        f.write("This is a sample text file for the Dataloop SDK getting started guide.")
else:
    print(f"Text file already exists at: {text_filepath}")
```

Now we'll upload the local files prepared in the previous step to our Dataloop dataset.
1. Filepaths for the local image and text file are constructed.
2. It checks if these files exist and raises a `FileNotFoundError` if they don't (this is a safeguard, as the previous cell should have created them).
3. The `dataset.items.upload()` method is used to upload each file:
   - `local_path`: Specifies the path to the file on your local system.
   - `remote_path`: Defines the directory structure where the item will be stored within the Dataloop dataset (e.g., '/images', '/docs').
   - `overwrite=True`: If an item with the same name already exists at the remote path, it will be overwritten. This is useful for re-running notebooks.
4. The returned `dl.Item` object for each uploaded item is stored (e.g., `image_item`, `text_item`), and their filenames and IDs are printed.


```python
import os

data_dir = 'data/getting_started_with_sdk'
image_filename = 'sample.jpg' # Ensure this file exists in the 'data' directory
text_filename = 'sample.txt' # Ensure this file exists in the 'data' directory
image_filepath = os.path.join(data_dir, image_filename)
text_filepath = os.path.join(data_dir, text_filename)

# Check if files exist before uploading
if not os.path.exists(image_filepath):
    raise FileNotFoundError(f"Image file not found: {image_filepath}. Please create it.")
if not os.path.exists(text_filepath):
    raise FileNotFoundError(f"Text file not found: {text_filepath}. Please create it.")

# Upload the local files to the dataset
# 'remote_path' specifies the directory structure within the Dataloop dataset
print("Uploading items...")

# Use overwrite=True to avoid errors if the item already exists
image_item: dl.Item = dataset.items.upload(
    local_path=image_filepath,
    remote_path='/images',
    overwrite=True
    )

print(f"Uploaded/Retrieved image item: {image_item.filename}, ID: {image_item.id}")
# image_item.print()

text_item: dl.Item = dataset.items.upload(
    local_path=text_filepath,
    remote_path='/docs',
    overwrite=True
    )

print(f"\nUploaded/Retrieved text item: {text_item.filename}, ID: {text_item.id}")
# text_item.print()
```

### 5.2 Listing Items

You can list items in a dataset, optionally applying filters.

This cell demonstrates how to list items within the dataset.
1. `dataset.items.list()` is called without filters to get a paginated list of all items in the dataset. The `.print()` method displays a summary, and `items_count` gives the total number.
2. To list items from a specific directory (e.g., '/images'), we create a `dl.Filters` object, specifying `resource=dl.FiltersResource.ITEM`.
3. We then use `filters.add()` to specify the filtering condition: `field='dir'` and `values='/images'`.
4. `dataset.items.list(filters=filters)` is then called with these filters.


```python
# List items in the dataset (can use filters)
print("\nListing all items in the dataset:")
all_items_page = dataset.items.list()
all_items_page.print()
print(f"Total items in dataset: {all_items_page.items_count}")

print("\nListing items in the '/images' directory:")
filters = dl.Filters(resource=dl.FiltersResource.ITEM)
filters.add(field='dir', values='/images') # Use add() method
image_items_page = dataset.items.list(filters=filters)
image_items_page.print()
print(f"Items in /images: {image_items_page.items_count}")
```

### 5.3 Retrieving Items

You can retrieve items using either their filepath within your dataset or by using their unique item ID.

This cell shows how to retrieve individual items.
1. It first ensures that `image_item` and `text_item` (from the upload step) exist and gets their IDs and remote filepaths (which include the directory, e.g., `/images/sample.jpg`).
2. To get an item by its path: `dataset.items.get(filepath=image_remote_filepath)` is used. This is wrapped in a try-except block to handle `dl.exceptions.NotFound` if the item doesn't exist at that path.
3. To get an item by its ID: `dataset.items.get(item_id=text_item_id)` is used, also with error handling.


```python
# Make sure we have the item IDs from the upload step
image_item_id = image_item.id
text_item_id = text_item.id
image_remote_filepath = image_item.filename # Get the actual remote path
text_remote_filepath = text_item.filename # Get the actual remote path

# Get an item by its path
try:
    retrieved_image_item = dataset.items.get(filepath=image_remote_filepath)
    print(f"\nRetrieved image item by path: {retrieved_image_item.filename}")
    # retrieved_image_item.print()
except dl.exceptions.NotFound:
    print(f"Error: Could not find item by path: {image_remote_filepath}")

# Get an item by its item id
try:
    retrieved_text_item = dataset.items.get(item_id=text_item_id)
    print(f"\nRetrieved text item by item id: {retrieved_text_item.id}")
    # retrieved_text_item.print()
except dl.exceptions.NotFound:
     print(f"Error: Could not find item by ID: {text_item_id}")
```

### 5.4 Getting and Updating Item Metadata

Each item has system metadata (like dimensions, mimetype) and user metadata (a flexible dictionary for your own information).

This cell demonstrates working with item metadata.
1. It first checks if `retrieved_image_item` (from the previous step) exists.
2. It prints the item's system metadata (`retrieved_image_item.system`) and user metadata (`retrieved_image_item.metadata.get('user', {})`) using `json.dumps` for pretty printing.
3. To update user metadata, it accesses `retrieved_image_item.metadata['user']`. It ensures this key exists and is a dictionary. New key-value pairs are then added, such as `processed_by_script` and a timestamp.
4. The `retrieved_image_item.update()` method is called to save these metadata changes to the Dataloop platform. The updated item object is reassigned to `retrieved_image_item`.
5. The user metadata is printed again to show the changes.


```python
import json

# Make sure we successfully retrieved the image item
if 'retrieved_image_item' in locals():
    # Print existing metadata
    print("\nItem System Metadata:")
    print(json.dumps(retrieved_image_item.system, indent=2))
    print("\nItem User Metadata (before update):")
    print(json.dumps(retrieved_image_item.metadata.get('user', {}), indent=2))

    # Add/Update user metadata
    # The metadata is a dictionary. We usually add custom info under the 'user' key.

    # Ensure 'user' key exists and is a dictionary
    if 'user' not in retrieved_image_item.metadata or not isinstance(retrieved_image_item.metadata['user'], dict):
        retrieved_image_item.metadata['user'] = {}
    retrieved_image_item.metadata['user']['processed_by_script'] = True
    retrieved_image_item.metadata['user']['custom_info'] = 'This is from the SDK notebook'
    retrieved_image_item.metadata['user']['run_timestamp'] = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Push the update to the platform
    retrieved_image_item = retrieved_image_item.update()
    print("\nItem User Metadata (after update):")
    print(json.dumps(retrieved_image_item.metadata.get('user', {}), indent=2))
else:
    print("\nSkipping metadata update because image item retrieval failed.")
```

### 5.5 Downloading Items

You can download items back to your local machine.

This cell shows how to download an item.
1. A `download_dir` ('downloaded_data') is defined, and `os.makedirs` ensures it exists.
2. It checks if `retrieved_image_item` is available.
3. `retrieved_image_item.download(local_path=download_path)` is called. The `local_path` specifies the full path (including filename) where the item will be saved locally. The method returns the actual filepath of the downloaded file.


```python
download_dir = 'downloaded_data'
os.makedirs(download_dir, exist_ok=True)

if 'retrieved_image_item' in locals():
    download_path = os.path.join(download_dir, retrieved_image_item.name)
    filepath = retrieved_image_item.download(local_path=download_path)
    print(f"Item '{retrieved_image_item.name}' downloaded successfully to: {filepath}")
else:
    print("Skipping item download because image item retrieval failed.")
```

## <a id='prompt-items'></a>6. Prompt Items

Prompt Items are a special type used for Large Language Model (LLM) interactions. They are structured JSON files containing prompts (which can include text, references to images/videos, etc.) and potentially responses (stored as annotations).

This cell demonstrates the creation and upload of a `dl.PromptItem`.
1. It checks if `retrieved_image_item` exists, as we'll reference this image in our prompt.
2. A `dl.PromptItem` object is instantiated with a name (which will be its filename, e.g., "my-first-prompt.json").
3. A `dl.Prompt` object is created. Each prompt within a `PromptItem` has a unique `key` and a `role` (e.g., "user", "assistant").
4. Elements are added to this `user_prompt` using `user_prompt.add_element()`:
   - A text element (`dl.PromptType.TEXT`) with the value "Describe this image:".
   - An image element (`dl.PromptType.IMAGE`) where the `value` is `retrieved_image_item.stream`. This `stream` attribute provides a reference to the image data on the Dataloop platform, allowing the prompt item to link to it without duplicating the image data itself.
5. The `user_prompt` is appended to the `prompt_item_obj.prompts` list.
6. Finally, the `prompt_item_obj` is uploaded to the dataset using `dataset.items.upload()`. The `local_path` is the `PromptItem` object itself, `remote_path` specifies a directory in the dataset, and `overwrite=True` is used. The uploaded prompt item's filename and ID are printed.


```python
# Ensure the image item was retrieved before creating the prompt item
if 'retrieved_image_item' in locals():
    # Create a PromptItem object (this doesn't upload yet)
    # The name will be the filename in the platform.
    prompt_item_name = "my-first-prompt.json"
    prompt_item_obj = dl.PromptItem(name=prompt_item_name)

    # Create a prompt (a single turn in a conversation)
    # Use a unique key for each prompt within the item
    user_prompt_key = "user_query_1"
    user_prompt = dl.Prompt(key=user_prompt_key, role="user")  # Default role is 'user'

    # Add elements to the prompt
    user_prompt.add_element(
        mimetype=dl.PromptType.TEXT,
        value="Describe this image:"
    )
    # Reference the image item we uploaded earlier by its data stream
    user_prompt.add_element(
        mimetype=dl.PromptType.IMAGE,
        value=retrieved_image_item.stream,
    )

    # Add the prompt to the PromptItem
    prompt_item_obj.prompts.append(user_prompt)

    # We can upload the prompt item directly
    uploaded_prompt_item: dl.Item = dataset.items.upload(
        local_path=prompt_item_obj,
        remote_path='/prompts',
        overwrite=True
        )
    print(f"Uploaded prompt item: {uploaded_prompt_item.filename} (ID: {uploaded_prompt_item.id})")

    # Open the item in the web interface
    # uploaded_prompt_item.open_in_web() # Uncomment to open
else:
    print("Skipping Prompt Item creation because image item retrieval failed.")
```

## <a id='annotations'></a>7. Annotations

Annotations add semantic meaning to your data items. Dataloop supports various types like bounding boxes, polygons, points, classifications, etc.

**Important:** The labels used here (`'Object1'`, `'CornerPoint'`, `'IndoorScene'`) should exist in the dataset's ontology (defined in Section 4).

This cell demonstrates how to add various types of annotations to the `retrieved_image_item`.
1. It checks if `retrieved_image_item` exists.
2. An `AnnotationBuilder` is obtained from the item: `builder = item_to_annotate.annotations.builder()`.
3. Different annotation types are added using `builder.add()`:
   - `dl.Box`: A bounding box defined by `top`, `left`, `bottom`, `right` coordinates and a `label` (e.g., "Object1"). An optional `object_id` can be used for instance tracking, and `attributes` (like `{'size': 'small'}`) can be added if defined in the ontology for that label.
   - `dl.Point`: A point annotation defined by `x`, `y` coordinates and a `label` (e.g., "CornerPoint").
   - `dl.Classification`: A classification label (e.g., "IndoorScene") applied to the entire item, which has no geometric definition.
4. The annotations built are currently in memory. The commented-out line `# item_to_annotate.annotations.delete(filters=None)` shows how you could clear all existing annotations from an item before uploading new ones (use with caution).
5. `item_to_annotate.annotations.upload(annotations=builder)` uploads the annotations from the builder to the Dataloop platform.
6. After uploading, `item_to_annotate.annotations.list()` retrieves all annotations on the item for verification, and `.print()` displays them.
7. An error handling block catches exceptions during upload, reminding the user to ensure labels exist in the ontology.


```python
# Let's add annotations to the image item we uploaded
if 'retrieved_image_item' in locals():
    item_to_annotate = retrieved_image_item
    print(f"Preparing to annotate item: {item_to_annotate.name}")

    # Use the Annotation Builder for the specific item
    builder = item_to_annotate.annotations.builder()

    # Add a Bounding Box annotation
    # Coordinates are relative to the top-left corner (0,0)
    builder.add(
        annotation_definition=dl.Box(
            top=10,
            left=10,
            bottom=50, # Increased size slightly
            right=60,
            label="Object1" # Ensure this label exists in the ontology
        ),
        object_id=1 # Optional: for tracking instances
    )

    # Add a Point annotation
    builder.add(
        annotation_definition=dl.Point(
            x=75,
            y=75,
            label="CornerPoint" # Ensure this label exists in the ontology
        ),
         object_id=2 # Optional: for tracking instances
    )

    # Add a Classification annotation (no geometry)
    builder.add(
        annotation_definition=dl.Classification(label="IndoorScene") # Ensure this label exists in the ontology
    )

    # The builder now holds these annotations in memory.
    # Before uploading, you might want to clear existing annotations for this item
    # Be cautious with this in real projects!
    # item_to_annotate.annotations.delete(filters=None) # Deletes ALL annotations on the item

    # Upload them to the platform:
    print("Uploading annotations...")
    try:
        uploaded_annotations = item_to_annotate.annotations.upload(annotations=builder)
        print(f"Successfully uploaded {len(uploaded_annotations)} annotations.")

        # You can retrieve the annotations on the item again to verify
        annotations_on_item = item_to_annotate.annotations.list()
        print("\nAnnotations now on the item:")
        annotations_on_item.print() # Prints a summary table

        # Open the item in the web interface
        # item_to_annotate.open_in_web() # Uncomment to open
    except Exception as e:
        print(f"Error uploading annotations: {e}")
        print("Ensure the labels used exist in the dataset's ontology (Section 4).")
else:
    print("Skipping annotation creation because image item retrieval failed.")
```

## <a id='tasks-assignments'></a>8. Tasks & Assignments

Tasks allow you to manage annotation or QA workflows. You assign items to specific users (assignees) to perform work.

This cell demonstrates creating an annotation task.
1. The assignee for the task is set to the current user's email (`dl.info()['user_email']`).
2. It checks if `image_item` (from the upload step) exists, as this item will be assigned to the task.
3. A `due_date` for the task is set to 7 days from the current time using `datetime`.
4. A unique `task_name` is generated including the current timestamp.
5. `dataset.tasks.create()` is called to create the task:
   - `task_name`: The name of the task.
   - `due_date`: The due date as a Unix timestamp.
   - `assignee_ids`: A list of user emails or IDs to assign the task to.
   - `items`: A list of specific `dl.Item` objects to include in the task. Alternatively, `filters` could be used to assign items based on criteria (e.g., all items in a specific directory, as shown in the commented-out example).
6. If task creation is successful, the task's name and ID are printed.
7. Creating a task automatically generates assignments for each assignee. `task.assignments.list()` retrieves these assignments, and `.print()` displays them.


```python
# Make sure we have a valid item and user email
assignee_email = dl.info()['user_email'] # Assign task to yourself
if 'image_item' in locals():
    # Define due date (e.g., 1 week from now)
    due_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)

    # Create an annotation task for the image item
    task_name = f"SDK-GettingStarted-Task-{datetime.datetime.now().strftime('%Y%m%d-%H%M')}"
    print(f"Creating task '{task_name}'...")
    try:
        task: dl.Task = dataset.tasks.create(
            task_name=task_name,
            due_date=due_date.timestamp(),
            assignee_ids=[assignee_email],
            # You can assign specific items or use filters
            items=[image_item], # Assign the specific image item we uploaded
            # Example using filters to assign all items in '/images':
            # filters=dl.Filters(resource=dl.FiltersResource.ITEM, field='dir', values='/images')
        )
        print(f"Task created successfully: {task.name} (ID: {task.id})")

        # Creating a task automatically creates assignments for the assignees
        # You can list assignments for the task
        assignments = task.assignments.list()
        print("\nAssignments created for the task:")
        assignments.print()
    except Exception as e:
        print(f"Error creating task: {e}")
else:
    print("Skipping task creation because image item upload/retrieval failed.")
```

## <a id='conclusion'></a>9. Conclusion and Next Steps

Congratulations! You have successfully completed the getting started tutorial for the Dataloop Python SDK.

### Summary of What You've Accomplished:
- **Authentication and Connection:** Successfully connected to the Dataloop platform and managed authentication
- **Project Management:** Created and managed Projects as the main containers for your work
- **Dataset Operations:** Created Datasets and understood their role in organizing data
- **Ontology Configuration:** Defined the Dataset's Ontology (Labels) for annotation with attributes and properties
- **Item Management:** Uploaded, retrieved, and managed Items (including PromptItems) with metadata operations
- **Annotation Workflows:** Added various types of Annotations (boxes, points, classifications) based on the Ontology
- **Task Management:** Created Tasks and Assignments for collaborative annotation work
- **Data Lifecycle:** Experienced the complete data management lifecycle from upload to annotation

### Next Steps:
This is just the beginning! The SDK offers much more functionality for data management, automation, model integration, and pipeline creation.

#### Immediate Next Steps:
- **Explore Advanced Item Types:** Work with videos, audio files, and other media types
- **Advanced Annotations:** Try different annotation types like polygons, polylines, and segmentation masks
- **Filtering and Queries:** Learn to use advanced filters for finding specific data
- **Batch Operations:** Perform operations on multiple items simultaneously

#### Advanced Workflows:
- **Model Integration:** Connect machine learning models for automated annotation and inference
- **Pipeline Creation:** Build automated workflows that process data through multiple stages
- **Quality Assurance:** Set up QA workflows with consensus mechanisms and review processes
- **Active Learning:** Implement intelligent annotation strategies that prioritize the most valuable data

#### Resources for Continued Learning:
- **[Dataloop Developer Documentation](https://developers.dataloop.ai/):** Comprehensive guides and API reference
- **[Tutorial Collection](https://developers.dataloop.ai/tutorials/):** Step-by-step guides for specific use cases
- **[GitHub Examples](https://github.com/dataloop-ai-apps):** Code samples and real-world implementations

#### Experiment and Build:
- Try building automated pipelines that combine data ingestion, annotation, and model training
- Experiment with different ontology attributes and annotation types for your specific use case
- Integrate Dataloop workflows into your existing ML/AI development processes
- Explore the platform's collaboration features for team-based annotation projects

The Dataloop SDK provides a powerful foundation for building scalable, production-ready AI applications. You're now equipped with the fundamental knowledge to start building sophisticated data and AI workflows!
