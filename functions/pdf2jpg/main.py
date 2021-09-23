import os
import dtlpy as dl
from pdf2image import convert_from_path


class ServiceRunner:
    def __init__(self):
        pass

    @staticmethod
    def run(item: dl.Item):
        filepath = ''
        output = '{}.jpg'.format(item.name)
        dataset = dl.datasets.get(dataset_id=item.datasetId, fetch=False)
        try:
            filepath = item.download()
            pages = convert_from_path(filepath, 500)
            pages[0].save(output, 'JPEG')
            jpg_item = dataset.items.upload(local_path=output,
                                            remote_path='/jpgs',
                                            remote_name=output)
        finally:
            if os.path.isfile(filepath):
                os.remove(filepath)
            if os.path.isfile(output):
                os.remove(output)
        return jpg_item.id
