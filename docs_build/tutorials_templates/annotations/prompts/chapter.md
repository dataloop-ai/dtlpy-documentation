# Prompt Item

### What is a Prompt Item

Prompt item allows working with Dataloop's [RLHF studio](https://docs.dataloop.ai/docs/rlhf?highlight=RLHF).
It allows to edit and rate annotations, follow a conversation and choose between responses.

### SDK usage

The `dtlpy` SDK includes a class that connects the Dataloop platform with Vision Language Models (VLMs) and Large Language
Models (LLMs). This class provides an easy way to create, edit, and annotate Prompt items.

## Creating a Prompt by uploading a json file

We use prompts and conversations using json files. In those files you can create prompts of all kinds and add multiple
prompts to simulate a conversation.

Example for a json prompt file - to be supported on the RLHF studio:

```json

{
  "shebang": "dataloop",
  "metadata": {
    "dltype": "prompt"
  },
  "prompts": {
    "prompt#1": [
      {
        "mimetype": "application/text",
        "value": "please generate image of a donkey"
      }
    ]
  }
}
```

An example of a prompt containing both text and an image (change to your item id):

```json

{
  "shebang": "dataloop",
  "metadata": {
    "dltype": "prompt"
  },
  "prompts": {
    "1": [
      {
        "mimetype": "image/*",
        "value": "https://gate.dataloop.ai/api/v1/items/<item-id>/stream"
      },
      {
        "mimetype": "application/text",
        "value": "What's in these images?"
      }
    ]
  }
}
```

The `prompts` are a list to support multiple prompts in a single file.

Each prompt can contains multiple sections, e.g. text and image.

## Creating a Prompt via SDK

First we create a project and a dataset

```python
import dtlpy as dl
project = dl.projects.get(project_name='<project name>')
dataset = project.datasets.get(dataset_name='prompts')
```

Now we can create a single prompt with multiple elements. The name of the file is the PromptItem `name`:

```python
# Crteate a prompt item entity
prompt_item = dl.PromptItem(name='<your prompt item name>')

# Create the prompt with ID
prompt1 = dl.Prompt(key='<your-key>')
# Add a text component
prompt1.add_element(mimetype=dl.PromptType.TEXT, value='who are you')
# Add an image component
prompt1.add_element(mimetype=dl.PromptType.IMAGE, value=dl.items.get(item_id='64f5bd67a9163562961377f5').stream)

# Add the prompt to the promptItem
prompt_item.prompts.append(prompt)

```

For conversation, we can add multiple prompts with unique IDs:

```python

prompt2 = dl.Prompt(key='2')
prompt2.add_element(mimetype=dl.PromptType.TEXT, value='where are you from')
prompt2.add_element(mimetype=dl.PromptType.AUDIO, value='http://item.jpg')

# Add the second prompt to the prompt item
prompt_item.prompts.append(prompt2)
```

And just upload the prompt item:

```python
item: dl.Item = dataset.items.upload(prompt_item, overwrite=True)
```

You can upload prompt same as all other files/entities.
For example, using a list of prompts items:

```python
items = dataset.items.upload([prompts_item_1,
                              prompts_item_2,
                              prompts_item_3,
                              prompts_item_4])
```

Or an entire directory of prompts json files:

```python
items = dataset.items.upload('/user/prompts')
```

# Prompt Annotations (Responses)

The prompt responses are basically annotations in the platform.
We introduce those annotations type:

1. FreeText
2. RefImage
3. RefVideo (Not available yet)
4. RefAudio (Not available yet)

## FreeText

This annotation type is used to annotate prompt with a textual response.
To upload text response for a prompt you need to connect the annotation to the prompt key:

```python
item = dl.items.get(item_id='<prompt item id>')
prompt_item = dl.PromptItem.from_item(item)

# Add annotations
prompt_item.add(message={"role": "assistant",
                         "content": [{"mimetype": dl.PromptType.TEXT,
                                      "value": 'My name is botman'}]},
                model_info={'name': '<model name>',
                            'confidence': 1.0,
                            'model_id': '<model id>'})

```

## Image Response

This annotation type is used to annotate prompt text or input image with an output image.
For example, generative model receive a text input and generate an image.
This is how you can upload images as annotations to other items:

```python
import dtlpy as dl

item = dl.items.get(item_id='64f6e6010871e45536fc5e8f')
dataset = item.dataset
# Upload the image you want to reference
output = dataset.items.upload(local_path=r"E:\TypesExamples\troy_and_abed.jpeg",
                              remote_path=f'/annotations/{item.id}')
# Add annotations
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


