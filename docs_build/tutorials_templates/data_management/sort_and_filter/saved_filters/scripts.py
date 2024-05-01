def section1():
    import dtlpy as dl
    project = dl.projects.get('My Project')
    filters = dl.Filters()
    # Create items filters
    filters.add(field='dir', values='/first')
    # Add annotations filters
    filters.add_join(field='label', values='cat')
    # Save
    filters.save(project=project, filter_name='only label cat')


def section2():
    import dtlpy as dl
    project = dl.projects.get('My Project')
    saved_filters_list = dl.Filters.list(project=project)
    print(saved_filters_list)


def section3():
    import dtlpy as dl
    project = dl.projects.get('My Project')
    # Load a saved filter
    filters = dl.Filters.load(project=project, filter_name='only label cat')
    # Print the filter or use it to list the items in a dataset
    filters.print()
