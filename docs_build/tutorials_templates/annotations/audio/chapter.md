# Audio Item

Read more about our audio studio [here](https://docs.dataloop.ai/docs/audio-guide).

For audio files (e.g. FLAC, mp3, etc.) we have a few annotation option available:

## Classification

You can classify an entire audio item or by selecting start and end time:

```python

import dtlpy as dl

project = dl.projects.get('My Project')
dataset = project.datasets.get('My Dataset')
item = dataset.items.get(filepath='/my_item.mp3')
# Create a builder instance and load annotation from the VTT file
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='Whisper'),
            start_time=1.0,
            end_time=2.5)
# Upload annotations to the item
item.annotations.upload(builder)
```

## Transcription

Our SDK supports importing VTT files directly with the `from_vtt_file` method:

```python
item = dataset.items.get(filepath='/my_item.mp3')
# Create a builder instance and load annotation from the VTT file
builder = item.annotations.builder()
builder.from_vtt_file(filepath=r"E:\TypesExamples\audio\subtitles.vtt")
# Upload annotations to the item
item.annotations.upload(builder)

```

Or read any other file or source and upload the annotations directly:

```python
item = dataset.items.get(filepath='/my_item.mp4')
# Using annotation builder
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Subtitle(label='<label>',
                                              text='<text>'),
            start_time='<start>',
            end_time='<end>')
```

