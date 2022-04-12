## Pagination  
### Pages  
We use pages instead of a list when we have an object that contains a lot of information.  
  
The page object divides a large list into pages (with a default of 1000 items) in order to save time when going over the items.  
  
It is the same as we display it in the annotation platform, see example <a href="https://dataloop.ai/docs/organize-dataset#datastructuredisplay" target="_blank">here</a>.  
  
You can redefine the number of items on a page with the page_size attribute.  
When we go over the items we use nested loops to first go to the pages and then go over the items for each page.  
  
### Iterator of Items  
You can create a generator of items with different filters.  
  

```python
import dtlpy as dl
# Get the project    
project = dl.projects.get(project_name='project_name')
# Get the dataset
dataset = project.datasets.get(dataset_name='dataset_name')
# Get items in pages (1000 item per page)
filters = dl.Filters()
filters.add(field='filename', values='/your/file/path.mimetype')
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
# Go over all item and print the properties
for i_page, page in enumerate(pages):
    print('{} items in page {}'.format(len(page), i_page))
    for item in page:
        item.print()
```
A Page entity iterator also allows reverse iteration for cases in which you want to change items during the iteration:  
  

```python
# Go over all item and print the properties
for i_page, page in enumerate(reversed(pages)):
    print('{} items in page {}'.format(len(page), i_page))
```
If you want to iterate through all items within your filter, you can also do so without going through them page by page:  
  

```python
for item in pages.all():
    print(item.name)
```
If you are planning to do some process on each item, it's faster to use multi-threads (or multi-process) for parallel computation.  
The following uses ThreadPoolExecutor with 32 workers to process parallel batches of 32 items:  
  

```python
from concurrent.futures import ThreadPoolExecutor
def single_item(item):
    # do some work on item
    print(item.filename)
    return True
with ThreadPoolExecutor(max_workers=32) as executor:
    executor.map(single_item, pages.all())
```
Lets compare the runtime to see that now the process is faster:  
  

```python
from concurrent.futures import ThreadPoolExecutor
import time
tic = time.time()
for item in pages.all():
    # do stuff on item
    time.sleep(1)
print('One by one took {:.2f}[s]'.format(time.time() - tic))
def single_item(item):
    # do stuff on item
    time.sleep(1)
    return True
tic = time.time()
with ThreadPoolExecutor(max_workers=32) as executor:
    executor.map(single_item, pages.all())
print('Using threads took {:.2f}[s]'.format(time.time() - tic))
```
Visualizing the progress with tqdm progress bar:  

```python
import tqdm
pbar = tqdm.tqdm(total=pages.items_count)
def single_item(item):
    # do stuff on item
    time.sleep(1)
    pbar.update()
    return True
with ThreadPoolExecutor(max_workers=32) as executor:
    executor.map(single_item, pages.all())
```
### Set page_size  
The following example sets the page_size to 50:  

```python
# Create filters instance
filters = dl.Filters()
# Get filtered item list in a page object, where the starting page is 1
pages = dataset.items.list(filters=filters, page_offset=1, page_size=50)
# Count the items
print('Number of filtered items in dataset: {}'.format(pages.items_count))
# Print items from page 1
print('Length of first page: {}'.format(len(pages.items)))
```
