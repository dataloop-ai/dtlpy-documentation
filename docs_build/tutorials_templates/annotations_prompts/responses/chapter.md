# Responses

The prompt responses are basically annotations in the platform.
We introduce those annotations type:

1. FreeText
2. RefImage
3. RefVideo (Not available yet)
4. RefAudio (Not available yet)

## FreeText

To upload text response for a prompt you need to connect the annotation to the prompt key:

```python
item = dl.items.get(item_id='<prompt item id>')
# add annotations
annotation_collection: dl.AnnotationCollection = item.annotations.builder()

annotation_collection.add(annotation_definition=dl.FreeText(text='My name is botman'),
                          prompt_id='prompt#1',
                          model_info={'name': 'llama2',
                                      'confidence': 0.96})
item.annotations.upload(annotation_collection)

```

## Image Response

This annotation type is used to annotate prompt text or input image with an output image.
For example, generative model receive a text input and generate an image.
This is how you can upload images as annotations to other items:

```python
import dtlpy as dl

item = dl.items.get(item_id='64f6e6010871e45536fc5e8f')
dataset = item.dataset
# upload the image you want to reference
output = dataset.items.upload(local_path=r"E:\TypesExamples\troy_and_abed.jpeg",
                              remote_path=f'/annotations/{item.id}')
# add annotations
annotation_collection: dl.AnnotationCollection = item.annotations.builder()

annotation_collection.add(annotation_definition=dl.RefImage(ref=output.id,
                                                            mimetype=output.mimetype),
                          prompt_id='prompt#2',
                          model_info={'name': 'stable-diffusion',
                                      'confidence': 0.96})
item.annotations.upload(annotation_collection)
```

Same structure could be applied for url reference:

```python
annotation_collection: dl.AnnotationCollection = item.annotations.builder()

annotation_collection.add(annotation_definition=dl.RefImage(
    ref='https://en.wikipedia.org/wiki/Pinky_and_the_Brain#/media/File:PinkyandtheBrain.Pinky.png',
    mimetype='image/png'),
                          prompt_id='prompt#2',
                          model_info={'name': 'stable-diffusion',
                                      'confidence': 0.96})
item.annotations.upload(annotation_collection)

```


