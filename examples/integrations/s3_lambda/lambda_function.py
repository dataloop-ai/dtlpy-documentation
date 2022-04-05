import os
import urllib.parse

# set dataloop path to tmp
os.environ["DATALOOP_PATH"] = "/tmp"

import dtlpy as dl

project_name = 'your project'
dataset_name = 'your async dataset'


def lambda_handler(event, context):
    dl.login_m2m(email='username', password='pass')

    project = dl.projects.get(project_name=project_name)
    dataset = project.datasets.get(dataset_name=dataset_name)

    for record in event['Records']:
        # get the bucket name
        bucket = record['s3']['bucket']['name']

        # get the file name
        key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')

        if 'ObjectRemoved' in record['eventName']:
            try:
                key_name = '/' + key
                filters = dl.Filters(field='filename', values=key_name)
                dataset.items.delete(filters=filters)

            except Exception as e:
                raise e

        elif 'ObjectCreated' in record['eventName']:
            try:
                # upload the file
                path = 'external://' + key
                # dataset.items.upload(local_path=path, overwrite=True) # if overwrite is required
                dataset.items.upload(local_path=path)

            except Exception as e:
                raise e
