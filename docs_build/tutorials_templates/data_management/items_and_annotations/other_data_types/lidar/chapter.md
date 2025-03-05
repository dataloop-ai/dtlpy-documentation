# LiDAR Data Setup

## Using Dataloop Mapping

### Files and Calibration Data Setup

To prepare a dataset for LiDAR video creation, please ensure that you complete the prerequisite steps outlined in the [LiDAR Data Setup](https://docs.dataloop.ai/docs/lidar-data-setup) documentation.

### Create the LiDAR Video File

Once all files are ready, to create the LiDAR video file (of all the PCD files stitched together), do as follows:

1. Install [Dataloop LiDAR SDK](https://github.com/dataloop-ai-apps/dtlpy-lidar) to your local python environment, using the command:

   ```bash
   pip install git+https://github.com/dataloop-ai-apps/dtlpy-lidar.git
   ```

2. Use the following code snippet to create the LiDAR video file:

   ```python
   import dtlpy as dl
   from dtlpylidar.parsers.base_parser import LidarFileMappingParser

   dataset = dl.datasets.get(dataset_id="<dataset id>")
   mapping_item = dataset.items.get(item_id="<mapping.json item id>")
   frames_item = LidarFileMappingParser().parse_data(mapping_item=mapping_item)
   frames_item.open_in_web()
   ```

3. The output item will be a `frame.json` file (the LiDAR video file) with all the PCD files stitched together,
   where each frame contains the following information:

   - **PCD file:** The point cloud data of the 3D scene for the given frame.
   - **JPEG/PNG files:** The 2D images of the available camera sources for the given frame.
   - **Calibration data:** The calibration data of the LiDAR sensor and the camera sources for the given frame (as was specified in the `mapping.json` file).

4. (Optional) Once all files are ready, contact Dataloop to execute the Ground Detection - on each provided .pcd file to enable the Ground Detection Toggle on the LiDAR Studio.

### Upload Framed Annotations

See how to upload different types of framed annotations to the LiDAR video item in the [Annotations](https://developers.dataloop.ai/tutorials/annotations/) page, under **LiDAR Annotations** section.

**Notice:** Make sure that the `frames.json` file includes the `fps` key in its metadata. \
Set it to a default value of `1` if it is not already present.

```json
{
  "system": {
    "originalname": "frames.json",
    "size": 32712,
    "encoding": "7bit",
    "shebang": {
      "dltype": "PCDFrames"
    },
    "taskStatusLog": [],
    "mimetype": "application/json",
    "isBinary": false,
    "refs": []
  },
  "fps": 1
}
```

## Using Custom LiDAR Parser

### Brief explanation

This section provides an advanced guide about how to set up a LiDAR scene dataset and create a LiDAR video file on the
Dataloop platform for any directory structure of a LiDAR scene, as long as the files are in the following formats:

1. **3D Scene Files** - Point Cloud Data files in `.pcd` **ASCII** format.
2. **2D Camera Views Files** - Image files in JPEG/PNG formats.
3. **Calibration Data Files** - Any file format that contains the required [Camera Calibration Parameters](https://www.mathworks.com/help/vision/ug/camera-calibration.html#:~:text=the%20intrinsics%20parameters.-,Camera%20Calibration%20Parameters,-The%20calibration%20algorithm).

In this guide we will show an example of modifying the [CustomBaseParser](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py)
to support the [PandaSet](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset) dataset. \
However, this parser can be extended to support custom LiDAR scenes by modifying the available `Customizable` methods as needed.

### Step 1: Files Setup

Create a dataset on the Dataloop platform and upload the following required LiDAR files to the dataset:

1. **3D Scene Files** - Point Cloud Data files used for generating the 3D scenes.
2. **2D Camera Views Files** - Usually showing the angle and viewport of the cameras that captured the main scene.
3. **Calibration Data Files** Any type of files that contains all required information to align the point cloud data with the camera images.
   For a detailed explanation about the parameters required in the mapping.json file, please refer to the Camera Calibration Parameters.

#### Example of arranging the files with PandaSet

To prepare the PandaSet dataset, do as follows:

1. Go to [PandaSet Kaggle Page](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset).
2. Download the dataset and extract the files from the `.zip` file.
3. Open a project on the Dataloop platform and create a new dataset for it.
4. Select a scene folder from the extracted files in the `.zip` file keep the following folders:
   - `lidar`
   - `camera`
5. **Normalize the data**, by updating the folders files through the following steps:
   1. Locate the `poses.json` file in the `lidar` folder and open it.
   2. Convert the PCD files from `.ply` to `.pcd` format, and apply the transformations from the `poses.json` file to the PCD files.
6. Upload the folders with the updated files to the dataset on the Dataloop platform.

**Important Notes:**

- **File Format Assumptions:** \
  The converter requires that the remote dataset will already have the PandaSet 3D scene files in `.pkl` format to converted into `.pcd` format. \
  For more details on why `.pcd` files are preferred, please refer to the [PCD file format documentation](https://pointclouds.org/documentation/tutorials/pcd_file_format.html).
- **Conversion Scripts:** \
  You can find helpful scripts for converting `.pkl` files to `.pcd` in the `dtlpylidar/utilities/converters` directory, on [Dataloop LiDAR SDK](https://github.com/dataloop-ai-apps/dtlpy-lidar),
  or you can use the provided example in the section (Upload PandaSet to Dataloop) for uploading the PandaSet dataset with the updated files.

#### Dataset structure explanation

The PandaSet scene folder structure:

- `lidar`:
  - Point cloud files in `.pkl` format for each frame (must be converted to `.pcd` format).
  - `poses.json` – contains the poses for each frame.
  - `timestamps.json` (optional) – includes timestamps for the frames.
- `camera`:
  - Per-camera sub-folder:
    - Images for each frame.
    - `intrinsics.json` – camera intrinsic parameters.
    - `poses.json` – camera poses.
    - `timestamps.json` (optional) – includes timestamps for the frames.

#### Json files structure

##### - `poses.json` file structure (similar for lidar and cameras)

Each object refer to a different frame.

```python
[
    {"position": {"x": 0.0, "y": 0.0, "z": 0.0}, "heading": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0}},  # PCD frame 0 extrinsics / Camera N frame 0 extrinsics
    {"position": {"x": 0.5, "y": 0.5, "z": 0.0}, "heading": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0}}
]
```

##### - `intrinsics.json` file structure (for cameras)

Each camera has static intrinsics calibrations across all its images.

```python
{"fx": 933.4667, "fy": 934.6754, "cx": 896.4692, "cy": 507.3557}
```

##### - `timestamps.json` file structure (similar for lidar and cameras)

Each object refer to a different frame.

```python
[
    1557539924.49981,  # PCD frame 0 timestamp / Camera N frame 0 timestamp
    1557539924.599788
]
```

#### Upload PandaSet to Dataloop

To upload the files to the dataset, you can use the following scripts to upload the scene folder to the dataset on the Dataloop platform:

1. Define the `dataset_id`, `scene_folder` and `remote_path` (on the dataset) to the target dataset for uploading the PandaSet scene.

```python
import dtlpy as dl

# Set the dataset id, scene folder path and remote path
dataset_id = "<dataset id>"
scene_folder = "C:/data/pandaset/001"
remote_path = "/001"

dataset = dl.datasets.get(dataset_id=dataset_id)
```

2. Execute the following function to upload the scene to the dataset on the Dataloop platform, ensuring it adheres to the correct structure
   (make sure [dtlpy-lidar](https://github.com/dataloop-ai-apps/dtlpy-lidar) is installed).

```python
import dtlpy as dl
import os
import json
import pathlib
import pickle
import pandas as pd
import open3d as o3d
import shutil

from dtlpylidar.utilities import transformations


def upload_pandaset_to_dataloop(dataset: dl.Dataset, scene_folder: str, remote_path = "/"):
    lidar_folder = os.path.join(scene_folder, "lidar")
    camera_folder = os.path.join(scene_folder, "camera")

    # Create new folder for the updated scene
    updated_scene_folder = os.path.join(scene_folder, "updated_scene")
    updated_scene_lidar_folder = os.path.join(updated_scene_folder, "lidar")
    updated_scene_camera_folder = os.path.join(updated_scene_folder, "camera")
    os.makedirs(updated_scene_lidar_folder, exist_ok=True)
    os.makedirs(updated_scene_camera_folder, exist_ok=True)

    # Copy the scene folder to the updated scene folder
    shutil.copytree(lidar_folder, updated_scene_lidar_folder, dirs_exist_ok=True)
    shutil.copytree(camera_folder, updated_scene_camera_folder, dirs_exist_ok=True)

    # Open the poses.json file to get the poses data
    with open(os.path.join(updated_scene_lidar_folder, "poses.json"), 'r') as f:
        poses_json_data: list = json.load(f)

    # Convert all the PCD files from .pkl to .pcd format and apply the transformations
    pkl_filepaths = sorted(pathlib.Path(updated_scene_lidar_folder).rglob('*.pkl'))
    for idx, pkl_filepath in enumerate(pkl_filepaths):
        with open(pkl_filepath, 'rb') as file:
            data = pickle.load(file)

        # Convert data to DataFrame if needed
        if isinstance(data, pd.DataFrame):
            df = data
        else:
            df = pd.DataFrame(data)

        # Extract x, y, z coordinates
        points = df[['x', 'y', 'z']].to_numpy()

        # Create Open3D PointCloud object
        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(points)

        # Apply transformation
        position = [
            poses_json_data[idx].get("position", dict()).get("x", 0),
            poses_json_data[idx].get("position", dict()).get("y", 0),
            poses_json_data[idx].get("position", dict()).get("z", 0)
        ]
        heading = [
            poses_json_data[idx].get("heading", dict()).get("x", 0),
            poses_json_data[idx].get("heading", dict()).get("y", 0),
            poses_json_data[idx].get("heading", dict()).get("z", 0),
            poses_json_data[idx].get("heading", dict()).get("w", 0)
        ]
        rotation = transformations.rotation_matrix_from_quaternion(*heading)
        transform = transformations.calc_transform_matrix(rotation=rotation, position=position)
        point_cloud.transform(transform)

        # Save the PCD data in .pcd format
        pcd_filepath = pkl_filepath.with_suffix(".pcd")
        o3d.io.write_point_cloud(str(pcd_filepath), point_cloud)
        os.remove(pkl_filepath)

    # Upload the updated scene folder to the dataset
    updated_scene_folder = os.path.join(updated_scene_folder, "*")
    dataset.items.upload(local_path=updated_scene_folder, remote_path=remote_path, overwrite=True)

upload_pandaset_to_dataloop(dataset=dataset, scene_folder=scene_folder, remote_path=remote_path)
```

### Step 2: [Build the Custom Base Parser](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py)

Once all files are ready, all the data available in the dataset needs to be merged in order to create the LiDAR video file (`frames.json` file).

To do that the `CustomBaseParser` methods needs to be implemented to parse the **Calibration data** from the dataset and build the `frames.json` file.

**Notice:** In the next section we will show an example on how to implement the function to support the PandaSet dataset,
and explain for what each method is used for.

#### Example functions implementation for PandaSet:

In this section we will show an example implementation of each method in the `CustomBaseParser` to support parsing the PandaSet dataset `Calibration data` and creating the LiDAR video file.

##### - [Download data (Customizable)](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py#L20)

A method to specify the required binaries and JSON annotations that need to be downloaded for use in subsequent parsing functions.

##### - [Parse LiDAR data (Customizable)](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py#L45)

A method to parse LiDAR sensor data from the downloaded files
(Extrinsic and Timestamps).

- `images_and_pcds.LidarPcdData` - A class that encapsulates LiDAR sensor calibration information for PCD files in the 3D scene (per frame).

`Notice:` This class later get converted into json formant, and get added to the `frames.json` file.

##### - [Parse cameras data (Customizable)](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py#L93)

A method to parse camera data from all available downloaded files
(Intrinsic, Extrinsic, Timestamps and Distortion).

- `images_and_pcds.LidarCameraData` - A class that stores camera calibration information required to position a camera object in the 3D scene (per frame, per camera).
- `images_and_pcds.LidarImageData` - A class extending `images_and_pcds.LidarCameraData` by associating a 2D image with the camera object in the 3D scene (per frame, per camera).

`Notice:` This classes later get converted into json formant, and get added to the `frames.json` file.

##### - [Build LiDAR scene](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py#L251)

A method to combine the `lidar_data` and `cameras_data` to construct the `frames.json` file, which represents a LiDAR video containing all point cloud and image files seamlessly integrated. Each frame includes the following information:

1. `PCD file:` The point cloud data of the 3D scene for the given frame.
2. `JPEG/PNG files:` The images of the available cameras for the given frame.

This integration ensures that each frame is a complete representation of the scene, combining LiDAR and camera data for synchronized analysis.

##### - [Run](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py#L286)

A method to execute the parser to process a dataset containing LiDAR data, using all the above functions, and upload the resulting `frames.json` file.

### Step 3: [Run the Custom Base Parser](https://github.com/dataloop-ai-apps/dtlpy-lidar/blob/13dd1b8f1170438c61376ca10446a78580b3914f/dtlpylidar/parsers/custom_base_parser.py#L332)

After implementing all the required functions in the `CustomBaseParser`, run the following code snippet to run the parser to create and upload the `frames.json` file to the dataset.
