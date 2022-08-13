# Modalities  
Modalities are multiple layers representing the same reality/scene. For example multiple sensors for the same image/object. In the Dataloop system there’s the main item, and other items relating to it are set as modality layers, saved in its metadata.  
## Setup  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```
## Set a single modality  
In the following example, Item2 is defined as a modality for the main item, item1  
  

```python
# Get the first item (main)
item1 = dataset.items.get(item_id='your-item-id')
# Get the second item
item2 = dataset.items.get(item_id='your-item-id')
# Create modality
item1.modalities.create(name='your-modality-name',
                        modality_type=dl.ModalityTypeEnum.OVERLAY,
                        ref=item2.id)
# Update item to apply changes to platform
item1.update()
```
## Upload multiple modalities  
Start by creating a JSON layout for your items and save it as modalities_layout.json. Use item paths for files stored locally on your machine or URLs for linked items.  
We use the dictionary key for the main item, and value will be a list of the modalities (local or URL for each item):  

```python
{
    "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9": [
        "https://images.unsplash.com/photo-1543852786-1cf6624b9987",
        "https://images.unsplash.com/photo-1561948955-570b270e7c36"
    ],
    "/home/items/primary/dogs/dog1.png": [
        "/home/items/modalities/dogs/dog1-mod1.png",
        "/home/items/modalities/dogs/dog1-mod2.png"
    ]
}
```
Use the following code to upload items and set as modalities based on the JSON you created (or any other dictionary).  
We use a Threaded pool to upload and create the modalities faster  
  

```python
import os
import dtlpy as dl
import json
from concurrent.futures import ThreadPoolExecutor
def upload_single(dataset, source, modalities):
    # Upload main item. If it's not a local image - create a URL Link
    if not os.path.isfile(source):
        source = dl.UrlLink(ref=source)
    main_item: dl.Item = dataset.items.upload(local_path=source)
    # Upload the modalities. If it's not a local image - create a URL Link
    modalities = [modality if os.path.isfile(modality) else dl.UrlLink(ref=modality) for modality in modalities]
    modalities_items = dataset.items.upload(local_path=modalities, remote_path='/modalities')
    # create the modalities references
    for modality_item in modalities_items:
        main_item.modalities.create(modality_type=dl.ModalityTypeEnum.OVERLAY,
                                    ref=modality_item.id,
                                    name='{}:{}'.format(modality_item.name, modality_item.id))
    main_item.update(system_metadata=True)
def main():
    with open('/home/project/images/modalities.json', 'r') as f:
        modalities_layout = json.load(f)
    # Run the following script to upload the modalities
    with ThreadPoolExecutor(max_workers=32) as executor:
        for source, modalities in modalities_layout.items():
            executor.submit(upload_single,
                            dataset=dataset,
                            source=source,
                            modalities=modalities)
    executor.shutdown()
if __name__ == "__main__":
    main()
```
Run the main() function to start the run  

```python
main()
```
