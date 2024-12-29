# Data setup

## Overview

In this process we will prepare and configure the Dataloop system to effectively utilize LiDAR data. \
Setting up the LiDAR data involves several key steps:

1. Files Setup
2. Calibration Data Setup
3. Create the LiDAR Video File

### Supported Files

The setup process include preparing the files for work in a point-cloud annotation/segmentation task. \
The supported files are:

1. **PCD Files:** Point Cloud Data files used for generating the 3D scenes. \
   Both single PCD file and multiple PCD files are supported. \
   For more details about why PCD files are preferred, please refer to the [PCD file format documentation](https://pointclouds.org/documentation/tutorials/pcd_file_format.html).

2. **JPEG/PNG Image Files:** Usually showing the angle and viewport of the cameras that captured the main scene. \
   These images will have real-time projections of the 3D objects annotated in the main point-cloud scene.


## 1. Files Setup

Setup or stitching of point cloud files with camera images is performed by arranging files in designated folders in the root of the dataset or a selected folder inside the dataset.

### Example of arranging the files in the root of the dataset:

1. Since every point cloud file is a frame, they must be first organized/prepared - the file names should be numbers starting from 0, which will define the order of the frames in the 3D scene.

![LidarFolder](../../../../assets/images/lidar/Lidar_folder_1.png)

2. **lidar** folder - All .pcd files are placed in a folder named lidar.

![FramesFolder](../../../../assets/images/lidar/Frame_folder_2.png)

3. **frames** folder - This folder contains subfolders, each with JPEG/PNG images per frame.

   1. The folder contains subfolders with names of the available cameras.

   2. For each available camera folder, the image filenames correspond directly to the PCD filenames. \
      Therefore, the images filenames need to match the 0-N numerical order.

   3. The alphabet order of the camera subfolders will dictate the order in which camera images will be displayed in each frame in the Lidar Studio.


### Example of arranging the files in a selected folder inside the dataset:

![LidarFolderSetupExample](../../../../assets/images/lidar/Lidar_folder_setup_example.png)

The same structure as in the example of arranging the files in the root of the dataset should be kept inside the selected folder.


## 2. Calibration Data Setup

To build the LiDAR video file, the calibration data is required to align the point cloud data with the camera images. \
Extract your dataset calibration data into a `mapping.json` file, in format provided below,
and upload it to the dataset in the same directory where the `lidar` and `frames` folders are located at.

For a detailed explanation about the parameters required in the `mapping.json` file, please refer to the [Camera Calibration Parameters](https://www.mathworks.com/help/vision/ug/camera-calibration.html#Camera_Calibration_Parameters).

```json
{
    "frames": {
        "0": {
            "path": <>, // for frame 0: "lidar/0.pcd" (Relative path from the mapping.json file)
            "timestamp": <>
            "position": { // lidar sensor location (used as the center of the world)
                "x": <>,
                "y": <>,
                "z": <>
            },
            "heading": { // lidar sensor rotation (Quaternion)
                "x": <>,
                "y": <>,
                "z": <>,
                "w": <>
            },
            "images": { // if no images are provided, add an empty dict
                "0": {
                    "image_path": <>, // for frame 0 image 0: "frames/0/0.jpg" (Relative path from the mapping.json file)
                    "timestamp": <>,
                    "intrinsics": { // camera intrinsic
                        "fx": <>, // Focal length in pixels.
                        "fy": <>,
                        "cx": <>, // Optical center (the principal point), in pixels.
                        "cy": <>,
                    },
                    "extrinsics": { // camera extrinsic
                        "translation": { // camera location in world coordinates (in relation to the lidar sensor)
                            "x": <>,
                            "y": <>,
                            "z": <>
                        },
                        "rotation": { // rotation of the camera (Quaternion)
                            "w": <>,
                            "x": <>,
                            "y": <>,
                            "z": <>
                        }
                    },
                    "distortion" : { // distortion parameters
                        "k1": <>,
                        "k2": <>,
                        "p1": <>,
                        "p2": <>,
                        "k3": <>,
                        "k4": <>
                    }
                }
            }
        }
    }
}
```


## 3. Create the LiDAR Video File

Once all files are ready, to create the LiDAR video file (of all the PCD files stitched together), do as follows:

1. Install [Dataloop LiDAR SDK](https://github.com/dataloop-ai-apps/dtlpy-lidar) to your local python environment, using the command:
    ```bash
    pip install git+https://github.com/dataloop-ai-apps/dtlpy-lidar.git
    ```

2. Use the following code snippet to create the LiDAR video file:
    ```python
    import dtlpy as dl
    from dtlpylidar.parsers.base_parser import LidarFileMappingParser

    dataset = dl.datasets.get(dataset_id='dataset-id')
    mapping_item = dataset.items.get(filepath="/mapping.json")
    frames_item = LidarFileMappingParser().parse_data(mapping_item=mapping_item)
    frames_item.open_in_web()
    ```

3. The output item will be the `frame.json` file, a LiDAR video file with all the point cloud and image files stitched together, where each frame contains the following information:
   - **PCD file:** The point cloud data of the 3D scene for the given frame.
   - **JPEG/PNG files:** The images of the available cameras for the given frame.

4. (Optional) Once all files are ready, contact Dataloop to execute the Ground Detection - on each provided .pcd file to enable the Ground Detection Toggle on the Lidar Studio.
