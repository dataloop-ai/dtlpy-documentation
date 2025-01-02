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

3. The output item will be a `frame.json` file (the LiDAR video file) with all the PCD files stitched together,
   where each frame contains the following information:
   - **PCD file:** The point cloud data of the 3D scene for the given frame.
   - **JPEG/PNG files:** The images of the available cameras for the given frame.
   - **Calibration data:** The calibration data of the LiDAR sensor and the cameras for the given frame (as was specified in the `mapping.json` file).

4. (Optional) Once all files are ready, contact Dataloop to execute the Ground Detection - on each provided .pcd file to enable the Ground Detection Toggle on the LiDAR Studio.


## Upload Framed Annotations

See how to upload different types of framed annotations to the LiDAR video item in the [Annotations](https://developers.dataloop.ai/tutorials/annotations/) page, under **LiDAR Annotations** section.

**Notice:** Make sure that the `frames.json` file includes the `fps` key in its metadata. \
Set it to a default value of `1` if it is not already present.
```json
{
    "system":   {
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
