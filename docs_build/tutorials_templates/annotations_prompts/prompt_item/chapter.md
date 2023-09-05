# Prompt Item

We use prompts and conversations using json files. In those files you can create prompts of all kinds and add multiple prompts to simulate a conversation.
Example for a json prompt file:
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

The `prompts` are a list to support multiple prompts in a single file.

Each prompt can contains multiple sections, e.g. text and image.

## Creating a Prompt

First we creat a project and a dataset
```python
project = dl.projects.get('COCO ors')
dataset = project.datasets.get('prompts')
```

Now we create a single prompt with multiple elements. The name of the file is the PromptItem `name`:
```python
# crteate a prompt item entity
prompts = dl.PromptItem(name='conversation_#1')

# create the prompt with ID
prompt1 = dl.Prompt(key='prompt#1')
# add a text component
prompt1.add(mimetype=dl.PromptType.TEXT, value='who are you')
# add an image component
prompt1.add(mimetype=dl.PromptType.IMAGE, value=dl.items.get(item_id='64f5bd67a9163562961377f5').stream)

# add the prompt to the promptItem
prompts.add(prompt=prompt1)
```

For conversation, we can add multiple prompts with unique IDs:

```python

prompt2 = dl.Prompt(key='2')
prompt2.add(mimetype=dl.PromptType.TEXT, value='where are you from')
prompt2.add(mimetype=dl.PromptType.AUDIO, value='http://item.jpg')

# add the second prompt to the prompt item
prompts.add(prompt=prompt2)
```

And just upload the prompt item:
```python
item: dl.Item = dataset.items.upload(prompts, overwrite=True)
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
