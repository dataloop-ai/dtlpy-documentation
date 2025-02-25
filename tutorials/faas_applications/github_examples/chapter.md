# 🌟 Real-World DPK Examples

Welcome to our showcase of real-world FaaS applications! Let's explore how Dataloop's serverless functions are being used in production environments. These examples are drawn from our [public apps repository](https://github.com/dataloop-ai-apps) and demonstrate the power and flexibility of FaaS.

## 🤖 AI Model Integration Examples

### ResNet Model Integration
The [torch-models](https://github.com/dataloop-ai-apps/torch-models/) repository provides ready-to-use model adapters for popular PyTorch architectures. The ResNet-50 adapter is perfect for image classification tasks and can be easily fine-tuned on your custom datasets. To use it:
1. Install the torch-models app from the Dataloop Marketplace
2. Get the installed model:
```python
# list the models in the project
models = project.models.list().print()

# get the model
model = project.models.get('-model-name')
```

2. Fine-tune on your dataset by connecting it to the model and initiating training.

### Faster R-CNN Object Detection
The [fasterrcnn-adapter](https://github.com/dataloop-ai-apps/fasterrcnn-adapter) provides a production-ready implementation of the Faster R-CNN model for object detection. Key features include:
- Pre-trained model support
- Custom training configuration
- Polygon annotation support
- Batch prediction capabilities
- GPU acceleration

The adapter is particularly useful for:
- Object detection in complex scenes
- Transfer learning on custom datasets
- Real-time inference applications

### CLIP Model Integration
From our [clip-model-adapter](https://github.com/dataloop-ai-apps/clip-model-adapter), here's how to implement zero-shot image classification:

```python
import torch
from PIL import Image
import dtlpy as dl
from transformers import CLIPProcessor, CLIPModel

class ServiceRunner(dl.BaseServiceRunner):
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.model.to(self.device)
    
    def classify_item(self, item: dl.Item, candidate_labels: list):
        # Download and process image
        image = Image.open(item.download(save_locally=False))
        inputs = self.processor(
            images=image,
            text=candidate_labels,
            return_tensors="pt",
            padding=True
        ).to(self.device)
        
        # Get prediction
        outputs = self.model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1)
        
        # Add classification
        builder = item.annotations.builder()
        builder.add(
            annotation_definition=dl.Classification(
                label=candidate_labels[probs.argmax().item()],
                confidence=float(probs.max().item())
            )
        )
        item.annotations.upload(builder)
```

## 🔄 Integration Examples

### GCS Export Service
Based on [export-gcs](https://github.com/dataloop-ai-apps/export-gcs), here's how to export annotations to Google Cloud Storage:

```python
import dtlpy as dl
from google.cloud import storage

class ServiceRunner(dl.BaseServiceRunner):
    def __init__(self):
        self.client = storage.Client()
    
    def export_annotations(self, dataset: dl.Dataset, bucket_name: str):
        # Get bucket
        bucket = self.client.get_bucket(bucket_name)
        
        # Export annotations for each item
        for item in dataset.items.list():
            # Get annotations
            annotations = item.annotations.list()
            
            # Convert to desired format
            export_data = self._format_annotations(annotations)
            
            # Upload to GCS
            blob = bucket.blob(f"annotations/{item.id}.json")
            blob.upload_from_string(
                data=json.dumps(export_data),
                content_type='application/json'
            )
    
    def _format_annotations(self, annotations):
        # Implement annotation formatting logic
        pass
```

## 💡 Key Takeaways

1. **Integration Flexibility**
   - FaaS seamlessly integrates with popular AI frameworks
   - Easy to incorporate external services (GCS, AWS, etc.)
   - Support for both synchronous and asynchronous processing

2. **Scalability**
   - Automatic scaling for model inference
   - Efficient handling of large datasets
   - Resource optimization through containerization

3. **User Experience**
   - Custom UI integration for complex workflows
   - Real-time monitoring and feedback
   - Intuitive toolbar integration

4. **Best Practices**
   - Use appropriate compute resources for AI models
   - Implement proper error handling and logging
   - Consider caching for frequently used models
   - Monitor service performance and costs

## 🚀 Next Steps

Ready to build your own FaaS applications? Here are some resources to help you get started:

1. Check out our [GitHub repository](https://github.com/dataloop-ai-apps) for more examples
2. Join our developer community for support and discussions
3. Explore our model adapters for quick AI integration
4. Try implementing these examples in your own projects

Need help? Our support team is always ready to assist you in building production-ready FaaS applications! Happy coding! ✨
