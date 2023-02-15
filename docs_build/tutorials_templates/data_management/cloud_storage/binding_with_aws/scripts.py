def section1():
    import os
    import urllib.parse

    # Set dataloop path to tmp (to read/write from the lambda)
    os.environ["DATALOOP_PATH"] = "/tmp"
    import dtlpy as dl

    DATASET_ID = ''
    DTLPY_USERNAME = ''
    DTLPY_PASSWORD = ''

    def lambda_handler(event, context):
        dl.login_m2m(email=DTLPY_USERNAME, password=DTLPY_PASSWORD)
        dataset = dl.datasets.get(dataset_id=DATASET_ID,
                                  fetch=False  # to avoid GET the dataset each time
                                  )
        driver_path = dl.drivers.get(driver_id=dataset.driver).path
        for record in event['Records']:
            # Get the bucket name
            bucket = record['s3']['bucket']['name']

            # Get the file name
            filename = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
            remote_path = None
            if driver_path == '/':
                driver_path = None
            if driver_path is not None and driver_path not in filename:
                return
            if driver_path:
                if not driver_path.startswith("/"):
                    driver_path = "/" + driver_path
                remote_path = filename.replace(driver_path, '')
            else:
                remote_path = filename
            if 'ObjectRemoved' in record['eventName']:
                # On delete event - delete the item from Dataloop
                try:
                    dtlpy_filename = '/' + remote_path
                    filters = dl.Filters(field='filename', values=dtlpy_filename)
                    dataset.items.delete(filters=filters)
                except Exception as e:
                    raise e

            elif 'ObjectCreated' in record['eventName']:
                # On create event - add a new item to the Dataset
                try:
                    # upload the file
                    path = 'external://' + filename
                    # dataset.items.upload(local_path=path, overwrite=True) # if overwrite is required
                    dataset.items.upload(local_path=path, remote_path=remote_path)
                except Exception as e:
                    raise e
