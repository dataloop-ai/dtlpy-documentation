# 🚗 3D World of LiDAR Annotations! 

Welcome to the exciting world of 3D annotations! While 2D annotations are like drawing on paper, LiDAR annotations are like sculpting in space. Let's learn how to create these digital sculptures! 🎨

## Creating Your First 3D Cuboid

Think of a 3D cuboid as a digital box that can float, rotate, and resize in 3D space. Here's how to create one:

```python
import dtlpy as dl
from scipy.spatial.transform import Rotation

# 1. Set Up Your Canvas (Get your dataset and frames)
dataset = dl.datasets.get(dataset_id="dataset-id")
frames_item = dataset.items.get(filepath='/frames.json')

# 2. Grab Your Digital Sculpting Tools
builder = frames_item.annotations.builder()

# 3. Define Your 3D Masterpiece
label = "Car"  # What are we creating?
position = [
    0.0,  # Where is it in X? (left/right)
    0.0,  # Where is it in Y? (forward/backward)
    0.0,  # Where is it in Z? (up/down)
]
scale = [
    1.0,  # How wide is it?
    1.0,  # How long is it?
    1.0,  # How tall is it?
]

# 4. Give it the Perfect Rotation
rotation = Rotation.from_quat([
    0.0,  # Rotation around X
    0.0,  # Rotation around Y
    0.0,  # Rotation around Z
    1.0,  # How much to rotate
]).as_euler(
    seq="xyz",
    degrees=False
)

# 5. Add Some Extra Details
attributes = {"onRoad": True}  # Additional information
description = "Car on road"    # A helpful note

# 6. Put It All Together
annotation_definition = dl.Cube3d(
    label=label,
    position=position,
    scale=scale,
    rotation=rotation,
    attributes=attributes,
    description=description
)

# 7. Place It in Your Scene
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

# 8. Save Your Work
builder.upload()
```

# 💡 Pro Tips for LiDAR Annotations

- Use consistent object IDs when tracking objects across frames
- Take advantage of attributes to add extra information about the objects

# 🎓 Advanced Topics

## Working with Multiple Frames
When annotating LiDAR data, you'll often work with sequences of frames. Here are some best practices:
- Keep object IDs consistent across frames for tracking
- Use the frame_num and end_frame_num parameters to specify temporal information
- Consider using metadata to store frame-specific information

## Coordinate Systems
LiDAR data typically uses a right-handed coordinate system where:
- X points to the right
- Y points forward
- Z points up

Remember this when positioning your annotations!

Need help? Check out our other tutorials or reach out to our support team. Happy 3D annotating! 🎉
