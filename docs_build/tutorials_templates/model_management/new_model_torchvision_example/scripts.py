def one():
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


def two():
    from torchvision.io.image import read_image
    from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
    import dtlpy as dl

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


def three():
    project = dl.projects.get("Test Project")
    # Publish the dpk
    fasterrcnn_dpk = project.dpks.publish()
    # Install the app:
    project.apps.install(fasterrcnn_dpk)


def four():
    project = dl.projects.get("Test Project")
    model = project.models.get("fasterrcnn")  # From the manifest's models.name
    model.deploy()


def five():
    ex = model.predict(item_ids=['...'])
