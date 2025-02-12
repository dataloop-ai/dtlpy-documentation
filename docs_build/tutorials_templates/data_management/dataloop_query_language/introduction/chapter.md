# Introduction to Dataloop Query Language (DQL) 🔍

Welcome to the world of DQL! Whether you're searching through millions of items, filtering annotations, or managing metadata, DQL is your Swiss Army knife for data manipulation in Dataloop.

## What is DQL? 🤔

The [Dataloop Query Language](https://docs.dataloop.ai/docs/api-dql) is a powerful tool that lets you:
- Filter through massive amounts of data 🎯
- Sort results in any order you need 📊
- Update metadata across multiple items ✏️

## Understanding Filters 🎯

Think of filters as your data sieve - they help you find exactly what you need in your datasets.

### Anatomy of a Filter

Every filter has two main components:
* **Field**: What you're filtering by (e.g., 'dir' for directory)
* **Value**: What you're looking for (e.g., '/new_folder')

### Basic Filtering Operations ⚡

Let's start with a simple example - finding all annotated items in a dataset:

```python
import dtlpy as dl

# Get project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')

# Create filters instance
filters = dl.Filters()

# Filter only annotated items
filters.add(field='annotated', values=True)

# Optional: Sort results by filename
filters.sort_by(field="filename")

# Get filtered items
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items')
```

### Advanced Filtering: Annotations 🎨

Want to filter items based on their annotations? Here's how:

```python
filters = dl.Filters()

# Find all approved items
filters.add(field='metadata.system.annotationStatus', values="approved")

# AND find only items with box annotations
filters.add_join(field='type', values='box')

# Optional: Sort by creation date (newest first)
filters.sort_by(
    field='createdAt',
    value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING
)

# Get results
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items')
```

## Logical Operators in Filters 🔄

### AND Operations

The AND operator is your default friend - use it to combine multiple conditions:

```python
filters = dl.Filters()

# Find items that are:
filters.add(
    field='annotated',
    values=True,
    method=dl.FiltersMethod.AND  # This is default, you can skip it
)

# AND have specific metadata
filters.add(
    field='metadata.user.is_automated',
    values=True,
    method=dl.FiltersMethod.AND
)

# Optional: Sort by name
filters.sort_by(field='name')

# Get results
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items')
```

### OR Operations

Need items that match any of your conditions? Use OR:

```python
filters = dl.Filters()

# Find items in either folder
filters.add(
    field='dir',
    values='/folderName1',
    method=dl.FiltersMethod.OR
)
filters.add(
    field='dir',
    values='/folderName2',
    method=dl.FiltersMethod.OR
)

# Optional: Sort by directory (descending)
filters.sort_by(
    field='dir',
    value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING
)

# Get results
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items')
```

## Working with Filtered Results 🛠️

### Updating Metadata

Need to update metadata for filtered items? Here's how:

```python
filters = dl.Filters()

# Find items in 'dogs' folder
filters.add(field='dir', values='/dogs')

# With 'black' attribute
filters.add_join(field='attributes', values='black')

# Update metadata
update_values = {'BlackDogs': True}  # Will be added to user metadata
pages = dataset.items.update(
    filters=filters,
    update_values=update_values
)
```

### Deleting Filtered Items

Be careful with this one - it's powerful but permanent:

```python
filters = dl.Filters()

# Find items by creation date
filters.add(field='createdAt', values="2020-08-30T08:17:08.000Z")

# Delete them
dataset.items.delete(filters=filters)
```

## Working with Pages 📄

When dealing with large datasets, Dataloop uses pagination to efficiently manage and process data. Instead of loading everything at once (which could be slow and memory-intensive), data is divided into pages.

### Understanding Pages 📚

By default, Dataloop returns pages with up to 1000 items each. You can:
- Navigate through pages one by one
- Customize the page size
- Use iterators for easy access
- Reverse iterate through pages (useful when modifying items)

Here's how to work with pages:

```python
# Create filters instance
filters = dl.Filters()

# Get filtered items in pages (default 1000 items per page)
pages = dataset.items.list(filters=filters)

# Print total count
print(f'Total items: {pages.items_count}')

# Method 1: Iterate through pages
for i_page, page in enumerate(pages):
    print(f'Page {i_page} has {len(page)} items')
    for item in page:
        print(f'Processing item: {item.name}')

# Method 2: Use the all() iterator
for item in pages.all():
    print(f'Processing item: {item.name}')

# Method 3: Reverse iteration (useful when modifying items)
for i_page, page in enumerate(reversed(pages)):
    print(f'Processing page {i_page} in reverse')
```

### Customizing Page Size ✂️

Need a different page size? No problem:

```python
# Get items with custom page size
pages = dataset.items.list(
    filters=filters,
    page_size=50,
    page_offset=0  # Start from first page
)

print(f'Items in first page: {len(pages.items)}')
```

### Parallel Processing with Pages 🚀

For faster processing, you can use multiple threads. Let's compare the runtime difference:

```python
from concurrent.futures import ThreadPoolExecutor
import tqdm
import time

# Single-threaded processing
tic = time.time()
for item in pages.all():
    # Your processing logic here
    time.sleep(1)  # Simulate work
print(f'Sequential processing took {time.time() - tic:.2f}[s]')

# Multi-threaded processing
def process_item(item):
    # Your processing logic here
    time.sleep(1)  # Simulate work
    return True

# Create a progress bar
pbar = tqdm.tqdm(total=pages.items_count)

# Process items in parallel
tic = time.time()
with ThreadPoolExecutor(max_workers=32) as executor:
    for item in executor.map(process_item, pages.all()):
        pbar.update()
print(f'Parallel processing took {time.time() - tic:.2f}[s]')
```

## Working with Saved Filters 💾

Need to reuse your filters across different sessions or share them with team members? Saved filters have got you covered!

### Saving Filters

Create and save your filters to use them later in both SDK and UI:

```python
import dtlpy as dl
project = dl.projects.get('My Project')

# Create your filter
filters = dl.Filters()
# Filter items in a specific directory
filters.add(field='dir', values='/first')
# AND with specific annotation label
filters.add_join(field='label', values='cat')

# Save for later use
filters.save(project=project, filter_name='only label cat')
```

### Listing Saved Filters

Want to see all available saved filters? Easy:

```python
import dtlpy as dl
project = dl.projects.get('My Project')

# List all saved filters
saved_filters_list = dl.Filters.list(project=project)
print(saved_filters_list)
```

### Loading Saved Filters

Need to use a previously saved filter? Here's how:

```python
import dtlpy as dl
project = dl.projects.get('My Project')

# Load a saved filter
filters = dl.Filters.load(project=project, filter_name='only label cat')

# Print the filter or use it
filters.print()
```

## Understanding Item and Annotation Fields 📝

When filtering, you can access any field in the item's JSON structure. 
Go to the [Item Fields](https://docs.dataloop.ai/docs/item-fields) page for more information.

## Understanding Filter Responses 📊

When you run a DQL query, here's what you get back:

```python
{
    "totalItemsCount": 2,  # Total number of matching items
    "totalPagesCount": 1,  # Number of pages
    "hasNextPage": False,  # Whether there are more pages
    "items": [
        {
            "id": "5d0783852dbc15306a59ef6c",
            "createdAt": "2019-06-18T23:29:15.775Z",
            "filename": "/5546670769_8df950c6b6.jpg",
            "type": "file"
            // ... more item fields ...
        },
        // ... more items ...
    ]
}
```


💡 **Pro Tip**: Use dot notation to access nested fields. For example:
- `metadata.system.originalname` for the original filename
- `metadata.user.myField` for custom metadata

## Best Practices 💫

1. **Be Specific**: The more specific your filters, the faster the query
2. **Use Indexing**: Common filter fields are indexed for better performance
3. **Batch Operations**: When updating/deleting, use filters to work in batches
4. **Test First**: Always test your filters with a small dataset first
5. **Check Results**: Verify your filter results before performing updates or deletes

## Need More Help? 🤔

- Check out our [DQL Documentation](https://docs.dataloop.ai/docs/api-dql) for more details
- Explore the [Filters API](https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters)
- For advanced filtering, visit our [Advanced SDK Filters](tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md) guide

Happy querying! 🚀
