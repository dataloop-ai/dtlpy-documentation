def section1():
    import dtlpy as dl
    # Get project and dataset
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Create filters instance with annotation resource
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    # Filter example - only note annotations
    filters.add(field='type', values='note')
    # optional - return results sorted by descending label 
    filters.sort_by(field='label', value=dl.FiltersOrderByDirection.DESCENDING)
    pages = dataset.annotations.list(filters=filters)
    # Count the annotations
    print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
    # Iterate through the annotations - Go over all annotations and print the properties
    for page in pages:
        for annotation in page:
            annotation.print()


def section2():
    # Create filters instance
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    # Filter all box annotations
    filters.add(field='type', values='box')
    # AND filter annotations by their items - only items that are of mimetype image
    # Meaning you will get 'box' annotations of all image items
    filters.add_join(field='metadata.system.mimetype', values="image*")
    # optional - return results sorted by descending creation date
    filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
    # Get filtered annotations list in a page object
    pages = dataset.annotations.list(filters=filters)
    # Count the annotations
    print('Number of filtered annotations in dataset: {}'.format(pages.items_count))


def section3():
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    # set annotation resource
    filters.add(field='type', values='box', method=dl.FiltersMethod.AND)
    filters.add(field='label', values='car',
                method=dl.FiltersMethod.AND)  # optional - return results sorted by ascending creation date
    filters.sort_by(field='createdAt')
    # Get filtered annotations list
    pages = dataset.annotations.list(filters=filters)
    # Count the annotations
    print('Number of filtered annotations in dataset: {}'.format(pages.items_count))


def section4():
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    # filters with or
    filters.add(field='type', values='/box', method=dl.FiltersMethod.OR)
    filters.add(field='type', values='/point',
                method=dl.FiltersMethod.OR)  # optional - return results sorted by descending updated date
    filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
    # Get filtered annotations list
    pages = dataset.annotations.list(filters=filters)
    # Count the annotations
    print('Number of filtered annotations in dataset: {}'.format(pages.items_count))


def section5():
    filters = dl.Filters()
    # set annotation resource
    filters.resource = dl.FiltersResource.ANNOTATION
    # Example - created on 30/8/2020 at 8:17 AM
    filters.add(field='createdAt', values="2020-08-30T08:17:08.000Z")
    dataset.annotations.delete(filters=filters)


def section6():
    {
        "id": "5f576f660bb2fb455d79ffdf",
        "datasetId": "5e368bee106a76a61cf05282",
        "type": "segment",
        "label": "Planet",
        "attributes": [],
        "coordinates": [
            [
                {
                    "x": 856.25,
                    "y": 1031.2499999999995
                },
                {
                    "x": 1081.25,
                    "y": 1631.2499999999995
                },
                {
                    "x": 485.41666666666663,
                    "y": 1735.4166666666665
                },
                {
                    "x": 497.91666666666663,
                    "y": 1172.9166666666665
                }
            ]
        ],
        "metadata": {
            "system": {
                "status": null,
                "startTime": 0,
                "endTime": 1,
                "frame": 0,
                "endFrame": 1,
                "snapshots_": [
                    {
                        "fixed": true,
                        "type": "transition",
                        "frame": 0,
                        "objectVisible": true,
                        "data": [
                            [
                                {
                                    "x": 856.25,
                                    "y": 1031.2499999999995
                                },
                                {
                                    "x": 1081.25,
                                    "y": 1631.2499999999995
                                },
                                {
                                    "x": 485.41666666666663,
                                    "y": 1735.4166666666665
                                },
                                {
                                    "x": 497.91666666666663,
                                    "y": 1172.9166666666665
                                }
                            ]
                        ],
                        "label": "Planet",
                        "attributes": []
                    }
                ],
                "automated": false,
                "isOpen": false,
                "system": false
            },
            "user": {}
        },
        "creator": "user@dataloop.ai",
        "createdAt": "2020-09-08T11:47:50.576Z",
        "updatedBy": "user@dataloop.ai",
        "updatedAt": "2020-09-08T11:47:50.576Z",
        "itemId": "5f572f4423a69b8c83408f12",
        "url": "https://gate.dataloop.ai/api/v1/annotations/5f576f660bb2fb455d79ffdf",
        "item": "https://gate.dataloop.ai/api/v1/items/5f572f4423a69b8c83408f12",
        "dataset": "https://gate.dataloop.ai/api/v1/datasets/5e368bee106a76a61cf05282",
        "hash": "11fdc816804faf0f7266b40d1cb67aff38e5c10d"
    }


def section7():
    filters = dl.Filters()
    # set resource
    filters.resource = dl.FiltersResource.ANNOTATION
    filters.add(field='label', values='your_label_value')
    pages = dataset.annotations.list(filters=filters)
    # Count the annotations
    print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
