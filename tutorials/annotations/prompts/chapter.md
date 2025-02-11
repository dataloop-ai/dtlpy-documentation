# 💬 Prompt Annotations - Where Conversations Come to Life!

Welcome to the world of prompt annotations! Think of prompts as digital conversations - they can include text, images, and even audio. Let's explore how to create and manage these interactive elements!

# 🎯 Getting Started with Prompts

## Understanding Prompt Structure
Prompts in Dataloop are stored as JSON files with a specific structure. Here's a simple example:

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
				"value": "Please generate an image of a donkey"
			}
		]
	}
}
```

## Multimodal Prompts
Want to combine text and images? Here's how:

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

# 🛠️ Creating and Managing Prompts

## Project Setup
First, let's set up our environment:

```python
import dtlpy as dl

# Get your project and dataset ready
project = dl.projects.get(project_name='<project name>')
dataset = project.datasets.get(dataset_name='<dataset name>')
```

## Creating a Single Prompt
Let's create a prompt with both text and image:

```python
# Create a prompt item
prompt_item = dl.PromptItem(name='my-first-prompt')

# Create a prompt with a unique key
prompt1 = dl.Prompt(key='conversation-1')

# Add text component
prompt1.add_element(
	mimetype=dl.PromptType.TEXT, 
	value='Who are you?'
)

# Add image component
prompt1.add_element(
	mimetype=dl.PromptType.IMAGE, 
	value=dl.items.get(item_id='your-image-id').stream
)

# Add the prompt to the prompt item
prompt_item.prompts.append(prompt1)
```

## Building Conversations
Create a sequence of prompts to simulate a conversation:

```python
# Add another prompt to continue the conversation
prompt2 = dl.Prompt(key='conversation-2')
prompt2.add_element(
	mimetype=dl.PromptType.TEXT, 
	value='Where are you from?'
)

# Add audio element (if needed)
prompt2.add_element(
	mimetype=dl.PromptType.AUDIO, 
	value='http://audio-file.mp3'
)

# Add to the same prompt item
prompt_item.prompts.append(prompt2)

# Upload the complete prompt item
item = dataset.items.upload(prompt_item, overwrite=True)
```

## Batch Upload
Need to upload multiple prompts? We've got you covered:

```python
# Upload multiple prompt items at once
items = dataset.items.upload([
	prompts_item_1,
	prompts_item_2,
	prompts_item_3,
	prompts_item_4
])

# Or upload an entire directory of prompt JSON files
items = dataset.items.upload('/user/prompts')
```

# 📝 Working with Responses (Annotations)

## Response Types
Dataloop supports various types of responses:
- FreeText: For text responses
- RefImage: For image references
- RefVideo: For video references (Coming soon!)
- RefAudio: For audio references (Coming soon!)

## Adding Text Responses
Here's how to add a text response to a prompt:

```python
# Get your prompt item
item = dl.items.get(item_id='<prompt item id>')
prompt_item = dl.PromptItem.from_item(item)

# Add a text response
prompt_item.add(
    prompt_key='<prompt key>',
	message={
		"role": "assistant",
		"content": [{
			"mimetype": dl.PromptType.TEXT,
			"value": 'My name is botman'
		}]
	},
	model_info={
		'name': 'gpt-4',
		'confidence': 1.0,
		'model_id': 'model-123'
	}
)
```

## Adding Image Responses
Want to respond with an image? Here's how:

```python
# First, upload the response image
image = dataset.items.upload(
	local_path="path/to/response.jpg",
	remote_path=f'/annotations/{item.id}'
)

# Add the image response to the prompt item
prompt_item.add(
    prompt_key='<prompt key>',
	message={
		"role": "assistant",
		"content": [{
			"mimetype": dl.PromptType.IMAGE,
			"value": dl.items.get(item_id=image.id).stream
		}]
	},
	model_info={
		'name': 'gpt-4o-mini',
		'confidence': 1.0,
		'model_id': '<model id>'
	}
)

```

## Using External Image URLs
You can also reference external images:

```python

# Add the image response to the prompt item
prompt_item.add(
    prompt_key='<prompt key>',
	message={
		"role": "assistant",
		"content": [{
			"mimetype": dl.PromptType.IMAGE,
			"value":"https://example.com/image.png"
		}]
	},
	model_info={
		'name': 'gpt-4o-mini',
		'confidence': 1.0,
		'model_id': '<model id>'
	}
)
```

# 💡 Pro Tips

## Best Practices
- Use meaningful prompt keys for easy tracking
- Keep prompt structures consistent
- Include metadata for better organization
- Handle multimodal content appropriately

## Quality Control
- Validate JSON structure before uploading
- Check response associations
- Monitor model confidence scores
- Keep track of conversation flow

## Performance Optimization
- Batch upload when possible
- Use appropriate mimetypes
- Optimize image sizes
- Consider response caching

Need help? Check out our other tutorials or reach out to our support team. Happy prompting! 💭✨


