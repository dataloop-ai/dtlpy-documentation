# Data setup


## Files and Calibration Data Setup

To prepare a dataset for LiDAR video creation, please ensure that you complete the prerequisite steps outlined in the [LiDAR Data Setup](https://docs.dataloop.ai/docs/lidar-data-setup) documentation.


## Create the LiDAR Video File

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

3. The output item will be the `frame.json` file, a LiDAR video file with all the point cloud and image files stitched together, where each frame contains the following information:
   - **PCD file:** The point cloud data of the 3D scene for the given frame.
   - **JPEG/PNG files:** The images of the available cameras for the given frame.

4. (Optional) Once all files are ready, contact Dataloop to execute the Ground Detection - on each provided .pcd file to enable the Ground Detection Toggle on the Lidar Studio.


## Upload Framed Annotations

Check out how to upload different type of annotations to the LiDAR video:

* [Cuboid Annotations](https://developers.dataloop.ai/tutorials/annotations/lidar/cuboid/chapter/)
