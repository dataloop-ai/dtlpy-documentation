def section1():
    # upload and claim item
    item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
    # or get item
    item = dataset.items.get(item_id='write-your-id-number')
    # Init user metadata
    item.metadata['user'] = dict()
    # Add string metadata
    item.metadata['user']['MyStringKey'] = 'MyValue'
    # Add number type metadata
    item.metadata['user']['MyNumberKey'] = 3
    # Add boolean type metadata
    item.metadata['user']['MyBooleanKey'] = True
    # Add null metadata
    item.metadata['user']['MyNullKey'] = None
    #Add list metadata
    item.metadata['user']['MyListKey'] = ["A", 2, False]
    # Append value to metadata list
    item.metadata['user']['MyListKey'].append(3)

    # update and reclaim item
    item = item.update()
    # Look at an items' metadata section (in platform or download the item's JSON) and review the USER section to see the values

def section2():
    import pandas
    import dtlpy as dl
    dataset = dl.datasets.get(dataset_id='id')  # Get dataset
    to_upload = list()
    # First item and info attached:
    to_upload.append({'local_path': r"E:\TypesExamples\000000000064.jpg",  # Item file path
                      'local_annotations_path': r"E:\TypesExamples\000000000776.json",  # Annotations file path
                      'remote_path': "/first",  # Dataset folder to upload the item to
                      'remote_name': 'f.jpg',  # Dataset folder name
                      'item_metadata': {'user': {'dummy': 'fir'}}})  # Added user metadata
    # Second item and info attached:
    to_upload.append({'local_path': r"E:\TypesExamples\000000000776.jpg",  # Item file path
                      'local_annotations_path': r"E:\TypesExamples\000000000776.json",  # Annotations file path
                      'remote_path': "/second",  # Dataset folder to upload the item to
                      'remote_name': 's.jpg',  # Dataset folder name
                      'item_metadata': {'user': {'dummy': 'sec'}}})  # Added user metadata
    df = pandas.DataFrame(to_upload)  # Make data into table
    items = dataset.items.upload(local_path=df,
                                 overwrite=True)  # Upload table to platform

def section3():
    # Get annotation
    annotation = dl.annotations.get(annotation_id='my-annotation-id')
    # Init metadata
    annotation.metadata['user'] = dict()
    # String type annotation metadata
    annotation.metadata['user']['FromModel'] = 'MyModel 1.0.1'
    # Boolean type annotation metadata
    annotation.metadata['user']['automated'] = True
    # Number type annotation metadata
    annotation.metadata['user']['AnnotationID'] = 3
    # Null type annotation metadata
    annotation.metadata['user']['Ignore'] = None
    # Add annotation list metadata
    item.metadata['user']['Params'] = ["A", 2, False]
    # Append value to annotation list metadata
    annotation.metadata['user']['Params'].append(3)
    # update and reclaim annotation
    annotation = annotation.update()
    # annotation in platform should have section 'user' in metadata with field 'red' and value True
