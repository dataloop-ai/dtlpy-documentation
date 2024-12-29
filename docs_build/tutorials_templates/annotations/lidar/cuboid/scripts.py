def section1():
    import dtlpy as dl
    from scipy.spatial.transform import Rotation

    # 0. Get the dataset and the frames item
    dataset = dl.datasets.get(dataset_id="dataset-id")
    frames_item = dataset.items.get(filepath='/frames.json')

    # 1. Create annotations builder
    builder = frames_item.annotations.builder()

    # 2. Define the Cube 3D calibrations data
    label = "Car"  # Annotation Label
    position = [
        0.0,  # Position X Coordinate
        0.0,  # Position Y Coordinate
        0.0,  # Position Z Coordinate
    ]
    scale = [
        1.0,  # Scale of X Dimension
        1.0,  # Scale of Y Dimension
        1.0,  # Scale of Z Dimension
    ]
    rotation = Rotation.from_quat([
        0.0,  # Quaternion X Coordinate
        0.0,  # Quaternion Y Coordinate
        0.0,  # Quaternion Z Coordinate
        1.0,  # Quaternion W Coordinate
    ]).as_euler(
        seq="xyz",
        degrees=False
    )
    attributes = {"onRoad": True}  # Annotation Attributes
    description = "Car on road"  # Annotation Description
    annotation_definition = dl.Cube3d(
        label=label,
        position=position,
        scale=scale,
        rotation=rotation,
        attributes=attributes,
        description=description
    )

    # 3. Define the Cube 3D Annotation final parameters and upload it to the lidar scene
    frame_num = 0
    end_frame_num = 1
    object_id = "0"
    metadata = {"user": {"Car": "onRoad"}}
    builder.add(
        annotation_definition=annotation_definition,
        frame_num=frame_num,
        end_frame_num=end_frame_num,
        object_id=object_id,
        metadata=metadata
    )
    builder.upload()
