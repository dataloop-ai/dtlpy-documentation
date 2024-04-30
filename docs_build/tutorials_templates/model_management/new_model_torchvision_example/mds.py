def one():
    """
    # Creating a Model Adapter for TorchVision's Faster R-CNN in Dataloop

    ## Introduction

    In this tutorial, we'll walk you through the process of creating a model adapter for TorchVision's Faster R-CNN to make it compatible with the Dataloop platform.
    A model adapter allows you to integrate pre-trained models into the Dataloop ecosystem, making it easier to deploy and manage your AI models.
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

    If you have any issues, click to get more information about [Dataloop python env](https://developers.dataloop.ai/tutorials/getting_started/sdk_overview/chapter/#installing-prerequisite-software) and about [torch](https://pytorch.org/get-started/locally/).

    ## Running Locally

    To start, you can run your Faster R-CNN model locally to ensure it's functioning as expected:

    * Set Up Dependencies: Install the required dependencies and libraries.
    * create `main.py` file and copy the following code (make sure to replace the image path to a local one, you
      download [this file](https://raw.githubusercontent.com/dataloop-ai/dtlpy-documentation/142cea1f9e913b810d5f5425c8404cc105eb0e8b/assets/images/hamster.jpg)):
    """


def two():
    """

    * Run the file. You should see the annotated image with the BB output of the model.

    ## Creating the Adapter

    Now we will split it to our model adapter functions.
    we will implement `load` adn `predict` and create the following adapter in `adapter.py`:
    """


def three():
    """

    ## Pushing to Dataloop

    To integrate your model adapter into Dataloop:

    1. Login to Dataloop: Use the sdk to log in to the platform - `dl.login()`.
    2. Initialize Adapter Project: Create a new project or use an existing one -- we will call it 'Test Project' here.
    3. Create the `dataloop.json` manifest that specifies the app that will run the module. More information on apps and their manifests can be found [here](https://developers.dataloop.ai/tutorials/applications/introduction/chapter/). Here follows an example of manifest used for FasterRCNN:

    ```json
    {
      "name": "fasterrcnn",
      "displayName": "FasterRCNN",
      "version": "0.1.13",
      "scope": "public",
      "description": "FasterRCNN application for object detection",
      "attributes": {
        "Provider": "PyTorch",
        "License": "BSD-3.0",
        "Category": "Model",
        "Computer Vision": "Semantic Segmentation",
        "Media Type": "Image"
      },
      "codebase": {
        "type": "git",
        "gitUrl": "https://github.com/dataloop-ai-apps/fasterrcnn-adapter",
        "gitTag": "0.1.13"
      },
      "components": {
        "computeConfigs": [
          {
            "name": "fasterrcnn-deploy",
            "versions": {
              "dtlpy": "1.89.11"
            },
            "runtime": {
              "podType": "regular-xs",
              "concurrency": 1,
              "autoscaler": {
                "type": "rabbitmq",
                "minReplicas": 0,
                "maxReplicas": 2,
                "queueLength": 100
              },
              "preemptible": false
            }
          },
          {
            "name": "fasterrcnn-train-evaluate",
            "versions": {
              "dtlpy": "1.89.11"
            },
            "runtime": {
              "podType": "gpu-t4",
              "concurrency": 1,
              "autoscaler": {
                "type": "rabbitmq",
                "minReplicas": 0,
                "maxReplicas": 2,
                "queueLength": 100
              },
              "preemptible": false,
              "executionTimeout": 36000000
            }
          }
        ],
        "modules": [
          {
            "name": "fasterrcnn-module",
            "entryPoint": "model_adapter.py",
            "className": "FasterRCNNAdapter",
            "computeConfig": "fasterrcnn-deploy",
            "description": "FasterRCNN Segmentation Module",
            "initInputs": [
              {
                "type": "Model",
                "name": "model_entity"
              }
            ],
            "functions": [
              {
                "name": "evaluate_model",
                "computeConfig": "fasterrcnn-train-evaluate",
                "input": [
                  {
                    "type": "Model",
                    "name": "model",
                    "description": "Dataloop Model Entity"
                  },
                  {
                    "type": "Dataset",
                    "name": "dataset",
                    "description": "Dataloop Dataset Entity"
                  }
                ],
                "output": [
                  {
                    "type": "Model",
                    "name": "model",
                    "description": "Dataloop Model Entity"
                  },
                  {
                    "type": "Dataset",
                    "name": "dataset",
                    "description": "Dataloop Dataset Entity"
                  }
                ],
                "displayName": "Evaluate a Model",
                "displayIcon": "",
                "description": "Function to evaluate FasterRCNN Segmentation model performance"
              },
              {
                "name": "predict_items",
                "input": [
                  {
                    "type": "Item[]",
                    "name": "items",
                    "description": "List of items to run inference on"
                  }
                ],
                "output": [
                   {
                     "type": "Item[]",
                     "name": "items",
                     "description": "The same input images for prediction."
                   },
                   {
                     "type": "Annotation[]",
                     "name": "annotations",
                     "description": "The predicted annotations."
                   }
                ],
                "displayName": "Predict Items",
                "displayIcon": "",
                "description": "Function to run FasterRCNN Segmentation inference on items"
              },
              {
                "name": "predict_dataset",
                "input": [
                  {
                    "type": "Dataset",
                    "name": "dataset",
                    "description": ""
                  },
                  {
                    "type": "Json",
                    "name": "filters",
                    "description": "Dataloop Filter DQL"
                  }
                ],
                "output": [],
                "displayName": "Predict Dataset",
                "displayIcon": "",
                "description": "Function to run FasterRCNN inference on a dataset"
              },
              {
                "name": "train_model",
                "computeConfig": "fasterrcnn-train-evaluate",
                "input": [
                  {
                    "type": "Model",
                    "name": "model",
                    "description": "Dataloop Model Entity"
                  }
                ],
                "output": [
                  {
                    "type": "Model",
                    "name": "model",
                    "description": "Dataloop Model Entity"
                  }
                ],
                "displayName": "Train a Model",
                "displayIcon": "",
                "description": "Function to train FasterRCNN Segmentation model"
              }
            ]
          }
        ],
        "models": [
          {
            "name": "fasterrcnn",
            "moduleName": "fasterrcnn-module",
            "scope": "project",
            "status": "pre-trained",
            "configuration": {
              "weights_filename": "weights/best.pth",
              "batch_size": 12,
              "num_epochs": 25,
              "id_to_label_map": {
                    "0": "person",
                    "1": "..."
                }
            },
            "inputType": "image",
            "outputType": "box",
            "supportedMethods": {
              "load": true,
              "predict": true,
              "train": true,
              "evaluate": true
            },
            "description": "State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations. ",
            "labels": [
              "person",
              "..."
            ]
          }
        ]
      }
    }
    ```
    the labels have been cut short to save space, but the full manifest includes 80 labels.

    4. Use the command line tool to install the app, running it from the model project directory:

    ```bash
    dlp app publish --project-name "Test Project"
    ```

    """


def four():
    """

    ## Deploy the model

    Finally, deploy and run your adapted Faster R-CNN model on the Dataloop platform:

    """


def five():
    """
    Inference on Dataloop: Use the Dataloop platform to perform inference on your Faster R-CNN model and monitor its performance.
    """


def six():
    """

    ## Conclusion

    With this tutorial, you'll be able to create a model adapter for TorchVision's Faster R-CNN and seamlessly integrate it into the Dataloop platform. Note that specific code implementation details are not included in this outline, but you can provide code snippets or refer to official documentation as needed.
    """
