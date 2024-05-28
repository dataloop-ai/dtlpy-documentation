# Audio Item

Read more about our audio studio [here](https://docs.dataloop.ai/docs/audio-guide).

For audio files (e.g. FLAC, mp3, etc.) we use the `subtitle` annotation type:

## Classification

You can classify an entire audio item or by selecting start and end time.
Setting the text to an empty string will not add the transcription, but only the desired class:

```python

import dtlpy as dl

project = dl.projects.get('My Project')
dataset = project.datasets.get('My Dataset')
item = dataset.items.get(filepath='/my_item.mp3')
# Create a builder instance and load annotation from the VTT file
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Subtitle(label='Whisper', text=''),
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
Since there is no label in the vtt files (only time and text), the default label for those annotation will be `Text`.

For any other specific use, you can read the vtt file (or any other format) and upload the annotations directly:

```python
import webvtt
import datetime
filepath = '/home/subtitles.vtt'
builder = item.annotations.builder()
for caption in webvtt.read(filepath):
    h, m, s = caption.start.split(':')
    start_time = datetime.timedelta(hours=float(h), minutes=float(m), seconds=float(s)).total_seconds()
    h, m, s = caption.end.split(':')
    end_time = datetime.timedelta(hours=float(h), minutes=float(m), seconds=float(s)).total_seconds()

    builder.add(annotation_definition=dl.Subtitle(label='Speaker1',
                                                  text=caption.text),
                start_time=start_time,
                end_time=end_time)

item.annotations.upload(builder)
```

