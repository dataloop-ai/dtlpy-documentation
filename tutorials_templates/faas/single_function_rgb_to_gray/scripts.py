import dtlpy as dl


def func1():
    def rgb2gray(item: dl.Item):
        """
        Function to convert RGB image to GRAY
        Will also add a modality to the original item
        :param item: dl.Item to convert
        :return: None
        """
        import numpy as np
        import cv2

        buffer = item.download(save_locally=False)
        bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        bgr_equalized_item = item.dataset.items.upload(local_path=gray,
                                                       remote_path='/gray' + item.dir,
                                                       remote_name=item.filename)

        # add modality
        item.modalities.create(name='gray',
                               ref=bgr_equalized_item.id)
        item.update(system_metadata=True)


def func2():
    service = project.services.deploy(func=rgb2gray,
                                      service_name='grayscale-item-service')


def func3():
    item.open_in_web()


def func4():
    execution = service.execute(project_id=project.id,
                                item_id=item.id,
                                function_name='rgb2gray')
    execution.logs(follow=True)

    execution = execution.wait()
    print(execution.latest_status)


def func5():
    item.open_in_web()
