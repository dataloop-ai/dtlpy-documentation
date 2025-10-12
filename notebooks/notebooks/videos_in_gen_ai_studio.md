# Videos in Dataloop GenAI Evaluation Studio Tutorial

This notebook guides you through the process of setting up a Dataloop project and dataset for evaluating videos using the Dataloop GenAI Evaluation Studio. The GenAI Evaluation Studio provides a powerful interface for creating custom evaluation workflows, particularly useful for assessing video content quality, relevance, and other subjective metrics.

You'll learn how to create evaluation layouts, upload videos, and set up comprehensive evaluation workflows that can be used by annotators to assess video content systematically.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **Project Access:** Ability to create projects and manage datasets.
* **Local Files:** Access to the required configuration and video files as described below.

### Required Local Files:
* `data/layout.json`: A JSON file defining the structure and questions for the evaluation interface.
* `data/item_schema.json`: A template JSON file that will link your video to the evaluation layout.
* `data/videos/`: A directory containing the video files you want to upload and evaluate.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Dataloop Environment Setup](#environment-setup)
3. [Dataset Management](#dataset-management)
4. [Understanding and Uploading the Evaluation Layout](#evaluation-layout)
5. [Understanding the Evaluation Item Schema](#item-schema)
6. [Processing and Uploading Videos for Evaluation](#video-upload)
7. [Conclusion and Next Steps](#conclusion)

## <a id='dependencies-setup'></a>1. Dependencies & Setup

First, let's install all required packages and import necessary libraries.


```python
!pip install dtlpy --upgrade --quiet
```

### Import Required Libraries

Next, let's import necessary libraries and define some key configuration variables.


```python
import dtlpy as dl
import os
import tempfile

# Paths to your local data files
LAYOUT_JSON_PATH = "data/videos_in_gen_ai_studio/layout.json"
ITEM_SCHEMA_JSON_PATH = "data/videos_in_gen_ai_studio/item_schema.json"
VIDEOS_DIR_PATH = "data/videos_in_gen_ai_studio/videos"

print(f"Dataloop SDK Version: {dl.__version__}")
print(f"Configuration paths set:")
print(f"  Layout JSON: {LAYOUT_JSON_PATH}")
print(f"  Item Schema: {ITEM_SCHEMA_JSON_PATH}")
print(f"  Videos Directory: {VIDEOS_DIR_PATH}")
```

## <a id='environment-setup'></a>2. Dataloop Environment Setup

This section handles connecting to the Dataloop platform. It will:
1. Check if your login token is expired and prompt for login if necessary.
2. Create or retrieve the specified Dataloop project.


```python
# Check login status and connect if needed
if dl.token_expired():
    dl.login()
    print("Successfully logged into Dataloop")
else:
    print(f"Already connected to Dataloop as {dl.info()['user_email']}")

# Define a unique name for your project or change it to your own project name
user_email = dl.info()['user_email']
user_prefix = user_email.split('@')[0].replace('.', '').replace('-', '') # Simple prefix from email
project_name = f'{user_prefix}-videos-in-gen-ai-studio'

# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=project_name)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=project_name)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")
```

## <a id='dataset-management'></a>3. Dataset Management

Here, we'll either create a new dataset or retrieve an existing one within your Dataloop project. This dataset will store your videos and their corresponding evaluation items.


```python
# Define a unique name for your dataset within the project
dataset_name = 'videos-in-gen-ai-studio-dataset'

# Check if the dataset exists within the project
# if not, create it. Dataloop automatically creates a default Recipe and Ontology.
try:
    dataset = project.datasets.get(dataset_name=dataset_name)
    print(f"Successfully retrieved dataset: '{dataset.name}' (ID: {dataset.id})")
except dl.exceptions.NotFound:
    dataset = project.datasets.create(dataset_name=dataset_name)
    print(f"Successfully created dataset: '{dataset.name}' (ID: {dataset.id}) in project '{project.name}'.")

print(f"Dataset ready for video evaluation setup")
```

## <a id='evaluation-layout'></a>4. Understanding and Uploading the Evaluation Layout

The Evaluation Studio in Dataloop uses a JSON file (often called `layout.json`) to define the user interface for an evaluation task. This file specifies the questions, input types (e.g., radio buttons, sliders), and any conditional logic between them. This is the same JSON built when using the Multimodal Recipe in the Dataloop platform's UI.

The `layout.json` file is uploaded to a special hidden dataset in your project called the 'binaries dataset'. The system then uses the ID of the target dataset (where your videos will reside) to create a unique name for this layout, ensuring it's specifically tied to your video evaluation task.

### 4.1 `layout.json` Structure

The `layout.json` file is an array of objects, where each object represents a page or a main section of your evaluation form. For this example, we typically use a single object in the array for a one-page form.

```json
[
  {
    "title": "Please evaluate the following video", // Title of the evaluation form/page
    "components": [ // Array of UI components (questions, inputs)
      // ... component definitions go here ...
    ]
  }
]
```

### 4.2 Available Component Types and Properties

These are the building blocks for your questions within the `components` array of your `layout.json`.

#### Video Display (`type: "video"`)
* `key`: Unique identifier (string). This key will be used in `item_schema.json` to link to the video stream.
  *Example: `"key": "video_stream"`*

#### Radio Group (`type: "radio"`)
*Note: Single-select options.*
* `key`: Unique identifier (string).
* `title`: Question text (string).
* `required`: Boolean (true/false) - whether an answer is mandatory.
* `options`: Array of `{label, value}` objects. `label` is displayed to the user, `value` is stored.
  *Example: `{"label": "Yes", "value": "yes"}`*
* `hierarchy`: Conditional logic definition (object, optional).

#### Slider (`type: "slider"`)
* `key`: Unique identifier (string).
* `title`: Question text (string).
* `required`: Boolean (true/false).
* `min`: Minimum value (number).
* `max`: Maximum value (number).
* `step`: Step increment (number).
* `default`: Default value (number, optional).
* `hierarchy`: Conditional logic definition (object, optional).

#### Select (`type: "select"`)
*Note: Renders as a dropdown, typically for single-select from a longer list.*
* `key`: Unique identifier (string).
* `title`: Question text (string).
* `required`: Boolean (true/false).
* `options`: Array of `{label, value}` objects.
* `hierarchy`: Conditional logic definition (object, optional).

#### Checkbox (`type: "checkbox"`)
*Note: Multi-select options.*
* `key`: Unique identifier (string).
* `title`: Question text (string).
* `required`: Boolean (true/false) - if true, at least one option must be selected.
* `options`: Array of `{label, value}` objects.
* `hierarchy`: Conditional logic definition (object, optional).

#### Text Input (`type: "text"`)
* `key`: Unique identifier (string).
* `title`: Question text (string).
* `required`: Boolean (true/false).
* `placeholder`: Hint text for input (string, optional).
* `hierarchy`: Conditional logic definition (object, optional).

### 4.3 Conditional Logic (Hierarchy)

You can show or hide components based on answers to previous questions using the `hierarchy` property. This uses Dataloop Query Language (DQL) syntax.

#### Basic Condition Structure:
Checks if the field specified by `fieldKey` equals `value`.

```json
"hierarchy": {
  "condition": {
    "fieldKey": "value" // Implicit '$eq' (equals) check
  }
}
// Equivalent explicit structure:
"hierarchy": {
  "condition": {
    "fieldKey": { "$eq": "value" }
  }
}
```

#### Comparison Operators:
* `$eq`: Equal to (e.g., `"radio_1": { "$eq": "yes" }`)
* `$ne`: Not equal to
* `$gt`: Greater than
* `$gte`: Greater than or equal to
* `$lt`: Less than
* `$lte`: Less than or equal to
* `$in`: Value is in array (useful for checking if a specific option in a `checkbox` is chosen)
* `$exists`: Field exists and is not null/empty

#### Logical Operators:
* `$and`: All nested conditions must be true. Takes an array of condition objects.
* `$or`: At least one nested condition must be true. Takes an array of condition objects.

### 4.4 Upload Evaluation Layout

Now let's create a function to upload the evaluation layout and then execute it.


```python
def upload_evaluation_layout(project: dl.Project, dataset_id: str, layout_json_path: str) -> str:
    """
    Uploads the evaluation layout JSON to the project's binaries dataset.
    The layout file will be named based on the target dataset's ID to ensure uniqueness
    and proper association.

    Args:
        project: The Dataloop Project object.
        dataset_id: The ID of the dataset where the videos and evaluation items will be stored.
                       This ID is used to name the layout file.
        layout_json_path: Local path to the layout.json file.

    Returns:
        The name of the uploaded layout file (used later in item metadata).
    """
    if not os.path.exists(layout_json_path):
        print(f"Error: Layout JSON file not found at {layout_json_path}")
        raise FileNotFoundError(f"Layout JSON file not found at {layout_json_path}")

    binaries_dataset: dl.Dataset = project.datasets._get_binaries_dataset() # Internal dataset for configs
    layout_file_name_prefix = f"dataset_{dataset_id}_layout"
    
    print(f"Uploading layout JSON '{layout_json_path}' to binaries dataset...")
    print(f"Layout will be stored with prefix: {layout_file_name_prefix}")

    # The remote_path specifies a directory-like structure within the binaries dataset.
    # The remote_name is the actual filename.
    uploaded_layout_item = binaries_dataset.items.upload(
        local_path=layout_json_path,
        remote_path=f"/.dataloop/evaluation-studio-layouts/{layout_file_name_prefix}/",
        remote_name=f"{layout_file_name_prefix}.json",
        overwrite=True, # Overwrite if a layout with the same name already exists
    )
    print(f"Successfully uploaded layout JSON. Item ID: {uploaded_layout_item.id}, Name: {uploaded_layout_item.name}")
    return layout_file_name_prefix # This is the 'layoutName' we need later
```


```python
# --- Run Layout Upload ---
layout_file_name = upload_evaluation_layout(
    project=project, 
    dataset_id=dataset.id, 
    layout_json_path=LAYOUT_JSON_PATH
)

print(f"\nLayout uploaded successfully with name: {layout_file_name}")
```

## <a id='item-schema'></a>5. Understanding the Evaluation Item Schema

For each video you upload, you'll also upload a corresponding JSON item. This JSON item tells the Dataloop Evaluation Studio:
1. Which video to display (via its stream URL).
2. Which evaluation layout to use.

We use a template file (`item_schema.json`) for this. The key part of this template is a placeholder for the video stream URL:

### Example `data/item_schema.json` content:
```json
{
    "video_stream": "{{video_stream}}"
}
```

* `"video_stream"`: This key **must match** the `key` of the `"type": "video"` component defined in your `layout.json`.
* `"{{video_stream}}"`: This is a placeholder that our script will replace with the actual Dataloop stream URL of the uploaded video.

When this JSON item is uploaded to Dataloop, we also add special metadata to it:
```python
item_metadata={
    "system": {
        "evaluation": {"layoutName": layout_file_name}, # Links to the uploaded layout.json
        "shebang": {"dltype": "evaluation-studio"},     # Tells Dataloop to open this with Evaluation Studio
    },
}
```
This metadata ensures that when an annotator opens this JSON item in Dataloop, it loads the correct video within the defined evaluation interface.

## <a id='video-upload'></a>6. Processing and Uploading Videos for Evaluation

This is the main part where we iterate through your video files. For each video, we will:
1. Upload the video file to your Dataloop dataset.
2. Create a temporary JSON file based on `item_schema.json`, injecting the uploaded video's stream URL.
3. Upload this new JSON file (the "Evaluation Item" or "Gen AI Studio Item") to the same dataset, linking it to the video and the evaluation layout via metadata.

### 6.1 Helper Functions

Let's define the helper functions for uploading videos and creating evaluation items.


```python
def upload_video_to_dataloop(dataset_obj: dl.Dataset, local_video_path: str) -> dl.Item:
    """
    Uploads a single video file to the specified Dataloop dataset.

    Args:
        dataset_obj: The Dataloop Dataset object to upload to.
        local_video_path: The local path to the video file.

    Returns:
        The Dataloop Item object for the uploaded video.
    """
    video_filename = os.path.basename(local_video_path)
    print(f"Uploading video: {video_filename}...")
    item = dataset_obj.items.upload(local_path=local_video_path, remote_path="/videos/")
    print(f"✓ Successfully uploaded video: {item.name} (ID: {item.id}, Stream URL: {item.stream})")
    return item

def create_and_upload_evaluation_item(
    dataset_obj: dl.Dataset,
    video_item: dl.Item, 
    video_file_basename: str,
    item_schema_template_path: str, 
    evaluation_layout_name: str
) -> dl.Item:
    """
    Creates and uploads the JSON item for the Evaluation Studio, linking it to the video and layout.

    Args:
        dataset_obj: The Dataloop Dataset object.
        video_item: The Dataloop Item object of the uploaded video.
        video_file_basename: The original base name of the video file (without extension), used for naming the JSON item.
        item_schema_template_path: Path to the item_schema.json template.
        evaluation_layout_name: The name of the layout file uploaded earlier (e.g., 'dataset_XYZ_layout').

    Returns:
        The Dataloop Item object for the uploaded JSON evaluation item.
    """
    print(f"Creating and uploading Evaluation Studio Item for {video_file_basename}...")
    
    if not os.path.exists(item_schema_template_path):
        print(f"Error: Item schema template not found at {item_schema_template_path}")
        raise FileNotFoundError(f"Item schema template not found at {item_schema_template_path}")
            
    with open(item_schema_template_path, "r") as f_schema, \
    tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as temp_json_file:
        
            schema_content_str = f_schema.read()
            # Replace the placeholder with the actual video stream URL from the uploaded video item
            # The item.stream attribute provides the web-accessible URL for the video.
            populated_schema_str = schema_content_str.replace('{{video_stream}}', video_item.stream)
            
            temp_json_file.write(populated_schema_str)
            temp_json_file_path = temp_json_file.name
            temp_json_file.flush()
            os.fsync(temp_json_file.fileno())

    try:
        # Upload the populated JSON file as a new item
        # This item will be what annotators open in the Evaluation Studio.
        genai_item = dataset_obj.items.upload(
            local_path=temp_json_file_path,
            remote_name=f"{video_file_basename}.json", # Name the JSON item after the video
            item_metadata={
                "system": {
                    "evaluation": {"layoutName": evaluation_layout_name}, # Links to the layout
                    "shebang": {"dltype": "evaluation-studio"},        # Specifies to open with Eval Studio
                },
            },
        )
        print(f"✓ Successfully uploaded Evaluation Studio Item: {genai_item.name} (ID: {genai_item.id})")
        return genai_item
    finally:
        os.remove(temp_json_file_path)
        print(f"Temporary file {temp_json_file_path} removed.")
```

### 6.2 Process and Upload Videos

Now let's process all videos in the specified directory.


```python
# --- Main Loop: Process and Upload Videos ---
print(f"\nStarting video processing from directory: {VIDEOS_DIR_PATH}")
if not os.path.isdir(VIDEOS_DIR_PATH):
    print(f"Error: Videos directory not found at {VIDEOS_DIR_PATH}. Please create it and add videos.")
else:
    video_files_processed = 0
    for video_filename_with_ext in os.listdir(VIDEOS_DIR_PATH):
        full_video_path = os.path.join(VIDEOS_DIR_PATH, video_filename_with_ext)
        
        # Process only files, skip directories if any
        if os.path.isfile(full_video_path):
            video_file_basename_no_ext = os.path.splitext(video_filename_with_ext)[0]
            print(f"\n--- Processing video: {video_filename_with_ext} ---")
            try:
                # 1. Upload the video file
                uploaded_video_item = upload_video_to_dataloop(
                    dataset_obj=dataset, 
                    local_video_path=full_video_path
                )
                
                # 2. Create and upload the corresponding Evaluation Studio JSON item
                evaluation_json_item = create_and_upload_evaluation_item(
                    dataset_obj=dataset,
                    video_item=uploaded_video_item,
                    video_file_basename=video_file_basename_no_ext,
                    item_schema_template_path=ITEM_SCHEMA_JSON_PATH,
                    evaluation_layout_name=layout_file_name # From step 4
                )
                video_files_processed += 1
                
            except Exception as e:
                print(f"✗ ERROR processing {video_filename_with_ext}: {str(e)}")
                continue 
        else:
            print(f"Skipping non-file entry: {video_filename_with_ext}")
            
    print(f"\n--- Finished processing. Total videos processed: {video_files_processed} ---")
```

## <a id='conclusion'></a>7. Conclusion and Next Steps

You have now successfully set up your Dataloop project for video evaluation!

### Summary of What You've Accomplished:
- Connected to Dataloop and configured your project for video evaluation
- Created or retrieved a dataset for storing videos and evaluation items
- Understood the structure and components of evaluation layouts (`layout.json`)
- Uploaded an evaluation layout that defines the UI for your annotators
- Learned about the evaluation item schema and its role in linking videos to layouts
- Processed and uploaded videos along with their corresponding evaluation JSON items
- Set up the complete workflow for video evaluation in the GenAI Evaluation Studio

### What Happened:
1. Connected to Dataloop and your specified project.
2. Created or retrieved a dataset for video evaluation.
3. Uploaded an evaluation layout (`layout.json`) that defines the UI for your annotators.
4. For each video in your `data/videos` directory:
   - The video file was uploaded to the dataset.
   - A corresponding JSON item was created and uploaded. This item links the video to the evaluation layout and tells Dataloop to open it with the Evaluation Studio.

### Next Steps:
- **Navigate to your dataset in the Dataloop platform:** You should see the uploaded JSON items (e.g., `myvideo.json`). The video files themselves will be in a `/videos/` folder within the dataset's item browser.
- **Open one of the JSON items:** Right click on the item → Open With and select "GenAI Evaluation Studio". It should open in the GenAI Evaluation Studio, displaying the video alongside the questions defined in your `layout.json`.
- **Create annotation tasks:** You can now assign these evaluation items to annotators by creating tasks in Dataloop.
- **Customize evaluation layouts:** Experiment with different component types and conditional logic to create more sophisticated evaluation workflows.
- **Analyze evaluation results:** Use Dataloop's analytics and reporting features to analyze the evaluation responses and derive insights from your video assessments.
- **Scale your workflow:** Integrate this process into larger content evaluation pipelines for systematic video quality assessment.


```python
# Open the dataset in the web interface to see your uploaded videos and evaluation items
dataset.open_in_web()
```
