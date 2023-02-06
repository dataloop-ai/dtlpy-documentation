import dtlpy as dl


class Scripts:
    def __init__(self):
        self.rgb2gray = None
        self.service = None
        self.execution = None

    def func1(self):
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
                                                           remote_name=item.name)

            # add modality
            item.modalities.create(name='gray',
                                   ref=bgr_equalized_item.id)
            item.update(system_metadata=True)

        # DTLPY-STOP
        self.rgb2gray = rgb2gray

    def func2(self, dl, rgb2gray):
        project = dl.projects.get(project_name='project-sdk-tutorial')
        service = project.services.deploy(func=rgb2gray,
                                          service_name='grayscale-item-service')

        # DTLPY-STOP
        self.service = service

    def func3(self):
        item.open_in_web()

    def func4(self, project, service, item):
        execution = service.execute(project_id=project.id,
                                    item_id=item.id,
                                    function_name='rgb2gray')
        execution.logs(follow=True)

        execution = execution.wait()
        print(execution.latest_status)

        # DTLPY-STOP
        self.execution = execution

    def func5(self, service, dataset):
        filters = dl.Filters(resource=dl.FiltersResource.ITEM,
                             field='dir',
                             values='/test',
                             context={'datasets': [dataset.id]})
        command = service.execute_batch(
            filters=filters,
            function_name='rgb2gray')

    def func6(self):
        item.open_in_web()
