# Responses

The prompt responses are basically annotations in the platform.
We introduce those annotations type:
1. FreeText
2. RefImage (WIP)
3. RefVideo (WIP)
4. RefAudio (WIP)

## Usage

To upload text response for a prompt you need to connect the annotation to the prompt key:

```python
item = dl.datasets.get(item_id='<prompt item id>')
# add annotations
annotation_collection: dl.AnnotationCollection = item.annotations.builder()

annotation_collection.add(annotation_definition=dl.FreeText(text='My name is botman'),
                          prompt_id='prompt#1',
                          model_info={'name': 'llama2',
                                      'confidence': 0.96})
item.annotations.upload(annotation_collection)

```

For now ,we only support text annotation. soon all mimetypes will be available as prompt annotations
