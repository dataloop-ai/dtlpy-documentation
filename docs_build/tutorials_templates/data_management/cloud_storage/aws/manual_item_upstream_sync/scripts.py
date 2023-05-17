def section1():
    import dtlpy as dl

    dl.login()

    # This path is in AWS context
    # In a case the item is located in a folder add the folder name as well "folder/item.png"
    item_path = 'external://' + '<Your_item_full_name>'

    # If you want to upload items to specific folder in Dataloop, you can specify the folder path
    remote_path = '/Test_Folder'

    dataset = dl.datasets.get(dataset_id='your dataset id')
    dataset.items.upload(local_path=item_path, remote_path=remote_path)