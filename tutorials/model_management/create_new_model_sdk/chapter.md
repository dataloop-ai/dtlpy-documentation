# Building Your Own Model: The DIY Guide 🛠️

Ready to bring your own model to the Dataloop platform? Let's build something amazing together! This guide will show you how to create your custom model adapter and get your model running smoothly on our platform.

## Choose Your Path: SDK or UI 🛤️

You've got two ways to bring your model to life in Dataloop:

### Option 1: Using the SDK (This Guide) 💻
Follow along with this guide to create your model programmatically using our Python SDK.

### Option 2: Using the Dataloop UI 🖥️

Prefer a more visual approach? You can use the [Dataloop UI](https://docs.dataloop.ai/docs/models-overview#using-the-dataloop-ui) to create and integrate your model. Here's how:

1. **Connect Your Docker Registry** 🐳
   - Link your container registry:
     * [AWS ECR](https://docs.dataloop.ai/docs/aws-elastic-container-registry)
     * [Google Container Registry (GCR)](https://docs.dataloop.ai/docs/google-container-registry)
     * [Google Artifact Registry (GAR)](https://docs.dataloop.ai/docs/google-artifacts-registry)

2. **Create Your Model Application** 🎨
   - Navigate to the [Model Marketplace](https://docs.dataloop.ai/docs/marketplace-applications#how-to-create-an-application)
   - Create a new application
   - Link your Docker image:
     * Provide the image URL
     * Connect it to your application
     * Enable predictions, training, and workflow capabilities

Now, let's dive into the SDK approach! 🚀

## The Model Adapter: Your Bridge to Dataloop 🌉

Think of the model adapter as a translator between your model and Dataloop. It's like teaching your model to speak our language! Let's create one:

```python
import dtlpy as dl
import torch
import os
class SimpleModelAdapter(dl.BaseModelAdapter):
    def load(self, local_path, **kwargs):
        """Load your model from saved weights"""
        print('🔄 Loading model from:', local_path)
        self.model = torch.load(os.path.join(local_path, 'model.pth'))

    def predict(self, batch, **kwargs):
        """Run predictions on a batch of data"""
        print(f'🎯 Predicting batch of size: {len(batch)}')
        
        # Get model predictions
        preds = self.model(batch)
        
        # Convert predictions to Dataloop format
        batch_annotations = list()
        for i_img, predicted_class in enumerate(preds):
            # Create a collection for each image
            image_annotations = dl.AnnotationCollection()
            
            # Add predictions as classifications
            image_annotations.add(
                annotation_definition=dl.Classification(label=predicted_class),
                model_info={'name': self.model_name}
            )
            batch_annotations.append(image_annotations)
            
        return batch_annotations
```

> 💡 **Pro Tip**: Check out our [ResNet adapter example](https://github.com/dataloop-ai-apps/torch-models/blob/main/adapters/resnet/resnet_adapter.py) on GitHub for a production-ready implementation!

## Publishing Your Model App 🚀

### 1. Create Your Manifest File 📝

First, you'll need a manifest file - think of it as your app's ID card. Here's a template:

```json
{
    "name": "my-awesome-model",
    "displayName": "My Awesome Model",
    "version": "1.0.0",
    "scope": "project",
    "description": "A fantastic model that does amazing things!",
    "codebase": {
        "type": "git",
        "gitUrl": "https://github.com/your-repo/your-model",
        "gitTag": "v1.0.0"
    },
    "components": {
        "computeConfigs": [
            {
                "name": "inference-service",
                "runtime": {
                    "podType": "regular-xs",
                    "concurrency": 1,
                    "autoscaler": {
                        "type": "rabbitmq",
                        "minReplicas": 0,
                        "maxReplicas": 2,
                        "queueLength": 100
                    }
                }
            }
        ],
        "modules": [
            {
                "name": "model-module",
                "entryPoint": "model_adapter.py",
                "className": "Adapter",
                "computeConfig": "inference-service"
            }
        ],
        "models": [
            {
                "name": "my-model",
                "moduleName": "model-module",
                "configuration": {
                    "weights_filename": "weights.pth",
                    "batch_size": 4,
                    "confidence_threshold": 0.25
                }
            }
        ]
    }
}
```

### 2. Publish Your App 🎉

Time to share your creation with the world (or at least your project)!

```python
# Get your project
project = dl.projects.get(project_name="your-awesome-project")
# Publish your app
dpk = project.dpks.publish()
```

### 3. Install Your App 📦

#### Option A: Through the UI 🖥️
1. Go to Models Marketplace
2. Find your app
3. Click "Install" - Done! ✨

#### Option B: Using Python 🐍
```python
# Get your project
project = dl.projects.get(project_name="your-awesome-project")
# Get your app's DPK
dpk = project.dpks.get(dpk_name='my-awesome-model')
# Install it!
app = project.apps.install(dpk=dpk)
```

## Upload Your Model Weights 🏋️‍♂️

Now let's give your model its superpowers:

```python
# Get your project and model
project = dl.projects.get(project_name="your-awesome-project")
model = project.models.get("my-model")

# Upload your weights
artifact = model.artifacts.upload(filepath='/path/to/weights.pth')

# Update the configuration
model.configuration['weights_filename'] = artifact.filename

# Deploy your model
model.deploy()
```

## Testing Your Model 🧪

### Method 1: Using the UI 🖥️
1. Go to the "Deployed" tab
2. Find your model
3. Click the "Test" tab
4. Drag & drop an image
5. Click "Test" and watch the magic happen! ✨

### Method 2: Using Python 🐍
```python
# Get your model and test item
model = dl.models.get(model_id='your-model-id')
item = dl.items.get(item_id='your-test-item-id')

# Run prediction
execution = model.predict(item_ids=[item.id])

# Wait for results
execution.wait()
execution = dl.executions.get(execution_id=execution.id)

# Check the status
print(f"Prediction status: {execution.status[-1]['status']}")
```

## Training Your Model 🎓

Time to teach your model some new tricks! Let's add training capabilities to your model adapter:

```python
class SimpleModelAdapter(dl.BaseModelAdapter):
    def train(self, data_path, **kwargs):
        """Train your model on Dataloop dataset"""
        print('🎯 Starting training with data from:', data_path)
        
        # Get training parameters from configuration
        epochs = self.configuration.get('epochs', 10)
        batch_size = self.configuration.get('batch_size', 32)
        learning_rate = self.configuration.get('learning_rate', 0.001)
        
        # Setup training
        train_dataset = self.load_data(data_path)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)
        criterion = torch.nn.CrossEntropyLoss()
        
        # Training loop
        for epoch in range(epochs):
            running_loss = 0.0
            for i, batch in enumerate(train_dataset):
                # Zero the gradients
                optimizer.zero_grad()
                
                # Forward pass
                outputs = self.model(batch['images'])
                loss = criterion(outputs, batch['labels'])
                
                # Backward pass and optimize
                loss.backward()
                optimizer.step()
                
                # Print statistics
                running_loss += loss.item()
                if i % 100 == 99:
                    print(f'🔄 Epoch {epoch + 1}, Batch {i + 1}: Loss = {running_loss / 100:.3f}')
                    running_loss = 0.0
                    
            
        print('🎉 Training completed!')
        
    def save(self, local_path):
        """Save model checkpoint"""
        checkpoint = {
            'model_state_dict': self.model.state_dict(),
            'configuration': self.configuration
        }
        checkpoint_path = os.path.join(local_path, f'checkpoint.pth')
        torch.save(checkpoint, checkpoint_path)
        print(f'💾 Saved checkpoint: {checkpoint_path}')
```

To train your model:


```python
# Get your model
parent_model = project.models.get('my-model')

# Get the dataset
dataset = project.datasets.get(dataset_name='my-ground-truth')

# Clone the model
model = parent_model.clone(model_name='my-model-trained',
                           dataset=dataset)

# Set training configuration
model.configuration.update({
    'epochs': 20,
    'batch_size': 32,
    'learning_rate': 0.001,
    'optimizer': 'adam'
})

# Start training
model.train()
```

> 🔥 **Important Note**: If you want your model to include annotations that were generated by a model in the training subsets, you must set "include_model_annotations": True in the model configuration. This ensures that both manually created and AI-generated annotations are considered during training.

> 💡 **Pro Tip**: Always monitor your training metrics! Add logging and validation steps to track your model's progress.

## Export The Weights 🎯

Once your model is trained and ready, it's time to export those precious weights! Here's how:


```python
# Get the model
model = project.models.get('my-model-trained')
# Download everything
model.artifacts.download(local_path='./my-model-trained')
```

## Best Practices for Weight Management 📋

1. **Version Control** 🔄
   - Use semantic versioning for your weights
   - Keep a changelog of training modifications
   - Store training parameters with weights

2. **Validation** ✅
   - Test exported weights before deployment
   - Verify model performance after loading
   - Keep validation metrics for comparison

3. **Documentation** 📝
   - Record training parameters
   - Note any preprocessing requirements
   - Document expected input/output formats

> 🔥 **Hot Tip**: Always keep a backup of your best performing weights!

## Troubleshooting Tips 🔍

If something's not working as expected:

1. **Check Service Status** 🚦
   - Make sure your model service is up and running
   - Look for the green light in the services page

2. **Check the Logs** 📋
   - Go to "Model Management" > "Deployed" tab
   - Click on the "Executions" number
   - Look for the paper icon to view logs

3. **Common Issues** ⚠️
   - Timeouts: Your service might need more resources
   - Memory errors: Try reducing batch size
   - Missing dependencies: Check your requirements.txt

## Ready to Rock? 🎸

You've just created your own custom model in Dataloop! Remember:
- Test thoroughly before deployment
- Monitor your model's performance
- Keep your weights and code in sync
- Document any special requirements

Happy modeling! 🚀

> 🎓 **Need More Help?** Check our [documentation](https://docs.dataloop.ai)