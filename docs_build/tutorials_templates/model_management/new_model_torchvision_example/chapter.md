# Building a Faster R-CNN Model: From PyTorch to Dataloop 🚀

Ever wanted to bring the power of PyTorch's Faster R-CNN to Dataloop? Let's build something awesome together! We'll transform a standard PyTorch model into a Dataloop-ready powerhouse.

## Before We Start 🎯

Let's get your workspace ready:

### What You'll Need 🧰
- 🔑 A Dataloop account (your gateway to AI awesomeness)
- 🐍 Python installed on your machine
- 📦 Dataloop SDK (`pip install dtlpy`)
- 🔥 TorchVision (`pip install torchvision`)

> 💡 **Quick Links**:
> - [Setting up Python for Dataloop](https://developers.dataloop.ai/tutorials/getting_started/sdk_overview/chapter/#installing-prerequisite-software)
> - [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)

## Test Drive: Running Locally 🏎️

Let's first test our model in its natural habitat. Create a file called `test_model.py`:

```python
from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image

def test_local_model(image_path):
    """Test Faster R-CNN locally"""
    print("🔄 Loading image and model...")
    
    # Load and prep the image
    img = read_image(image_path)
    
    # Get the best available weights
    weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
    model = fasterrcnn_resnet50_fpn_v2(
        weights=weights, 
        box_score_thresh=0.9
    )
    model.eval()
    
    # Prepare the image
    preprocess = weights.transforms()
    batch = [preprocess(img)]
    
    # Run prediction
    print("🎯 Running prediction...")
    prediction = model(batch)[0]
    
    # Visualize results
    labels = [weights.meta["categories"][i] for i in prediction["labels"]]
    box = draw_bounding_boxes(
        img, 
        boxes=prediction["boxes"],
        labels=labels,
        colors="red",
        width=4, 
        font_size=30
    )
    
    # Show the result
    im = to_pil_image(box.detach())
    im.show()
    print("✨ Done! Check out the visualized predictions!")

# Try it out!
test_local_model("/path/to/your/image.jpg")
```

> 🌟 **Pro Tip**: You can grab a test image [here](https://raw.githubusercontent.com/dataloop-ai/dtlpy-documentation/main/assets/images/hamster.jpg)

## Building the Dataloop Bridge: Model Adapter 🌉

Now let's create our model adapter - the magical translator between PyTorch and Dataloop. Create `adapter.py`:

```python
import dtlpy as dl
from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights

class FasterRCNNAdapter(dl.BaseModelAdapter):
    def load(self, local_path, **kwargs):
        """Load the model with its super-powers"""
        print('🚀 Initializing Faster R-CNN...')
        
        # Get the best weights
        self.weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
        self.model = fasterrcnn_resnet50_fpn_v2(
            weights=self.weights, 
            box_score_thresh=0.9
        )
        self.model.eval()
        
        # Setup preprocessing
        self.preprocess = self.weights.transforms()
        print('✅ Model loaded and ready!')

    def prepare_item_func(self, item: dl.Item):
        """Prepare items for the model"""
        print(f'🔄 Preparing item: {item.name}')
        img = read_image(item.download())
        return self.preprocess(img)

    def predict(self, batch, **kwargs):
        """Run predictions and return Dataloop annotations"""
        print(f'🎯 Running prediction on batch of {len(batch)} items')
        
        predictions = self.model(batch)
        batch_annotations = []
        
        for pred in predictions:
            collection = dl.AnnotationCollection()
            
            # Convert predictions to Dataloop annotations
            for box, label, score in zip(
                pred["boxes"], 
                pred["labels"], 
                pred["scores"]
            ):
                collection.add(
                    annotation_definition=dl.Box(
                        left=box[0],
                        top=box[1],
                        right=box[2],
                        bottom=box[3],
                        label=self.model_entity.id_to_label_map[label]
                    ),
                    model_info={
                        'name': self.model_entity.name,
                        'model_id': self.model_entity.id,
                        'confidence': score
                    }
                )
            batch_annotations.append(collection)
            
        print('✨ Predictions complete!')
        return batch_annotations
```

## Launching on Dataloop 🚀

### 1. Create Your Model DPK 📦

First, create a `dataloop.json` manifest file:

```json
{
    "name": "faster-rcnn",
    "displayName": "Faster R-CNN Object Detector",
    "version": "1.0.0",
    "scope": "public",
    "description": "State-of-the-art object detection using Faster R-CNN",
    "components": {
        "computeConfigs": [
            {
                "name": "default-config",
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
                "name": "rcnn-module",
                "entryPoint": "adapter.py",
                "className": "FasterRCNNAdapter",
                "computeConfig": "default-config"
            }
        ],
        "models": [
            {
                "name": "faster-rcnn",
                "moduleName": "rcnn-module",
                "configuration": {
                    "confidence_threshold": 0.9,
                    "batch_size": 4
                }
            }
        ]
    }
}
```

### 2. Deploy Your Model 🌟

```python
import dtlpy as dl

# Login to Dataloop
dl.login()

# Get your project
project = dl.projects.get("Your-Awesome-Project")

# Publish your DPK
print("📦 Publishing DPK...")
dpk = project.dpks.publish()

# Install the app
print("🔧 Installing app...")
project.apps.install(dpk=dpk)

# Get and deploy your model
print("🚀 Deploying model...")
model = project.models.get("faster-rcnn")
model.deploy()

print("✨ Your model is ready to rock!")
```

### 3. Test Your Model 🧪

```python
# Upload a test image
item = dataset.items.upload(
    'path/to/test/image.jpg'
)

# Run prediction
execution = model.predict(item_ids=[item.id])
execution.wait()

# Check results
print(f"🎯 Prediction status: {execution.status[-1]['status']}")
item.open_in_web()
```

## Pro Tips for Success 👑

1. **Performance Optimization** ⚡
   - Use GPU pods for faster inference
   - Batch your predictions when possible
   - Monitor memory usage

2. **Error Handling** 🛡️
   - Add proper logging
   - Handle edge cases
   - Validate inputs

3. **Best Practices** 📋
   - Version your model artifacts
   - Document configuration options
   - Test thoroughly before deployment

## Need Help? 🤝

- 🔍 Check the [full example on GitHub](https://github.com/dataloop-ai-apps/torch-models)
- 📚 Read our [Model Management docs](https://docs.dataloop.ai/docs/model-management-overview)

Happy modeling! May your predictions be accurate and your deployments smooth! 🚀
