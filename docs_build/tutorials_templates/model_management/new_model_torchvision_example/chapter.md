# Creating a Model Adapter for TorchVision's Faster R-CNN in Dataloop

## Introduction

In this tutorial, we'll walk you through the process of creating a model adapter for TorchVision's Faster R-CNN to make
it compatible with the Dataloop platform.
A model adapter allows you to integrate pre-trained models into the Dataloop ecosystem, making it easier to deploy and
manage your AI models.
This tutorial is based on torchvision example [here](https://pytorch.org/vision/stable/models.html#object-detection).

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

* Dataloop Account: You need an active Dataloop account to use the platform.
* Python: Install Python on your local machine.
* Dataloop SDK: Install the Dataloop SDK, which allows you to interact with Dataloop's API.
* TorchVision: Make sure you have TorchVision installed for working with Faster R-CNN models.

```shell
pip install torchvision
```

If you have any issues, click to get more information
about [Dataloop python env](https://developers.dataloop.ai/tutorials/getting_started/sdk_overview/chapter/#installing-prerequisite-software)
and about [torch](https://pytorch.org/get-started/locally/).

## Running Locally

To start, you can run your Faster R-CNN model locally to ensure it's functioning as expected:

* Set Up Dependencies: Install the required dependencies and libraries.
* create `main.py` file and copy the following code (make sure to replace the image path to a local one, you
  download [this file](https://raw.githubusercontent.com/dataloop-ai/dtlpy-documentation/142cea1f9e913b810d5f5425c8404cc105eb0e8b/assets/images/hamster.jpg)):

```python
from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image

img = read_image("/user/tst/image.jpg")

# Step 1: Initialize model with the best available weights
weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
model.eval()

# Step 2: Initialize the inference transforms
preprocess = weights.transforms()

# Step 3: Apply inference preprocessing transforms
batch = [preprocess(img)]

# Step 4: Use the model and visualize the prediction
prediction = model(batch)[0]
labels = [weights.meta["categories"][i] for i in prediction["labels"]]
box = draw_bounding_boxes(img, boxes=prediction["boxes"],
                          labels=labels,
                          colors="red",
                          width=4, font_size=30)
im = to_pil_image(box.detach())
im.show()
```

* Run the file. You should see the annotated image with the BB output of the model.

## Creating the Adapter

Now we will split it to our model adapter functions.
we will implement `load` adn `predict` and create the following adapter in `adapter.py`:

```python
from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
import dtlpy as dl


@dl.Package.decorators.module(description='Model Adapter for FasterRCNN object detection',
                              name='model-adapter',
                              init_inputs={'model_entity': dl.Model})
class FasterRCNNAdapter(dl.BaseModelAdapter):
    def load(self, local_path, **kwargs):
        # Step 1: Initialize model with the best available weights
        weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
        self.model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
        self.model.eval()

        # Step 2: Initialize the inference transforms
        self.preprocess = weights.transforms()

    def prepare_item_func(self, item: dl.Item):
        # Step 3: Apply inference preprocessing transforms
        img = read_image(item.download())
        return self.preprocess(img)

    def predict(self, batch, **kwargs):
        # Step 4: Use the model and visualize the prediction
        predictions = self.model(batch)
        batch_annotations = list()
        for pred in predictions:
            collection = dl.AnnotationCollection()
            for box, label, score in zip(pred["boxes"], pred["labels"], pred["scores"]):
                collection.add(annotation_definition=dl.Box(left=box[0],
                                                            top=box[1],
                                                            right=box[2],
                                                            bottom=box[3],
                                                            label=self.model_entity.id_to_label_map[label]),
                               model_info={'name': self.model_entity.name,
                                           'model_id': self.model_entity.id,
                                           'confidence': score})
            batch_annotations.append(collection)
        return batch_annotations


```

## Pushing to Dataloop

To integrate your model adapter into Dataloop:

1. Login to Dataloop: Use the sdk to log in to the platform - `dl.login()`.
2. Initialize Adapter Project: Create a new project or use an existing one.
3. Push Adapter to Dataloop: Use the Dataloop SDK to push your code in to a dl.Package.

```python
project = dl.projects.get('FasterRCNN Example')
weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
metadata = dl.Package.get_ml_metadata(cls=FasterRCNNAdapter,
                                      default_configuration={},
                                      output_type=dl.AnnotationType.BOX)
module = dl.PackageModule.from_entry_point(entry_point='adapter.py')
package = project.packages.push(package_name='faster-rcnn',
                                src_path=os.getcwd(),
                                package_type='ml',
                                modules=[module],
                                service_config={
                                    'runtime': dl.KubernetesRuntime(
                                        pod_type=dl.INSTANCE_CATALOG_REGULAR_M,
                                        autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                            min_replicas=0,
                                            max_replicas=1
                                        ),
                                        concurrency=1
                                    ).to_json()},
                                metadata=metadata
                                )
model = package.models.create(model_name='faster-rcnn',
                              description='faster-rcnn for object segmentation',
                              tags=['pretrained'],
                              scope='project',
                              status='trained',
                              configuration={
                                  'id_to_label_map': {i: x.tag for i, x in enumerate(weights.meta["categories"])},
                              },
                              project_id=project.id,
                              labels=weights.meta["categories"],
                              output_type='box',
                              input_type='image'
                              )
```

## Deploy the model

Finally, deploy and run your adapted Faster R-CNN model on the Dataloop platform:

```python
model.deploy()
```

Inference on Dataloop: Use the Dataloop platform to perform inference on your Faster R-CNN model and monitor its
performance.

```python
ex = model.predict(item_ids=[''])
```

## Conclusion

With this tutorial, you'll be able to create a model adapter for TorchVision's Faster R-CNN and seamlessly integrate it
into the Dataloop platform. Note that specific code implementation details are not included in this outline, but you can
provide code snippets or refer to official documentation as needed.




