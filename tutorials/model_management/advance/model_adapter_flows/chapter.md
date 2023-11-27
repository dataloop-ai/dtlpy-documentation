# Wrappers Functions

## `load_from_model`
```mermaid
flowchart TD
    id1(load_from_model)-->
    id2(create local_path\ndefault @\nDATALOOP_PATH/models/model.name)-->
    id3(download model artifacts @ local_path)-->
    id4("load(local_path)")-->
    id5(save_model)
```

```shell
Directory tree at this stage:
DATALOOP_PATH
|-- models
|   |-- model.name
|      |-- artifacts
```
## `save_to_model`
```mermaid
flowchart TD
    id1("save_to_model")-->
    id2("save(local_path)")-->
    id3("upload artifact @ local_path/*")

```
## `prdict_items`

```mermaid
flowchart LR
    id1(predict_items)-->
    id2(i_batch = next batch start)-->
    id3("batch = items[i: (i+batch_size)]")-->
    id4("prepare_item_func")-->
    id5("annotation = predict(batch)")-->
    id6("upload batch_collections for batch_items")-->
    id7("Is last batch?")
    id8("done")
    id7 -->|Yes| id3
    id7 -->|No| id8

```

## `train_model`

When running a training session from the model adapter, we start by calling the `train_model` wrapper function

```mermaid
flowchart TD
    id1(train_model)-->
    id2(load_from_model)-->
    id3(prepare_data)-->
    id4("train(data_path, out_path)")-->
    id5(save_model)-->
    id6(cleanup)
    click id2 "./#load-from-model"

```

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
# `evaludate_model`
```mermaid
flowchart TD
    id1(evaluate_model)-->
    id2(load_from_model)-->
    id3(predict_dataset)-->
    id4("evaluate")

```

# User Function

## `load`
After the wrapper function download all the model artifact to the local directory, users must implement this function to load the model (using the local files and the model config) and instantiate the model.

## `save`
Users need to implement this function to dump the model state to a local directory, e.g. `torch.save(model.state_dict(), PATH)`
After that, the wrapper function will take care of the rest and will upload the files into the platform, update the model config, and save everything on to the model entity

## `train`
This function is called the wrapper function loads the model, downloads and prepare the data.
Now everything is ready locally and this function implements the actual model training.
When this is done, there's no need to do anything - the wrapper will take care of the saving and uploading.

## `predict`
This function is called the load model, so now we have the model ready to predict.
Each item goes through the `prepare_item_func` and a batch is ready to predict.
After the model prediction, user will need to prepare the annotation is the Dataloop format using the DL annotations.

## `prepare_item_func`
Prepares each item for prediction. Bt default, images will be downloaded and loaded into a ndarray as a batch (NHWC)
