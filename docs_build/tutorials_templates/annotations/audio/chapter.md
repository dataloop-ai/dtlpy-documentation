# 🎵 Audio Annotations - Making Sound Visible!

Welcome to the world of audio annotations! While other annotations deal with what you can see, audio annotations help us mark what you can hear. Let's explore how to capture and annotate sound! 

## 🎯 Basic Audio Annotation

Think of audio annotations like marking timestamps in a song or podcast. Here's how to create one:

```python
import dtlpy as dl

project = dl.projects.get('My Project')
dataset = project.datasets.get('My Dataset')
item = dataset.items.get(filepath='/your-audio.wav')
builder = item.annotations.builder()

# Create a simple audio segment annotation
builder.add(annotation_definition=dl.Audio(start_time=1.5,    # Start time in seconds
                                         end_time=3.2,        # End time in seconds
                                         label='speech',
                                         attributes={'speaker': 'person1',
                                                   'language': 'english'}))

# Save your work
item.annotations.upload(builder)
```

## 🎼 Advanced Audio Annotations

### Transcription Annotations
Add text transcriptions to your audio segments:

```python
item = dataset.items.get(filepath='/my_item.mp3')
# Create a builder instance and load annotation from the VTT file
builder = item.annotations.builder()
builder.from_vtt_file(filepath=r"E:\TypesExamples\audio\subtitles.vtt")
# Upload annotations to the item
item.annotations.upload(builder)

```

Another example:

``python
import webvtt
import datetime
filepath = '/home/subtitles.vtt'
builder = item.annotations.builder()
for caption in webvtt.read(filepath):
    h, m, s = caption.start.split(':')
    start_time = datetime.timedelta(hours=float(h), minutes=float(m), seconds=float(s)).
    total_seconds()
    h, m, s = caption.end.split(':')
    end_time = datetime.timedelta(hours=float(h), minutes=float(m), seconds=float(s)).
    total_seconds()

    builder.add(annotation_definition=dl.Subtitle(label='Speaker1',
                                                  text=caption.text),
                start_time=start_time,
                end_time=end_time)

```


# 💡 Pro Tips for Audio Annotations

- Always verify your timestamps match the audio content
- Use consistent labels for similar sound types
- Consider using attributes for additional context like speaker ID or sound quality
- Keep track of overlapping annotations

# 🎓 Best Practices

## Working with Long Audio Files
When dealing with lengthy recordings:
- Break down the file into logical segments
- Use clear naming conventions for different types of sounds
- Consider using multiple passes for different annotation types
- Document any audio quality issues or background noise

## Annotation Guidelines
For consistent audio annotations:
- Define clear rules for segment boundaries
- Document how to handle overlapping sounds
- Establish conventions for speaker identification
- Use attributes to capture audio characteristics

## Audio Quality Considerations
- Note any background noise or interference
- Document audio channel information
- Consider sample rate and bit depth
- Mark sections with poor audio quality

Need help? Check out our other tutorials or reach out to our support team. Happy audio annotating! 🎧✨

