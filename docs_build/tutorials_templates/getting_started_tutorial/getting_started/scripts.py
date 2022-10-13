import dtlpy as dl


def func3():
    dl.login()


def func4():
    if dl.token_expired():
        dl.login()


def func5():
    import dtlpy as dl
    # use browser login to create the bot
    dl.login()
    project = dl.projects.get(project_name='myProject')  # get your project
    my_bot = project.bots.create(name='my-unique-name', return_credentials=True)


def func6():
    print("the bot email is " + my_bot.email)
    print("the bot password is " + my_bot.password)


def func7():
    import dtlpy as dl
    # Login to Dataloop platform
    dl.login_m2m(email=email, password=password)


def func8():
    project = dl.projects.create(project_name='my-new-project')
    project = dl.projects.get(project_name='my-project')


def func9():
    project.datasets.create(dataset_name='my-dataset-name')
    dataset = project.datasets.get(dataset_name='my-dataset-name')


def func10():
    dataset.items.upload(local_path="/path/to/image.jpg")
    # Upload items to a specific folder in the dataset
    dataset.items.upload(local_path="/path/to/image.jpg", remote_path="/path/to/dataset/folder")


def func11():
    # Get a single item
    item = dataset.items.get(item_id='my_item_Id')

    # Get all items and iterate through them
    pages = dataset.items.list()
    # Go over all item and print the properties
    for page in pages:
        for item in page:
            item.print()


def func12():
    # Filter all items with an annotation that has a label in the list
    filters = dl.Filters()
    # Filter items with dog OR cat labels
    filters.add_join(field='label', values=['dog', 'cat'], operator=dl.FILTERS_OPERATIONS_IN)
    # optional - return results sorted by ascending file name
    filters.sort_by(field='filename')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def func13():
    item.metadata['user'] = dict()
    item.metadata['user']['MyKey'] = 'MyValue'
    item.update()


def func14():
    # Upload box annotation
    builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100, label='labelName'))
    item.annotations.upload(builder)


def func15():
    mask = np.zeros(shape=(item.height, item.width), dtype=np.uint8)
    mask[50:100, 200:250] = 1
    builder.add(annotation_definition=dl.Segmentation(geo=mask, label='label1'))


def func16():
    # getting the item
    item = dl.items.get(item_id='item_id')
    # now getting the items annotations list
    for ann in item.annotations.list():
        print(ann)

    # we can also get only annotated items from a dataset then print out the annotations that were created by a
    # specific user.
    dataset = dl.datasets.get(dataset_id='dataset_id')
    # creating the annotated items filter
    ItemFilter = dl.Filters()
    ItemFilter.add(field='annotated', values=True)
    # creating the annotation level filter
    annotation_filter = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    annotation_filter.add(field='creator', values='sewar.d@dataloop.ai')
    pages = dataset.items.list(filters=ItemFilter)
    for page in pages:
        for item in page:
            for ann in item.annotations.list(annotation_filter):
                print(ann)


def func17():
    annotation.metadata['user'] = dict()
    annotation.metadata['user']['MyKey'] = 'MyValue'
    annotation.update()


def func18():
    path = r'path-to-json'
    converter = dl.Converter()
    converter.upload_local_dataset(
        from_format=dl.AnnotationFormat.COCO,
        dataset=dataset,
        local_annotations_path=path)


def func19():
    path = r'path-to-json'
    ds = dl.datasets.get(dataset_id='ds_ID')
    # load the json
    with open(json_path, 'r', encoding="utf8") as f:
        data = json.load(f)
        # filter the items in the dataset based on a key\ID\name..
        namefilter = dl.Filters()
        namefilter.resource = dl.FILTERS_RESOURCE_ITEM
        namefilter.add(field='name', values=data['img_name'])
        pages = dataset.items.list(filters=namefilter)
        # pbar to track the progress
        pbar = tqdm.tqdm(total=pages.items_count)
        # going over the filter result
        for page in pages:
            for item in page:
                # now updating the metadata
                item.metadata['user'] = dict()
                item.metadata['user']['camera_dict'] = data['camera_dict']
                item.metadata['user']['name'] = data['name']
                item.update()
                # for the same item we'll update the annotations
                for i_ann in range(len(data['annotations'])):
                    label = data['annotations'][i_ann]['object_type']
                    top = data['annotations'][i_ann]['top'][0]
                    left = data['annotations'][i_ann]['left'][0]
                    bottom = data['annotations'][i_ann]['bottom'][0]
                    right = data['annotations'][i_ann]['right'][1]
                    angle = data['annotations'][i_ann]['bbox_angle_deg']
                    builder.add(
                        annotation_definition=dl.Box(top=top, left=left, bottom=bottom, right=right, label=label,
                                                     angle=angle))
                    item.annotations.upload(builder)


def func20():
    task = dataset.tasks.create(
        task_name='task_name',
        assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'])

    filters = dl.Filters(field='dir', values='/my/folder/directory')
    task.add_items(
        filters=filters, assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'])
