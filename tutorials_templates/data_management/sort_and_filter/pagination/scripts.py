def section1():
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


def section2():
    # Go over all item and print the properties
    for i_page, page in enumerate(reversed(pages)):
        print('{} items in page {}'.format(len(page), i_page))


def section3():
    for item in pages.all():
        print(item.name)


def section4():
    from concurrent.futures import ThreadPoolExecutor
    def single_item(item):
        # do some work on item
        print(item.filename)
        return True

    with ThreadPoolExecutor(max_workers=32) as executor:
        executor.map(single_item, pages.all())


def section5():
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


def section6():
    import tqdm
    pbar = tqdm.tqdm(total=pages.items_count)

    def single_item(item):
        # do stuff on item
        time.sleep(1)
        pbar.update()
        return True

    with ThreadPoolExecutor(max_workers=32) as executor:
        executor.map(single_item, pages.all())


def section7():
    # Create filters instance
    filters = dl.Filters()
    # Get filtered item list in a page object, where the starting page is 1
    pages = dataset.items.list(filters=filters, page_offset=1, page_size=50)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))
    # Print items from page 1
    print('Length of first page: {}'.format(len(pages.items)))
