# LiDAR Data Processing Tutorial

This notebook provides a comprehensive guide on preparing and managing LiDAR data on the Dataloop platform using its Python SDK. LiDAR (Light Detection and Ranging) data processing is essential for autonomous vehicles, robotics, and 3D mapping applications.

You'll learn how to structure LiDAR data, upload it to Dataloop, construct LiDAR video items, and add 3D annotations for comprehensive spatial analysis.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **LiDAR Data:** Access to LiDAR data files including PCD files, camera images, and calibration data.
* **Local Data Structure:** Your LiDAR data should be organized as described in this tutorial.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Environment Setup](#environment-setup)
3. [LiDAR Data Preparation](#data-preparation)
4. [Construct LiDAR Video Item](#construct-lidar-video)
5. [Upload Annotations](#upload-annotations)
6. [Conclusion and Next Steps](#conclusion)

For more detailed information, refer to the official Dataloop documentation:
- [LiDAR Data Setup](https://docs.dataloop.ai/docs/lidar-data-setup)
- [LiDAR Video Annotations](https://developers.dataloop.ai/tutorials/annotations/lidar/chapter)

## <a id='dependencies-setup'></a>1. Dependencies & Setup

First, let's ensure all required Python packages are installed. The cell below will install `dtlpy` for Dataloop SDK interaction and `dtlpylidar` for LiDAR-specific functionalities. It is recommended to run this to ensure you have the latest compatible versions.


```python
!pip install dtlpy git+https://github.com/dataloop-ai-apps/dtlpy-lidar.git --upgrade --quiet
```

## <a id='environment-setup'></a>2. Environment Setup

### Import Required Libraries

With the dependencies installed, we will now import the necessary libraries for this tutorial.


```python
import dtlpy as dl
from dtlpylidar.parsers.base_parser import LidarFileMappingParser
```

### Connect to Dataloop Platform

To begin, we need to connect to the Dataloop platform. If you're not already logged in, running the cell below will prompt you to do so. We will then create a new project or retrieve an existing one to work in.

> **Action Required:** In the cell below, replace `"your-lidar-project-name"` with your Dataloop project name. If a project with this name already exists, it will be retrieved; otherwise, a new one will be created.


```python
if dl.token_expired():
    dl.login()

PROJECT_NAME = "your-lidar-project-name"
# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=PROJECT_NAME)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=PROJECT_NAME)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")
```

## <a id='data-preparation'></a>3. LiDAR Data Preparation

To construct a LiDAR video item, your dataset must contain three key components: PCD files for 3D scenes, camera images for 2D views, and a `mapping.json` file for sensor calibration. This section explains how to structure these files locally before uploading them to Dataloop.

### 3.1 Local File Structure

Before uploading to the Dataloop platform, your LiDAR data must be arranged in a specific local directory structure. This ensures that all components (point clouds, images) are correctly associated.

#### Required Directory Structure:

1. **`lidar` folder:** Contains all PCD files, named numerically in sequence (e.g., `0.pcd`, `1.pcd`, ...).

2. **`frames` folder:** Contains subfolders for each frame's camera images.
   - Subfolders must be named numerically to match the PCD files (e.g., `0`, `1`, ...).
   - Image files within each subfolder must be named sequentially (e.g., `0.jpg`, `1.jpg`, ...).

3. **`mapping.json` file:** This file, located at the root of your data directory, contains the calibration data that links the 3D point clouds to the 2D images.

### 3.2 Mapping.json Schema

The `mapping.json` file must follow a specific schema. Below is a template demonstrating the required structure, including paths, timestamps, and camera calibration parameters (intrinsics and extrinsics).

```json
{
    "frames": {
        "0": {
            "path": "lidar/0.pcd", // Relative path from the mapping.json file
            "timestamp": 1234567890,
            "position": { // LiDAR sensor location (used as the center of the world)
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            },
            "heading": { // LiDAR sensor rotation (Quaternion)
                "x": 0.0,
                "y": 0.0,
                "z": 0.0,
                "w": 1.0
            },
            "images": { // if no images are provided, add an empty dict
                "0": {
                    "image_path": "frames/0/0.jpg", // Relative path from the mapping.json file
                    "timestamp": 1234567890,
                    "intrinsics": { // camera intrinsic parameters
                        "fx": 525.0, // Focal length in pixels
                        "fy": 525.0,
                        "cx": 319.5, // Optical center (the principal point), in pixels
                        "cy": 239.5
                    },
                    "extrinsics": { // camera extrinsic parameters
                        "translation": { // camera location in world coordinates (in relation to the lidar sensor)
                            "x": 0.0,
                            "y": 0.0,
                            "z": 0.0
                        },
                        "rotation": { // rotation of the camera (Quaternion)
                            "w": 1.0,
                            "x": 0.0,
                            "y": 0.0,
                            "z": 0.0
                        }
                    },
                    "distortion": { // distortion parameters
                        "k1": 0.0,
                        "k2": 0.0,
                        "p1": 0.0,
                        "p2": 0.0,
                        "k3": 0.0,
                        "k4": 0.0
                    }
                }
            }
        }
    }
}
```

### 3.3 Upload Data to Dataloop

You can use your own data structured as described above, or use sample data from [OSDaR23](https://data.fid-move.de/dataset/osdar23) for this tutorial.

> **Action Required:** In the cell below, update `DATASET_NAME` with your desired dataset name and `DATA_PATH` with the local path to your data directory.


```python
DATASET_NAME = "My-LiDAR-Dataset"
# Check if the dataset exists within the project
# if not, create it. Dataloop automatically creates a default Recipe and Ontology.
try:
    dataset = project.datasets.get(dataset_name=DATASET_NAME)
    print(f"Successfully retrieved dataset: '{dataset.name}' (ID: {dataset.id})")
except dl.exceptions.NotFound:
    dataset = project.datasets.create(dataset_name=DATASET_NAME)
    print(f"Successfully created dataset: '{dataset.name}' (ID: {dataset.id}) in project '{project.name}'.")
```

### 3.4 Upload Items to Dataset

Now that we created or retrieved the dataset, we can upload items to it.


```python
# Upload the data to the dataset
DATA_PATH = "./data/*"
dataset.items.upload(local_path=DATA_PATH)

print(f"Data uploaded successfully to dataset '{dataset.name}'")
```

### 3.5 View Dataset in Platform

We can take a look at the items in the platform using the following command:


```python
# Open the dataset in the Dataloop web interface
dataset.open_in_web()
```

## <a id='construct-lidar-video'></a>4. Construct LiDAR Video Item

After uploading your raw data files (`.pcd`, `.jpg`, `mapping.json`), we use the Dataloop LiDAR SDK to create a single, composite LiDAR video item. The `LidarFileMappingParser` reads the `mapping.json` file and generates a `frames.json` item, which represents the synchronized 3D video sequence in the Dataloop studio.

### 4.1 Parse Mapping File

Use the LiDAR parser to process the mapping file and create the LiDAR video item.


```python
# Get the mapping item using filters
filters = dl.Filters(field=dl.FiltersKnownFields.NAME, values="mapping.json")
mapping_item = dataset.items.get_all_items(filters=filters)[0]
frames_item = LidarFileMappingParser().parse_data(mapping_item=mapping_item)
print(f"LiDAR Video File: ItemID: {frames_item.id}, ItemName: {frames_item.name}")
```

## <a id='upload-annotations'></a>5. Upload Annotations

With the `frames.json` video item created, you can now add annotations. The process is similar to annotating standard videos in Dataloop, but with support for 3D annotation types like cuboids. First, we need to retrieve the `frames.json` item we just created.

### 5.1 Retrieve Frames Item

Get the created frames item for annotation.


```python
# Get the created frames item using filters
filters = dl.Filters(field=dl.FiltersKnownFields.NAME, values="frames.json")
frames_item = dataset.items.get_all_items(filters=filters)[0]
print(f"Retrieved frames item: {frames_item.name} (ID: {frames_item.id})")
```

### 5.2 Define and Upload a 3D Cuboid

#### Define the Annotation

To create a 3D cuboid annotation, we define its geometric properties and any additional metadata. The key parameters are:

- **Position:** The 3D coordinates of the cuboid's center (x, y, z).
- **Rotation:** Euler angles for the cuboid's orientation (roll, pitch, yaw).
- **Scale:** The dimensions of the cuboid (width, height, depth).

The code below defines a `dl.Cube3d` annotation for a "person".


```python
# Define Your 3D Annotation Parameters
label = "person"
position = [
    73.9,  # x coordinate
    -5.9,  # y coordinate
    0.79   # z coordinate
]
rotation = [
    0.0,   # roll
    0.0,   # pitch
    0.0    # yaw
]
scale = [
    1.2,   # width
    0.8,   # height
    1.8    # depth
]

# Add Some Extra Details
attributes = {"age": "adult"}
description = "An adult person standing on the station"

# Create the 3D Cuboid Annotation
annotation_definition = dl.Cube3d(
    label=label,
    position=position,
    scale=scale,
    rotation=rotation,
    attributes=attributes,
    description=description
)

print(f"Created 3D cuboid annotation for label '{label}'")
print(f"Position: {position}")
print(f"Scale: {scale}")
print(f"Rotation: {rotation}")
```

#### Upload the Annotation

Now that the `dl.Cube3d` object is defined, we use an annotation `builder` to add it to the `frames.json` item. We specify the frame range (`frame_num` to `end_frame_num`) where the annotation should appear and then upload it to the platform.


```python
# Create annotation builder for the frames item
builder = frames_item.annotations.builder()

# Define annotation parameters
frame_num = 0
end_frame_num = 1
object_id = "0"
metadata = {"user": {"isDistracted": True}}

# Add the annotation to the builder
builder.add(
    annotation_definition=annotation_definition,
    frame_num=frame_num,
    end_frame_num=end_frame_num,
    object_id=object_id,
    metadata=metadata
)

# Upload the annotations
builder.upload()
print(f"Successfully uploaded 3D cuboid annotation to frames {frame_num}-{end_frame_num}")
```

### 5.3 View in Dataloop Studio

Once the annotation is uploaded, you can open the LiDAR video item in the Dataloop platform to view it in the LiDAR Studio. The following command will open the item directly in your web browser.


```python
# Open the LiDAR video item in the Dataloop LiDAR Studio
frames_item.open_in_web()
```

## <a id='conclusion'></a>6. Conclusion and Next Steps

Congratulations! You have successfully walked through the entire process of preparing a LiDAR dataset for the Dataloop platform.

### Summary of What You've Accomplished:
- Set up your Dataloop environment and project for LiDAR data processing
- Learned the required file structure for LiDAR data (PCDs, images, and mapping file)
- Understood the `mapping.json` schema for sensor calibration and synchronization
- Uploaded and structured raw LiDAR data files to Dataloop
- Constructed a composite LiDAR video item using the Dataloop LiDAR SDK
- Created and uploaded 3D cuboid annotations to the video item
- Visualized the results in the Dataloop LiDAR Studio

### Next Steps:
From here, you can explore more advanced functionalities:
- **Advanced Annotations:** Experiment with different 3D annotation types (polylines, polygons, points)
- **Custom LiDAR Parser:** Try constructing a LiDAR video item using a [Custom LiDAR Parser](https://developers.dataloop.ai/tutorials/data_management/items_and_annotations/other_data_types/lidar/chapter#using-custom-lidar-parser) for data that doesn't fit the standard structure
- **Automated Pipelines:** Create automated pipelines for LiDAR data processing and annotation workflows
- **Machine Learning Integration:** Integrate LiDAR workflows with machine learning models for autonomous systems and 3D object detection
- **Multi-Modal Analysis:** Combine LiDAR data with other sensor modalities for comprehensive scene understanding
- **Quality Assurance:** Set up QA workflows for 3D annotation validation and consensus

For more advanced LiDAR processing capabilities, explore the full [Dataloop LiDAR SDK documentation](https://github.com/dataloop-ai-apps/dtlpy-lidar) and the [LiDAR tutorials](https://developers.dataloop.ai/tutorials/data_management/items_and_annotations/other_data_types/lidar/chapter) in the Dataloop developer documentation.
