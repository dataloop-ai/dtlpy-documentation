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
   - **JPEG/PNG files:** The images of the available cameras for the given frame.
   - **Calibration data:** The calibration data of the LiDAR sensor and the cameras for the given frame (as was specified in the `mapping.json` file).

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

This notebook provides an advanced guide about how to set up a LiDAR scene dataset on the Dataloop platform
for any directory structure of a LiDAR scene, as long as the files are in the following formats:

1. **3D Scene Files** - Point Cloud Data files in `.pcd` **ASCII** format.
2. **2D Camera Views Files** - Image files in JPEG/PNG formats.
3. **Calibration Data Files** - Any file format that contains the required [Camera Calibration Parameters](https://www.mathworks.com/help/vision/ug/camera-calibration.html#:~:text=the%20intrinsics%20parameters.-,Camera%20Calibration%20Parameters,-The%20calibration%20algorithm).

In this notebook we will show an example of modifying the `AdvancedBaseParser` to support the [PandaSet](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset) dataset. \
However, this parser can be extended to support custom LiDAR scenes by modifying the available `Customizable` methods as needed.

### Step 1: Files Setup

Create a dataset on the Dataloop platform and upload the following required LiDAR files to the dataset:

1. **3D Scene Files** - Point Cloud Data files used for generating the 3D scenes.
2. **2D Camera Views Files** - Usually showing the angle and viewport of the cameras that captured the main scene.
3. **Calibration Data Files** Any type of files that contains all required information to align the point cloud data with the camera images. \
   For a detailed explanation about the parameters required in the mapping.json file, please refer to the Camera Calibration Parameters.

### Example of arranging the files with PandaSet

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

##### `poses.json` file structure (similar for lidar and cameras)

Each object refer to a different frame.

```python
[
    {"position": {"x": 0.0, "y": 0.0, "z": 0.0}, "heading": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0}},  # PCD frame 0 extrinsics / Camera N frame 0 extrinsics
    {"position": {"x": 0.5, "y": 0.5, "z": 0.0}, "heading": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0}}
]
```

##### `intrinsics.json` file structure (for cameras)

Each camera has static intrinsics calibrations across all its images.

```python
{"fx": 933.4667, "fy": 934.6754, "cx": 896.4692, "cy": 507.3557}
```

##### `timestamps.json` file structure (similar for lidar and cameras)

Each object refer to a different frame.

```python
[
    1557539924.49981,  # PCD frame 0 timestamp / Camera N frame 0 timestamp
    1557539924.599788
]
```

### Upload PandaSet to Dataloop

To upload the files to the dataset, you can use the following scripts to upload the scene folder to the dataset on the Dataloop platform:

1. Define the `dataset_id`, `scene_folder` and `remote_path` (on the dataset) to the target dataset for uploading the PandaSet scene.

```python
import dtlpy as dl

# Set the dataset id and the scene folder path
dataset_id = "dataset-id"
scene_folder = "path/to/scene/folder"
remote_path = "/"

dataset = dl.datasets.get(dataset_id=dataset_id)
```

2. Execute the following function to upload the scene to the dataset on the Dataloop platform, ensuring it adheres to the correct structure.

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

### Step 2: Build the Advanced Base Parser

Once all files are ready, all the data available in the dataset needs to be merged in order to create the LiDAR video file (`frames.json` file).

To do that the `AdvancedBaseParser` methods needs to be implemented to parse the **Calibration data** from the dataset
and build the `frames.json` file.

**Notice:** In the next section we will show an example on how to implement the function to support the PandaSet dataset,
and explain for what each method is used for.

```python
import dtlpy as dl
import os
import json
import uuid
import logging
import shutil
import pathlib
import numpy as np

from dtlpylidar.parser_base import (extrinsic_calibrations, images_and_pcds, camera_calibrations, lidar_frame,
                                    lidar_scene)
from dtlpylidar.utilities import transformations

logger = logging.Logger(name="advanced_base_parser")


class AdvancedBaseParser(dl.BaseServiceRunner):
    # TODO: Override this method in the derived class if needed
    @staticmethod
    def download_data(dataset: dl.Dataset, remote_path: str, download_path: str) -> tuple:
        """
        Download the required data for the parser
        :param dataset: Input dataset
        :param remote_path: Path to the remote folder where the LiDAR data is uploaded
        :param download_path: Path to the downloaded data
        :return: (items_path, json_path) Paths to the downloaded items and annotations JSON files directories
        """
        pass

    # TODO: Override this method in the derived class if needed
    @staticmethod
    def parse_lidar_data(items_path: str, json_path: str) -> dict:
        """
        Parse the LiDAR Calibration data to build all the scene LidarPcdData objects
        :param items_path: Paths to the downloaded items directory
        :param json_path: Paths to the downloaded annotations JSON files directory
        :return: lidar_data: Dictionary containing mapping of frame number to LidarPcdData object
        """
        pass

    # TODO: Override this method in the derived class if needed
    @staticmethod
    def parse_cameras_data(items_path: str, json_path: str) -> dict:
        """
        Parse the Cameras Calibration data to build all the scene LidarCameraData and LidarImageData objects
        :param items_path: Paths to the downloaded items directory
        :param json_path: Paths to the downloaded annotations JSON files directory
        :return: lidar_data: Dictionary containing mapping of camera and frame number
        to LidarCameraData and LidarImageData objects
        """
        pass

    @staticmethod
    def build_lidar_scene(lidar_data: dict, cameras_data: dict):
        """
        Merge the all the object of lidar_data and cameras_data to build the LidarScene object that will be uploaded as
        the frames.json item
        :return: scene_data: LidarScene data as JSON that will to be uploaded to the dataloop platform as
        the frames.json item
        """
        scene = lidar_scene.LidarScene()
        frames_number = len(lidar_data)
        for frame_number in range(frames_number):
            logger.info(f"Processing PCD data [Frame: {frame_number}]")
            frame_lidar_pcd_data = lidar_data[frame_number]
            lidar_frame_images = list()

            for camera_idx, (camera_folder, camera_data) in enumerate(cameras_data.items()):
                logger.info(f"Processing Camera data [Frame: {frame_number}, Camera Index: {camera_idx}]")
                frame_lidar_camera_data = camera_data.get(frame_number, dict()).get("lidar_camera", None)
                frame_lidar_image_data = camera_data.get(frame_number, dict()).get("lidar_image", None)

                if frame_lidar_camera_data is None or frame_lidar_image_data is None:
                    continue

                scene.add_camera(frame_lidar_camera_data)
                lidar_frame_images.append(frame_lidar_image_data)

            lidar_scene_frame = lidar_frame.LidarSceneFrame(
                lidar_frame_pcd=frame_lidar_pcd_data,
                lidar_frame_images=lidar_frame_images
            )
            scene.add_frame(lidar_scene_frame)

        scene_data = scene.to_json()
        return scene_data

    def run(self, dataset: dl.Dataset, remote_path: str = "/") -> dl.Item:
        """
        Run the parser
        :param dataset: Input dataset
        :param remote_path: Path to the remote folder where the LiDAR data is uploaded
        :return: frames_item: dl.Item entity of the uploaded frames.json
        """
        if remote_path.startswith("/"):
            remote_path = remote_path[1:]

        if remote_path.endswith("/"):
            remote_path = remote_path[:-1]

        base_path = f"{dataset.name}_{str(uuid.uuid4())}"
        download_path = os.path.join(os.getcwd(), base_path)
        try:
            items_path, json_path = self.download_data(
                dataset=dataset,
                remote_path=remote_path,
                download_path=download_path
            )

            lidar_data = self.parse_lidar_data(items_path=items_path, json_path=json_path)
            cameras_data = self.parse_cameras_data(items_path=items_path, json_path=json_path)
            scene_data = self.build_lidar_scene(lidar_data=lidar_data, cameras_data=cameras_data)

            frames_item = dataset.items.upload(
                remote_name="frames.json",
                remote_path=f"/{remote_path}",
                local_path=json.dumps(scene_data).encode(),
                overwrite=True,
                item_metadata={
                    "system": {
                        "shebang": {
                            "dltype": "PCDFrames"
                        }
                    },
                    "fps": 1
                }
            )
        finally:
            shutil.rmtree(path=download_path, ignore_errors=True)

        return frames_item
```

### Example functions implementation for PandaSet:

In this section we will show an example implementation of each method in the `AdvancedBaseParser` to support parsing the PandaSet dataset
`Calibration data` and creating the LiDAR video file.

#### Download data (Customizable)

A method to specify the required binaries and JSON annotations that need to be downloaded for use in subsequent parsing functions.

```python
@staticmethod
def download_data(dataset: dl.Dataset, remote_path: str, download_path: str) -> tuple:
    """
    Download the required data for the parser
    :param dataset: Input dataset
    :param remote_path: Path to the remote folder where the LiDAR data is uploaded
    :param download_path: Path to the downloaded data
    :return: (items_path, json_path) Paths to the downloaded items and annotations JSON files directories
    """
    # Download items dataloop annotation JSONs
    # (PCD and Image annotation JSONs contains the Dataloop platform references (Like: ID) to the remote files)
    filters = dl.Filters(field="metadata.system.mimetype", values="*pcd*", method=dl.FiltersMethod.OR)
    filters.add(field="metadata.system.mimetype", values="*image*", method=dl.FiltersMethod.OR)
    dataset.download_annotations(local_path=download_path, filters=filters)

    # Download required binaries (Calibrations Data)
    # PandaSet Calibration Data is saved in JSON files (Like: poses.json, intrinsics.json, timestamps.json)
    filters = dl.Filters(field="metadata.system.mimetype", values="*json*")
    dataset.items.download(local_path=download_path, filters=filters)

    items_path = os.path.join(download_path, "items", remote_path)
    json_path = os.path.join(download_path, "json", remote_path)
    return items_path, json_path
```

#### Parse LiDAR data (Customizable)

A method to parse LiDAR sensor data from the downloaded files
(Extrinsic and Timestamps).

- `images_and_pcds.LidarPcdData` - A class that encapsulates LiDAR sensor calibration information for PCD files in the 3D scene (per frame).

`Notice:` This class later get converted into json formant, and get added to the `frames.json` file.

```python
@staticmethod
def parse_lidar_data(items_path: str, json_path: str) -> dict:
    """
    Parse the LiDAR Calibration data to build all the scene LidarPcdData objects
    :param items_path: Paths to the downloaded items directory
    :param json_path: Paths to the downloaded annotations JSON files directory
    :return: lidar_data: Dictionary containing mapping of frame number to LidarPcdData object
    """
    lidar_data = dict()

    lidar_json_path = os.path.join(json_path, "lidar")
    lidar_items_path = os.path.join(items_path, "lidar")

    # Opening the poses.json file to get the Timestamps of the Lidar Scene per frame
    timestamps_json = os.path.join(lidar_items_path, "timestamps.json")
    with open(timestamps_json, 'r') as f:
        timestamps_json_data: list = json.load(f)

    # Get all the lidar JSONs sorted by frame number
    lidar_jsons = pathlib.Path(lidar_json_path).rglob('*.json')
    lidar_jsons = sorted(lidar_jsons, key=lambda x: int(x.stem))

    for lidar_frame_idx, lidar_json in enumerate(lidar_jsons):
        with open(lidar_json, 'r') as f:
            lidar_json_data = json.load(f)

        ground_map_id = lidar_json_data.get("metadata", dict()).get("user", dict()).get(
            "lidar_ground_detection", dict()).get("groundMapId", None)
        lidar_translation = extrinsic_calibrations.Translation(x=0, y=0, z=0)
        lidar_rotation = extrinsic_calibrations.QuaternionRotation(x=0, y=0, z=0, w=1)
        lidar_timestamp = str(timestamps_json_data[lidar_frame_idx])

        lidar_pcd_data = images_and_pcds.LidarPcdData(
            item_id=lidar_json_data.get("id"),
            ground_id=ground_map_id,
            remote_path=lidar_json_data.get("filename"),
            extrinsic=extrinsic_calibrations.Extrinsic(
                rotation=lidar_rotation,
                translation=lidar_translation
            ),
            timestamp=lidar_timestamp
        )
        lidar_data[lidar_frame_idx] = lidar_pcd_data

    return lidar_data
```

#### Parse cameras data (Customizable)

A method to parse camera data from all available downloaded files
(Intrinsic, Extrinsic, Timestamps and Distortion).

- `images_and_pcds.LidarCameraData` - A class that stores camera calibration information required to position a camera object in the 3D scene (per frame, per camera). \
- `images_and_pcds.LidarImageData` - A class extending `images_and_pcds.LidarCameraData` by associating a 2D image with the camera object in the 3D scene (per frame, per camera).

`Notice:` This classes later get converted into json formant, and get added to the `frames.json` file.

```python
@staticmethod
def parse_cameras_data(items_path: str, json_path: str) -> dict:
    """
    Parse the Cameras Calibration data to build all the scene LidarCameraData and LidarImageData objects
    :param items_path: Paths to the downloaded items directory
    :param json_path: Paths to the downloaded annotations JSON files directory
    :return: lidar_data: Dictionary containing mapping of camera and frame number
    to LidarCameraData and LidarImageData objects
    """
    # Get lidar transforms for all the frames
    lidar_transform_list = list()

    lidar_items_path = os.path.join(items_path, "lidar")
    lidar_json_path = os.path.join(json_path, "lidar")

    poses_json = os.path.join(lidar_items_path, "poses.json")
    with open(poses_json, 'r') as f:
        poses_json_data: list = json.load(f)

    # Get count of all the lidar JSONs
    lidar_jsons = pathlib.Path(lidar_json_path).rglob('*.json')
    lidar_jsons_count = len(list(lidar_jsons))

    for idx in range(lidar_jsons_count):
        lidar_position_idx = [
            poses_json_data[idx].get("position", dict()).get("x", 0),
            poses_json_data[idx].get("position", dict()).get("y", 0),
            poses_json_data[idx].get("position", dict()).get("z", 0)
        ]
        lidar_heading_idx = [
            poses_json_data[idx].get("heading", dict()).get("x", 0),
            poses_json_data[idx].get("heading", dict()).get("y", 0),
            poses_json_data[idx].get("heading", dict()).get("z", 0),
            poses_json_data[idx].get("heading", dict()).get("w", 1)
        ]
        lidar_rotation_idx = transformations.rotation_matrix_from_quaternion(*lidar_heading_idx)
        lidar_transform_idx = transformations.calc_transform_matrix(
            rotation=lidar_rotation_idx,
            position=lidar_position_idx
        )
        lidar_transform_list.append(lidar_transform_idx)

    # Get all the cameras data
    cameras_data = dict()

    camera_json_path = os.path.join(json_path, "camera")
    camera_items_path = os.path.join(items_path, "camera")

    # Get the list of all the available camera folders, and building the cameras data objects per camera per frame
    camera_folders_list = sorted(os.listdir(camera_json_path))
    for camera_folder_idx, camera_folder in enumerate(camera_folders_list):
        cameras_data[camera_folder] = dict()

        camera_folder_json_path = os.path.join(camera_json_path, camera_folder)
        camera_folder_items_path = os.path.join(camera_items_path, camera_folder)

        # Opening the intrinsics.json file to get the Intrinsics (fx, fy, cx, cy) of the Current Camera per frame
        intrinsics_json = os.path.join(camera_folder_items_path, "intrinsics.json")
        with open(intrinsics_json, 'r') as f:
            intrinsics_json_data: dict = json.load(f)

        # Opening the poses.json file to get the Extrinsic (Translation and Rotation) of the Current Camera per frame
        poses_json = os.path.join(camera_folder_items_path, "poses.json")
        with open(poses_json, 'r') as f:
            poses_json_data: list = json.load(f)

        # Opening the poses.json file to get the Timestamps of the Current Camera per frame
        timestamps_json = os.path.join(camera_folder_items_path, "timestamps.json")
        with open(timestamps_json, 'r') as f:
            timestamps_json_data: list = json.load(f)

        # Get all the camera JSONs sorted by frame number
        camera_jsons = pathlib.Path(camera_folder_json_path).rglob('*.json')
        camera_jsons = sorted(camera_jsons, key=lambda x: int(x.stem))

        for camera_frame_idx, camera_json in enumerate(camera_jsons):
            with open(camera_json, 'r') as f:
                camera_json_data = json.load(f)

            camera_id = f"{camera_folder}_frame_{camera_frame_idx}"
            camera_intrinsic = camera_calibrations.Intrinsic(
                fx=intrinsics_json_data.get("fx", 0),
                fy=intrinsics_json_data.get("fy", 0),
                cx=intrinsics_json_data.get("cx", 0),
                cy=intrinsics_json_data.get("cy", 0)
            )

            # Get lidar transform for the current camera frame
            lidar_transform_idx = lidar_transform_list[camera_frame_idx]

            # Get camera transform for the current camera frame
            camera_position_idx = [
                poses_json_data[camera_frame_idx].get("position", dict()).get("x", 0),
                poses_json_data[camera_frame_idx].get("position", dict()).get("y", 0),
                poses_json_data[camera_frame_idx].get("position", dict()).get("z", 0)
            ]
            camera_heading_idx = [
                poses_json_data[camera_frame_idx].get("heading", dict()).get("x", 0),
                poses_json_data[camera_frame_idx].get("heading", dict()).get("y", 0),
                poses_json_data[camera_frame_idx].get("heading", dict()).get("z", 0),
                poses_json_data[camera_frame_idx].get("heading", dict()).get("w", 1)
            ]

            # Calculate updated camera transform
            camera_rotation_idx = transformations.rotation_matrix_from_quaternion(*camera_heading_idx)
            camera_transform_idx = transformations.calc_transform_matrix(
                rotation=camera_rotation_idx,
                position=camera_position_idx
            )
            camera_updated_transform_idx = np.dot(lidar_transform_idx, camera_transform_idx)
            camera_updated_position_idx = transformations.translation_vector_from_transform_matrix(
                transform_matrix=camera_updated_transform_idx
            )

            # Extracting the updated camera translation and rotation
            camera_updated_rotation_idx = transformations.rotation_matrix_from_transform_matrix(
                transform_matrix=camera_updated_transform_idx
            )
            camera_updated_heading_idx = transformations.quaternion_from_rotation_matrix(
                rotation_matrix=camera_updated_rotation_idx
            )

            camera_translation = extrinsic_calibrations.Translation(*camera_updated_position_idx)
            camera_rotation = extrinsic_calibrations.QuaternionRotation(*camera_updated_heading_idx)
            camera_distortion = camera_calibrations.Distortion(
                k1=0,
                k2=0,
                k3=0,
                p1=0,
                p2=0
            )
            camera_timestamp = str(timestamps_json_data[camera_frame_idx])

            lidar_camera_data = camera_calibrations.LidarCameraData(
                intrinsic=camera_intrinsic,
                extrinsic=extrinsic_calibrations.Extrinsic(
                    rotation=camera_rotation,
                    translation=camera_translation
                ),
                channel=camera_json_data.get("filename"),
                distortion=camera_distortion,
                cam_id=camera_id,
            )

            lidar_image_data = images_and_pcds.LidarImageData(
                item_id=camera_json_data.get("id"),
                lidar_camera=lidar_camera_data,
                remote_path=camera_json_data.get("filename"),
                timestamp=camera_timestamp
            )

            cameras_data[camera_folder][camera_frame_idx] = {
                "lidar_camera": lidar_camera_data,
                "lidar_image": lidar_image_data
            }

    return cameras_data
```

#### Build LiDAR scene

A method to combine the `lidar_data` and `cameras_data` to construct the `frames.json` file, which represents a LiDAR video containing all point cloud and image files seamlessly integrated. Each frame includes the following information:

1. `PCD file:` The point cloud data of the 3D scene for the given frame.
2. `JPEG/PNG files:` The images of the available cameras for the given frame.

This integration ensures that each frame is a complete representation of the scene, combining LiDAR and camera data for synchronized analysis.

```python
@staticmethod
def build_lidar_scene(lidar_data: dict, cameras_data: dict):
    """
    Merge the all the object of lidar_data and cameras_data to build the LidarScene object that will be uploaded as
    the frames.json item
    :return: scene_data: LidarScene data as JSON that will to be uploaded to the dataloop platform as
    the frames.json item
    """
    scene = lidar_scene.LidarScene()
    frames_number = len(lidar_data)
    for frame_number in range(frames_number):
        logger.info(f"Processing PCD data [Frame: {frame_number}]")
        frame_lidar_pcd_data = lidar_data[frame_number]
        lidar_frame_images = list()

        for camera_idx, (camera_folder, camera_data) in enumerate(cameras_data.items()):
            logger.info(f"Processing Camera data [Frame: {frame_number}, Camera Index: {camera_idx}]")
            frame_lidar_camera_data = camera_data.get(frame_number, dict()).get("lidar_camera", None)
            frame_lidar_image_data = camera_data.get(frame_number, dict()).get("lidar_image", None)

            if frame_lidar_camera_data is None or frame_lidar_image_data is None:
                continue

            scene.add_camera(frame_lidar_camera_data)
            lidar_frame_images.append(frame_lidar_image_data)

        lidar_scene_frame = lidar_frame.LidarSceneFrame(
            lidar_frame_pcd=frame_lidar_pcd_data,
            lidar_frame_images=lidar_frame_images
        )
        scene.add_frame(lidar_scene_frame)

    scene_data = scene.to_json()
    return scene_data
```

#### Run

A method to execute the parser to process a dataset containing LiDAR data, using all the above functions, and upload the resulting `frames.json` file.

```python
def run(self, dataset: dl.Dataset, remote_path: str = "/") -> dl.Item:
    """
    Run the parser
    :param dataset: Input dataset
    :param remote_path: Path to the remote folder where the LiDAR data is uploaded
    :return: frames_item: dl.Item entity of the uploaded frames.json
    """
    if remote_path.startswith("/"):
        remote_path = remote_path[1:]

    if remote_path.endswith("/"):
        remote_path = remote_path[:-1]

    base_path = f"{dataset.name}_{str(uuid.uuid4())}"
    download_path = os.path.join(os.getcwd(), base_path)
    try:
        items_path, json_path = self.download_data(
            dataset=dataset,
            remote_path=remote_path,
            download_path=download_path
        )

        lidar_data = self.parse_lidar_data(items_path=items_path, json_path=json_path)
        cameras_data = self.parse_cameras_data(items_path=items_path, json_path=json_path)
        scene_data = self.build_lidar_scene(lidar_data=lidar_data, cameras_data=cameras_data)

        frames_item = dataset.items.upload(
            remote_name="frames.json",
            remote_path=f"/{remote_path}",
            local_path=json.dumps(scene_data).encode(),
            overwrite=True,
            item_metadata={
                "system": {
                    "shebang": {
                        "dltype": "PCDFrames"
                    }
                },
                "fps": 1
            }
        )
    finally:
        shutil.rmtree(path=download_path, ignore_errors=True)

    return frames_item
```

### Step 3: Run the Advanced Base Parser

After implementing all the required functions in the `AdvancedBaseParser`, run the following code snippet to run the parser
to create and upload the `frames.json` file to the dataset:

```python
def run_parser():
    dataset = dl.datasets.get(dataset_id="673615818ab4c9a0b0be683e")
    parser = AdvancedBaseParser()
    frames_item = parser.run(dataset=dataset)
    # frames_item.open_in_web()
    print(frames_item)


if __name__ == '__main__':
    run_parser()
```
