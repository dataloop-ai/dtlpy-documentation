def func1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()


def func2():
    project = dl.projects.create(project_name='project-sdk-tutorial')
    project.datasets.create(dataset_name='dataset-sdk-tutorial')


def func3():
    project = dl.projects.get(project_name='project-sdk-tutorial')
    dataset = project.datasets.get(dataset_name='dataset-sdk-tutorial')


def func4():
    import dtlpy as dl
    import cv2
    import numpy as np

    class ImageProcess(dl.BaseServiceRunner):
        @staticmethod
        def rgb2gray(item: dl.Item):
            """
            Function to convert RGB image to GRAY
            Will also add a modality to the original item
            :param item: dl.Item to convert
            :return: None
            """
            buffer = item.download(save_locally=False)
            bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
            gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
            gray_item = item.dataset.items.upload(local_path=gray,
                                                  remote_path='/gray' + item.dir,
                                                  remote_name=item.filename)
            # add modality
            item.modalities.create(name='gray',
                                   ref=gray_item.id)
            item.update(system_metadata=True)

        @staticmethod
        def clahe_equalization(item: dl.Item):
            """
            Function to perform histogram equalization (CLAHE)
            Will add a modality to the original item
            Based on opencv https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
            :param item: dl.Item to convert
            :return: None
            """
            buffer = item.download(save_locally=False)
            bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
            # create a CLAHE object (Arguments are optional).
            lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
            lab_planes = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            lab_planes[0] = clahe.apply(lab_planes[0])
            lab = cv2.merge(lab_planes)
            bgr_equalized = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
            bgr_equalized_item = item.dataset.items.upload(local_path=bgr_equalized,
                                                           remote_path='/equ' + item.dir,
                                                           remote_name=item.filename)
            # add modality
            item.modalities.create(name='equ',
                                   ref=bgr_equalized_item.id)
            item.update(system_metadata=True)


def func5():
    modules = [dl.PackageModule(name='image-processing-module',
                                entry_point='main.py',
                                class_name='ImageProcess',
                                functions=[dl.PackageFunction(name='rgb2gray',
                                                              description='Converting RGB to gray',
                                                              inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                    name='item')]),
                                           dl.PackageFunction(name='clahe_equalization',
                                                              description='CLAHE histogram equalization',
                                                              inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                    name='item')])
                                           ])]


def func6():
    src_path = 'functions/opencv_functions'
    project = dl.projects.get(project_name='project-sdk-tutorial')
    package = project.packages.push(package_name='image-processing',
                                    modules=modules,
                                    src_path=src_path)


def func7():
    service = package.services.deploy(service_name='image-processing',
                                      runtime=dl.KubernetesRuntime(concurrency=32),
                                      module_name='image-processing-module')


def func8():
    filters = dl.Filters()
    filters.add(field='datasetId', values=dataset.id)

    trigger = service.triggers.create(name='image-processing2',
                                      function_name='clahe_equalization',
                                      execution_mode=dl.TriggerExecutionMode.ONCE,
                                      resource=dl.TriggerResource.ITEM,
                                      actions=dl.TriggerAction.CREATED,
                                      filters=filters)


def func9():
    trigger = service.triggers.create(name='image-processing-rgb',
                                      function_name='rgb2gray',
                                      execution_mode=dl.TriggerExecutionMode.ALWAYS,
                                      resource=dl.TriggerResource.ITEM,
                                      actions=dl.TriggerAction.UPDATED,
                                      filters=filters)


def func10():
    item = dataset.items.upload(
        local_path=['https://raw.githubusercontent.com/dataloop-ai/tiny_coco/master/images/train2017/000000463730.jpg'])
    # Remote path is optional, images will go to the main directory by default


def func11():
    service.log()


def func12():
    item.open_in_web()


def func13():
    service.pause()


def func14():
    modules = [
        dl.PackageModule(
            name='first-module',
            entry_point='first_module_main.py',
            functions=[
                dl.PackageFunction(
                    name='run',
                    inputs=[dl.FunctionIO(name='item',
                                          type=dl.PackageInputType.ITEM)]
                )
            ]
        ),
        dl.PackageModule(
            name='second-module',
            entry_point='second_module_main.py',
            functions=[
                dl.PackageFunction(
                    name='run',
                    inputs=[dl.FunctionIO(name='item',
                                          type=dl.PackageInputType.ITEM)]
                )
            ]
        )
    ]


def func15():
    package = project.packages.push(package_name='two-modules-test',
                                    modules=modules,
                                    src_path='<path to where the entry point is located>'
                                    )


def func16():
    service = package.deploy(
        module_name='first-module',
        service_name='first-module-test-service'
    )
