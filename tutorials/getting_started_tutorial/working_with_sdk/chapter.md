rking with Dataloop SDK  
e SDK documents contain everything you need to know about the Dataloop SDK. Information is laid out in the following way:  
ties- contains information about the various entities and their related functions/operations and data. For example for “Item” entities - Download, Update (e.g. update its metadata), or update its status in task.  
sitories- A collection of entities, which are usually queried (e.g. using a filter), or referred to (for example all Items in a Dataset entity). It allows performing bulk operations (for example Delete all items), or addressing each entity within the repository (for example every Item in an Items collection).  
nation - We use pages instead of a list when we have an object that contains a lot of information. The page object divides a large list into pages (with a default of 1000 items) in order to save time when going over the entries. You can redefine the number of entries per page with the 'page_size' attribute.  
 going over all entries in a page out of multiple pages, we use nested loops to first go to the pages and then go over the entities for each page.  
  
ple 1 - populating pages with filter results and iterating through items.  
  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
# Get the project
project = dl.projects.get(project_name='project_name')
# Get the dataset
dataset = project.datasets.get(dataset_name='dataset_name')
# Get items in pages (100 item per page)
filters = dl.Filters()
filters.add(field='filename', values='/your/file/path.mimetype')
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
# Go over all item and print the properties
for page in pages:
    for item in page:
        item.print()
```
Example 2 - A Page entity iterator also allows reverse iteration for cases in which you want to change items during the iteration:  

```python
for page in reverse(pages):
    for item in page:
        item.print()
```
Example 3 - If you want to iterate through all items within your filter, you can also do so without going through them page by page:  

```python
for page in pages.all():
    for item in page:
        item.print()
```
Example 4 -  Iterator of Annotations  

```python
pages = dataset.annotations.list(filters=filters)
# Iterate through the annotations - Go over all annotations and print the properties
for page in pages:
    for annotation in page:
        print(annotation)
```
