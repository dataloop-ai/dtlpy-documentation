# Using Saved Filters  
  
You can easily list, load and save any saved filters from the UI in the SDK  
  
## Save  
Create any dl.Filter and save it to the saved filters. After saving you can load the same filter from the Data Browser  
  

```python
import dtlpy as dl
project = dl.projects.get('My Project')
filters = dl.Filters()
# Create items filters
filters.add(field='dir', values='/first')
# Add annotations filters
filters.add_join(field='label', values='cat')
# Save
filters.save(project=project, filter_name='only label cat')
```
## List  
List all the saved filters from a project:  
  

```python
import dtlpy as dl
project = dl.projects.get('My Project')
saved_filters_list = dl.Filters.list(project=project)
print(saved_filters_list)
```
## Load  
Using any saved filter name from the list above, you can load and create a new dl.Filter object:  
  

```python
import dtlpy as dl
project = dl.projects.get('My Project')
# Load a saved filter
filters = dl.Filters.load(project=project, filter_name='only label cat')
# Print the filter or use it to list the items in a dataset
filters.print()
```
