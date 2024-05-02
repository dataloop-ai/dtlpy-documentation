# Model Adapter Class Methods

In this tutorial, we can see the flowcharts for the Model Adapter functiions. There are two main types of functions:

* **Wrapper Functions**: Those are functions that come as part of the ```BaseModelAdapter``` class and perform most of the auxiliary tasks needed for adapting a machine learning model to the Dataloop format.
* **User Functions**: Each wrapper function will call a user function, i.e. a function implemented by the user in their ```ModelAdapter``` with the specific code related to the model they wish to adapt.

In the following sections we will see explanations for each function of each category.

## Wrapper Functions

Here we will see the flowcharts explaining the logic of the wrapper functions. The blocks in green show operations performed by the wrapper function, while blocks in yellow show a call to a user function, which will require implementation.

### `load_from_model`

This function is used to download model artifacts and load them to model object so it will be ready to be used for training and inference.

```mermaid
flowchart TD
    id1(load_from_model)-->
    id2("download artifacts @ \nlocal_path=~/.dataloop/models/{model.name}")-->
    id3("load(local_path)")
    style id1 fill:#adebad, stroke:black
    style id2 fill:#adebad, stroke:black
    style id3 fill:#ffff99, stroke:red
    click id3 "./#load"
```

The ```load_from_model``` function performs starts by downloading artifacts as seen in the ```download_artifacts``` block. It will define the variable ```local_path``` to the path ```~/.dataloop/models/{model.name}``` where ```{model.name}``` will be filled with the name of the model as defined during its creation. Inside this directory, the ```model.artifacts``` will be downloaded. Those usually include weight files, but can include any other auxiliary files needed by the model that were uploaded by the user. More information at [this page](https://developers-dev.redoc.ly/tutorials/model_management/introduction/chapter/#artifacts-and-codebase).

Once all files are in ```local_path``` the user function ```load``` is invoked. Its explanation can be found [below](#load).

The directory structure will be, considering that ```~/.dataloop``` is the default ```DATALOOP_PATH```:

```shell
Directory tree at this stage:
DATALOOP_PATH
|-- models
|   |-- model.name
|      |-- artifacts
```

### `save_to_model`

This function saves the current model files and uploads them as artifacts.

```mermaid
flowchart TD
    id1("save_to_model")-->
    id2("save(local_path)")-->
    id3("upload artifact @ \nlocal_path/*")
    style id1 fill:#adebad, stroke:black
    style id2 fill:#ffff99, stroke:red
    style id3 fill:#adebad, stroke:black
    click id2 "./#save"
```


The ```save_to_model``` function invokes the ```save``` user function explained [below](#save) and then uploads all the files in ```local_path``` as model artifacts, as described [here](https://developers-dev.redoc.ly/tutorials/model_management/introduction/chapter/#artifacts-and-codebase).

### `predict_items`

This function receives a list of items over which the model will need to perform predictions and create annotations.

```mermaid
flowchart TD
    id1(predict_items)-->
    id2(i_batch = next batch start)-->
    id3("batch = items[i: (i+batch_size)]")-->
    id4("prepare_item_func")-->
    id5("annotation = predict(batch)")-->
    id6("upload batch_collections for batch_items")-->
    id7("Is last batch?")
    id8("return items and annotations list")
    id7 -->|No| id3
    id7 -->|Yes| id8
    style id1 fill:#adebad, stroke: black
    style id2 fill:#adebad, stroke: black
    style id3 fill:#adebad, stroke: black
    style id4 fill:#ffff99, stroke: red
    style id5 fill:#ffff99, stroke: red
    style id6 fill:#adebad, stroke: black
    style id7 fill:#adebad, stroke: black
    style id8 fill:#adebad, stroke: black
    click id4 "./#prepare_item_func"
    click id5 "./#predict"
```

The ```predict_items``` function will prepare batches of items with ```batch_size``` being defined in the model's configurations. For each batch it will call [```prepare_item_func```](#prepare_item_func) which will preprocess the batch's items before they can be used as input to the model in the [```predict(batch)```](#predict) which will have the predictions stored in ```annotation```. The annotations are then stored in ```batch_collections``` and uploaded as annotations for all the items in the batch.

Once the predictions are performed over all the items in all the batches, the function returns a list of items and another list with their respective annotations.

### `train_model`

When running a training session from the model adapter, we start by calling the `train_model` wrapper function so the model can learn according to the data provided to it in its creation.

```mermaid
flowchart TD
    id1(train_model)-->
    id2(load_from_model)-->
    id3(prepare_data)-->
    id4("train(data_path, out_path)")-->
    id5(save_to_model)-->
    id6(cleanup)
    style id1 fill:#adebad, stroke: black
    style id2 fill:#adebad, stroke: black
    style id3 fill:#adebad, stroke: black
    style id4 fill:#ffff99, stroke: red
    style id5 fill:#adebad, stroke: black
    style id6 fill:#adebad, stroke: black
    click id2 "./#load_from_model"
    click id4 "./#train"
    click id5 "./#save_to_model"
```

Train model starts by [loading the model](#load_from_model), prepares the data by downloading it according to the directory structure shown below. It then invokes the [```train```](#train) function implemented by the user and saves the result of training by calling [```save_to_model```](#save_to_model). Lastly, it does a ```cleanup``` by deleting all the local copies of the dataset files used for training.

When creating the model, train and validation subsets should be defined for the dataset as shown [here](https://developers.dataloop.ai/tutorials/model_management/create_new_model_ui/chapter/#creating-a-model-from-a-public-architecture). The ```prepare_data``` function will create the directory structure shown below and in the ```data_path``` it will download the training data in the directories seen in this schema. The data will be divided according to the model's subset filters, and ```items``` will hold the data items themselves while ```json``` has the annotation jsons associated to each item. Keep that in mind when preprocessing the data in the ```train``` function.

```shell
Directory tree at convert_from_dtlpy (supposing train and validation subsets):
-- DATALOOP_PATH
   |-- models
   |   |-- model.name
   |      |-- artifacts
   |-- model_data
       |-- model.id_model.name
           |-- timestamp (root_path)
               |-- output (out_path)
               |-- datasets
                   |-- dataset.id (data_path)
                       |-- train
                       |   |-- items
                       |   |   |-- train_dir (from filter)
                       |   |-- json
                       |       |-- train_dir (from filter)
                       |-- validation
                           |-- items
                           |   |-- val_dir (from filter)
                           |-- json
                               |-- val_dir (from filter)

```
### `evaluate_model`

This function generates predictions for a whole test set provided to it and then creates metrics that will be uploaded to Dataloop platform.

```mermaid
flowchart TD
    id1(evaluate_model)-->
    id2(load_from_model)-->
    id3(predict_dataset)-->
    id4("evaluate")
    style id1 fill:#adebad, stroke: black
    style id2 fill:#adebad, stroke: black
    style id3 fill:#adebad, stroke: black
    style id4 fill:#ffff99, stroke: red
    click id2 "./#load_from_model"
    click id3 "./#predict_items"
    click id4 "./#evaluate"
```

It starts by invoking [```load_from_model```](#load_from_model) so it has the latest model artifacts and then calls ```predict_dataset``` which in turn calls ```predict_items``` for a whole dataset and a filter provided, which should determine a test set for this dataset. Finally, ```evaluate``` will compute metrics by comparing the model's predictions with the ground truth present in the test set.

## User Function

Those are the function that users must implement in order to run the model. For only prediction, must implement `load` and `predict`. For training - `train` and `save` are also required.

### `load`
After the wrapper function download all the model artifact to the local directory, users must implement this function to load the model (using the local files and the model config) and instantiate the model.

### `save`
Users need to implement this function to dump the model state to a local directory, e.g. `torch.save(model.state_dict(), PATH)`
After that, the wrapper function will take care of the rest and will upload the files into the platform, update the model config, and save everything on to the model entity

### `train`
This function is called the wrapper function loads the model, downloads and prepare the data.
Now everything is ready locally and this function implements the actual model training.
When this is done, there's no need to do anything - the wrapper will take care of the saving and uploading.

### `predict`
This function is called the load model, so now we have the model ready to predict.
Each item goes through the `prepare_item_func` and a batch is ready to predict.
After the model prediction, user will need to prepare the annotation is the Dataloop format using the DL annotations.

### `prepare_item_func`
Prepares each item for prediction. Bt default, images will be downloaded and loaded into a ndarray as a batch (NHWC)
