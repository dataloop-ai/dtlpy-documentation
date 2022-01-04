import inspect
import dtlpy as dl


def func1():
    def rgb2gray(item: dl.Item):
        # download item as a buffer
        buffer = item.download(save_locally=False)
        image = Image.open(buffer).convert("LA" if "png" in item.mimetype else "L")
        buffer = io.BytesIO()
        buffer.name = item.name
        image.save(buffer)
        # upload item
        new_item = item.dataset.items.upload(local_path=buffer,
                                             remote_path='/greyscale',
                                             overwrite=True)
        if item.annotations_count:
            new_item.annotations.upload(annotations=item.annotations.list())
        return new_item.id


def func2():
    service = project.services.deploy(func=greyscale_single_item, service_name='greyscale-item-service')


def func3():
    dl.print()
