# Advanced Data Setup (Using custom base parser)

## Brief explanation

This notebook provides a guide about how to set up a LiDAR scene dataset on the Dataloop platform (Using [PandaSet](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset) as an example). \
This example can be extended to support custom LiDAR scenes by modifying the available Customizable methods as needed.

__Important Notes:__

* __File Format Assumptions:__ \
  The converter assumes that the remote dataset already has PandaSet `.pkl` files converted into `.pcd` files for the point cloud data. For more details on why .pcd files are preferred, please refer to the [PCD file format documentation](https://pointclouds.org/documentation/tutorials/pcd_file_format.html).
* __Conversion Scripts:__ \
  You can find helpful scripts for converting `.pkl` files to `.pcd` in the dtlpylidar/utilities/converters directory.


## 1. Files Setup

Create a dataset on the Dataloop platform and upload the following required LiDAR files to the dataset:
1. **PCD Files:** Point Cloud Data files used for generating the 3D scenes.
2. **JPEG/PNG Image Files:** Usually showing the angle and viewport of the cameras that captured the main scene.
3. **Calibration Files:** Any type of files that contains all required information to align the point cloud data with the camera images. \
   For a detailed explanation about the parameters required in the mapping.json file, please refer to the Camera Calibration Parameters.

### Example of arranging the files with PandaSet:

To prepare the PandaSet dataset, do as follows:
1. Go to [PandaSet Kaggle Page](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset).
2. Download the dataset and extract the files from the zip files.
3. Open a project on the Dataloop platform and create a new dataset for it.
4. Select a scene folder from the extracted files and upload it to the dataset, as follows:
   1. The `lidar` folder with the `.ply` files converted to `.pcd` files.
   2. The `camera` folder in the same structure.

#### Dataset structure explanation:

The PandaSet scene folder structure:
* `lidar`:
  * Point cloud files in `.pkl` format for each frame (must be converted to `.pcd` format).
  * `poses.json`– contains the poses for each frame.
  * `timestamps.json` (optional) – includes timestamps for the frames.
* `camera`:
  * Per-camera sub-folder:
    * Images for each frame.
    * `intrinsics.json` – camera intrinsic parameters.
    * `poses.json` – camera poses.
    * `timestamps.json` (optional) – includes timestamps for the frames.

#### Json files structure

##### `poses.json` file structure (similar for lidar and cameras):

Each object refer to a different frame.

```python
[
    {"position": {"x": 0.0, "y": 0.0, "z": 0.0}, "heading": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0}},  # PCD frame 0 extrinsics / Camera N frame 0 extrinsics
    {"position": {"x": 0.5, "y": 0.5, "z": 0.0}, "heading": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0}}
]
```

##### `intrinsics.json` file structure (for cameras):

Each camera has static intrinsics calibrations across all its images.

```python
{"fx": 933.4667, "fy": 934.6754, "cx": 896.4692, "cy": 507.3557}
```

##### `timestamps.json` file structure (similar for lidar and cameras):

Each object refer to a different frame.

```python
[
    1557539924.49981,  # PCD frame 0 timestamp / Camera N frame 0 timestamp
    1557539924.599788
]
```

#### 2. Build and run the Custom Base Parser

```python
from dtlpylidar.parser_base import extrinsic_calibrations
from dtlpylidar.parser_base import images_and_pcds, camera_calibrations, lidar_frame, lidar_scene
import dtlpy as dl
import os
import json
import uuid
import logging
import shutil
import pathlib

logger = logging.Logger(name="lidar_base_parser")


class LidarBaseParser(dl.BaseServiceRunner):
    # TODO: Override this method in the derived class if needed
    @staticmethod
    def download_data(dataset: dl.Dataset, remote_path: str, download_path: str) -> tuple:
        """
        Download the required data for the parser
        :param dataset: Input dataset
        :param remote_path: Path to the remote folder where the Lidar data is uploaded
        :param download_path: Path to the downloaded data
        :return: (items_path, json_path) Paths to the downloaded items and annotations JSON files directories
        """
        pass

    # TODO: Override this method in the derived class if needed
    @staticmethod
    def parse_lidar_data(items_path: str, json_path: str) -> dict:
        """
        Parse the Lidar Calibration data to build all the scene LidarPcdData objects
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

    def run(self, dataset: dl.Dataset, remote_path: str = "/"):
        """
        Run the parser
        :param dataset: Input dataset
        :param remote_path: Path to the remote folder where the Lidar data is uploaded
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


def test_parser():
    dataset = dl.datasets.get(dataset_id="")
    parser = LidarBaseParser()
    print(parser.run(dataset=dataset))


if __name__ == '__main__':
    test_parser()
```
