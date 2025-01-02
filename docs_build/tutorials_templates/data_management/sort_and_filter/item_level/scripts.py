def section1():
    import dtlpy as dl
    # Get project and dataset
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Create filters instance
    filters = dl.Filters()
    # Filter only annotated items
    filters.add(field='annotated', values=True)
    # optional - return results sorted by ascending file name 
    filters.sort_by(field="filename")
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section2():
    filters = dl.Filters()
    # Filter all approved items
    filters.add(field='metadata.system.annotationStatus', values="approved")
    # AND filter items by their annotation - only items with 'box' annotations
    # Meaning you will get approved items with 'box' annotations
    filters.add_join(field='type', values='box')
    # optional - return results sorted by descending creation date 
    filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section3():
    filters = dl.Filters()  # filters with and
    filters.add(field='annotated', values=True, method=dl.FiltersMethod.AND)
    filters.add(field='metadata.user.is_automated', values=True,
                method=dl.FiltersMethod.AND)  # optional - return results sorted by ascending file name
    filters.sort_by(field='name')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section4():
    filters = dl.Filters()
    # filters with or
    filters.add(field='dir', values='/folderName1', method=dl.FiltersMethod.OR)
    filters.add(field='dir', values='/folderName2',
                method=dl.FiltersMethod.OR)  # optional - return results sorted by descending directory name
    filters.sort_by(field='dir', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section5():
    filters = dl.Filters()
    # For example -  filter only items in a specific folder - like 'dogs'
    filters.add(field='dir', values='/dogs')
    # For example - filter items by their annotation - only items with 'black' attribute
    filters.add_join(field='attributes', values='black')
    # to add filed BlackDogs to all filtered items and give value True
    # this field will be added to user metadata
    # create update order
    update_values = {'BlackDogs': True}
    # update
    pages = dataset.items.update(filters=filters, update_values=update_values)


def section6():
    filters = dl.Filters()
    # For example -  filter only annotated items
    filters.add(field='createdAt', values="2020-08-30T08:17:08.000Z")

    dataset.items.delete(filters=filters)


def section7():
    {
        "id": "5f4b60848ced1d50c3df114a",
        "datasetId": "5f4b603d9825b9f191bbd3b3",
        "createdAt": "2020-08-30T08:17:08.000Z",
        "dir": "/new_folder",
        "filename": "/new_folder/optional.jpg",
        "type": "file",
        "hidden": false,
        "metadata": {
            "system": {
                "originalname": "file",
                "size": 3290035,
                "encoding": "7bit",
                "mimetype": "image/jpeg",
                "annotationStatus": [
                    "completed"
                ],
                "refs": [
                    {
                        "type": "task",
                        "id": "5f4b61f8f81ab6238c331bd2"
                    },
                    {
                        "type": "assignment",
                        "id": "5f4b61f8f81ab60508331bd3"
                    }
                ],
                "executionLogs": {
                    "image-metadata-extractor": {
                        "default_module": {
                            "run": {
                                "5f4b60841b892d82eaa2d95b": {
                                    "progress": 100,
                                    "status": "success"
                                }
                            }
                        }
                    }
                },
                "exif": {},
                "height": 2734,
                "width": 4096,
                "statusLog": [
                    {
                        "status": "completed",
                        "timestamp": "2020-08-30T14:54:17.014Z",
                        "creator": "user@dataloop.ai",
                        "action": "created"
                    }
                ],
                "isBinary": true
            }
        },
        "name": "optional.jpg",
        "url": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a",
        "dataset": "https://gate.dataloop.ai/api/v1/datasets/5f4b603d9825b9f191bbd3b3",
        "annotationsCount": 18,
        "annotated": "discarded",
        "stream": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a/stream",
        "thumbnail": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a/thumbnail",
        "annotations": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a/annotations"
    }


def section8():
    filters = dl.Filters()
    filters.add_join(field='label', values='your_label_value')
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))


def section9():
    filters = dl.Filters()
    filters.add(field='metadata.system.annotationStatus', values=["completed", "approved"])
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section10():
    filters = dl.Filters()
    # set resource
    filters.add(field='metadata.system.annotationStatus', values="completed")
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section11():
    filters = dl.Filters()
    filters.add(field='metadata.system.annotationStatus', values=["completed"])
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section12():
    filters = dl.Filters()
    filters.add(field='metadata.system.refs', values=[])
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section13():
    filters = dl.Filters()
    filters.add(field='dir', values="/folderName")
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section14():
    filters = dl.Filters()
    filters.add(field='name', values='foo.bar.*')
    # Get filtered item list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))


def section15():
    filters = dl.Filters()
    filters.add(field='metadata.system.size', values='0', operator='gt')
    filters.add(field='metadata.system.size', values='5242880', operator='lt')
    filters.sort_by(field='filename', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
    # Get filtered item list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))


def section16():
    filters = dl.Filters()
    # set annotation resource
    filters.resource = dl.FiltersResource.ANNOTATION
    # return results sorted by descending label
    filters.sort_by(field='label', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
    filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
    # Get filtered item list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))


def section17():
    {
        "totalItemsCount": number,
        "items": Array,
        "totalPagesCount": number,
        "hasNextPage": boolean,
    }

    # A possible result:

    {
        "totalItemsCount": 2,
        "totalPagesCount": 1,
        "hasNextPage": false,
        "items": [
            {
                "id": "5d0783852dbc15306a59ef6c",
                "createdAt": "2019-06-18T23:29:15.775Z",
                "filename": "/5546670769_8df950c6b6.jpg",
                "type": "file"
                        // ...
            },
            {
                "id": "5d0783852dbc15306a59ef6d",
                "createdAt": "2019-06-19T23:29:15.775Z",
                "filename": "/5551018983_3ce908ac98.jpg",
                "type": "file"
                        // ...
            }
        ]
    }


def section18():
    filters = dl.Filters(custom_filter={"$and": [{"hidden": False},
                                                 {"type": "file"},
                                                 {"annotated": True}]},
                         )
    pages = dataset.items.list(filters=filters)
    print('Number of filtered items in dataset: {}'.format(pages.items_count))

def section19():
    filters = dl.Filters()
    filters.add(field='annotated', values=True)
    filters.open_in_web(dataset)
