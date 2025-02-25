# 🎬 Video Annotations - Bringing Motion to Life!

Welcome to the exciting world of video annotations! While image annotations are like taking snapshots, video annotations are like directing a movie - we're working with objects that move and change over time. Let's learn how to capture this motion! 

# 🎯 Getting Started with Video Annotations

## Project Setup
First, let's set up our environment:

```python
import dtlpy as dl

# Login if needed
if dl.token_expired():
    dl.login()

# Get your project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')

# Get your video file
item = dataset.items.get(filepath='/your-video.mp4')
```

## Your First Video Annotation
Think of video annotations as telling a story about objects across frames. Here's how to start:

```python
# Create your annotation builder
builder = item.annotations.builder()

# Add a simple box annotation that spans multiple frames
builder.add(annotation_definition=dl.Box(top=10,
                                       left=10,
                                       bottom=100,
                                       right=100,
                                       label='moving-object'),
           frame_num=1,              # Starting frame
           end_frame_num=30)         # Ending frame

# Save your work
item.annotations.upload(builder)
```

# 🎭 Advanced Video Annotations

## Object Tracking
Track objects as they move through your video. Think of it like following an actor through different scenes:

```python
# Create a tracked box that changes position
builder.add(annotation_definition=dl.Box(top=10,
                                       left=10,
                                       bottom=100,
                                       right=100,
                                       label='tracked-object'),
           frame_num=1,
           end_frame_num=30,
           object_id='unique_object_1')  # Link annotations of the same object

# Add the same object in a different position in later frames
builder.add(annotation_definition=dl.Box(top=20,
                                       left=20,
                                       bottom=110,
                                       right=110,
                                       label='tracked-object'),
           frame_num=31,
           end_frame_num=60,
           object_id='unique_object_1')
```

## Frame-by-Frame Annotations
Create detailed annotations that change in every frame:

```python
# Create annotation that changes in each frame
annotation = dl.Annotation.new(item=item)

# Add annotations for 100 frames
for i_frame in range(100):
    annotation.add_frame(
        annotation_definition=dl.Box(
            top=2 * i_frame,                    # Box moves down
            left=2 * (i_frame + 10),            # Box moves right
            bottom=2 * (i_frame + 50),          # Maintain height
            right=2 * (i_frame + 100),          # Maintain width
            label="moving-box"
        ),
        frame_num=i_frame
    )

# Upload to platform
annotation.upload()
```

## Multiple Objects Per Frame
Handle multiple objects in each frame:

```python
# Create annotation builder
builder = item.annotations.builder()

# Add 10 different objects across 100 frames
for i_frame in range(100):
    for i_detection in range(10):
        builder.add(
            annotation_definition=dl.Box(
                top=2 * i_frame,
                left=2 * i_detection,
                bottom=2 * i_frame + 10,
                right=2 * i_detection + 100,
                label="object-" + str(i_detection)
            ),
            frame_num=i_frame,
            object_id=i_detection + 1  # Unique ID for each object
        )

# Upload all annotations
item.annotations.upload(builder)
```

# 🎨 Working with Video Frames

## Reading Frame Annotations
Extract information about annotations in specific frames:

```python
# Get all annotations
annotations = item.annotations.list()

# Print information for each annotation
for annotation in annotations:
    print(f"Object ID: {annotation.object_id}")
    # Get coordinates for each frame
    for frame_num, frame in annotation.frames.items():
        print(f"Frame {frame_num}:")
        print(f"  Position: ({frame.left}, {frame.top}) to ({frame.right}, {frame.bottom})")
```

## Creating Frame Snapshots
Generate still images from your video for easier annotation:

```python
# Generate snapshots every 30 frames
dl.utilities.Videos.video_snapshots_generator(
    item=item,
    frame_interval=30
)
```

# 🎥 Video Playback and Visualization

## Video Player with Annotations
View your video with annotations:

```python
from dtlpy.utilities.videos.video_player import VideoPlayer

# Launch video player with annotations
VideoPlayer(project_name='project_name',
           dataset_name='dataset_name',
           item_filepath='/path/to/video.mp4')
```

## Visualizing Frame Annotations
Check annotations in specific frames:

```python
import matplotlib.pyplot as plt

# Get all annotations
annotations = item.annotations.list()

# Show annotations for frame 55
frame_annotation = annotations.get_frame(frame_num=55)

# Display the frame with annotations
plt.figure(figsize=(10, 8))
plt.imshow(frame_annotation.show())
plt.title(f"Frame 55 - {frame_annotation.label}")
plt.axis('off')
plt.show()
```

# 💡 Pro Tips for Video Annotations

## Best Practices
- Use consistent object IDs for tracking the same object
- Consider frame rate when setting frame numbers
- Break long videos into logical segments
- Keep annotation styles consistent across frames

## Performance Optimization
- Work with video segments for long files
- Use keyframes for efficiency
- Consider frame sampling for initial passes
- Verify tracking consistency
- Use batch operations when possible

## Quality Control
- Review annotations across multiple frames
- Check object persistence and tracking
- Verify temporal consistency
- Document frame rate and timing information
- Test playback with annotations

# 🔧 Troubleshooting Common Issues

## Frame Synchronization
- Ensure frame numbers match video timing
- Check for gaps in tracking
- Verify object IDs are consistent
- Monitor frame rate changes

## Memory Management
- Process long videos in segments
- Use frame intervals for large files
- Clean up resources after processing
- Monitor memory usage during batch operations

Need help? Check out our other tutorials or reach out to our support team. Happy video annotating! 🎥✨
