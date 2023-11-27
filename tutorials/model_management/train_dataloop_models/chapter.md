## Tutorial: using models from the AI library  
  
Model algorithms that are ready for use out-of-the-box are available in the Dataloop AI Library. The AI library contains various algorithms and pretrained models that can be used for inferencing or fine-tuning via additional training on your custom datasets.  
  
This tutorial will cover how to use AI library models for:  
  
- predicting from pretrained models, and  
- fine-tuning training on a custom dataset.  
  
To see available AI library models, filter all available packages to view those with a “public” scope:  
  

```python
filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
filters.add(field='scope', values='public')
dl.models.list(filters=filters).print()
```
### Clone and deploy a model  
  
Get the model and package you want and copy it to your project.  
  
Only models that are trained (i.e. model.status = 'trained') can be deployed. Since the AI library model is pre-trained (i.e. model status is 'trained'), it can be deployed directly.  
  

```python
public_model = dl.models.get(model_id="<model_id>")
model = project.models.clone(from_model=public_model,
                             model_name='remote_model',
                             project_id=project.id)
model.deploy()
```
### Train on a custom dataset  
  
If you would like to customize the AI library model (for transfer-learning or fine-tuning), you can indicate the new dataset and labels you want to use for model training.  
  

```python
custom_model = dl.models.clone(from_model=public_model,
                               model_name='remote_custom_model',
                               dataset=dataset,
                               project_id=project.id,
                               labels=['label1', 'label2'])
```
  
#### Dataset subsets  
Our AI library models require a train/validation split of the dataset for the training session. To avoid data leakage between training sessions and to make each training reproducible, we will determine the data subsets and save the split type to the dataset entity (using a DQL). Using DQL filters you can subset the data however you like.  
  
For example, if your dataset is split between folders, you can use this DQL to add metadata for all items in the dataset  

```python
dataset.metadata['system']['subsets'] = {
    'train': json.dumps(dl.Filters(field='dir', values='/train').prepare()),
    'validation': json.dumps(dl.Filters(field='dir', values='/validation').prepare()),
}
dataset.update(system_metadata=True)
```
This way, when the training starts, the sets will be downloaded using the DQL and any future training session on this dataset will have the same subsets of data.  
  
NOTE: In the future, this mechanism will be expanded to use a tagging system on items. This will allow more flexible data subsets and random data allocation.  
  
To train the model on your custom data, simply use the `model.train()` function and wait for the training to finish. You can monitor the training progress on the platform or via the python SDK. To see the updated model status, retrieve the model again from the platform.  
  

```python
custom_model.train()
custom_model = dl.models.get(model_id=custom_model.id)
print(custom_model.status)
```
#### Deploying the model  
  
Once the model is trained, it can be deployed as a service. The `model.deploy()` function automatically creates a bot and service for the trained model.  
  
Once you have a model deployed, you can create a UI slot to inference on individual data items on the platform, or call the model to inference in a FaaS or pipelines.  

```python
custom_model.deploy()
```
### Predict on a single item  
  
Once a model is deployed, you can predict on items using the `model.predict()` function. The function returns an execution object that can be used to track whether the prediction execution was successful. If successful, the annotations will be uploaded to the item directly and can be viewed in the annotation studio.  
  
If you have just deployed the model, `get` the model again to get the updated model metadata that includes the deployment information.  
  

```python
model = dl.models.get(model_id=model.id)
model.predict(item_ids=[item.id])
```
