import dtlpy as dl


def func1():
    import dtlpy as dl
    import os
    project = dl.projects.get(project_name='My Project')
    package = project.packages.push(package_name='dummy-model-package',
                                    codebase=dl.entities.LocalCodebase(os.getcwd()),
                                    modules=[])
    model = package.models.create(model_name='My Model',
                                  description='model for offline model logging',
                                  dataset_id='My Dataset',
                                  labels=[])


def func2():
    for x_metric, y_metric in zip(some_metric):
        model.add_log_samples(samples=dl.LogSample(figure='test metrics',
                                                   legend='metric1',
                                                   x=x_metric,
                                                   y=y_metric),
                              dataset_id=model.dataset_id)


def func3():
    filters = dl.Filters(resource=dl.FiltersResource.PACKAGE, use_defaults=False)
    filters.add(field='scope', values='public')
    dl.packages.list(filters=filters).print()


def func4():
    global_yolo_package = dl.packages.get(package_id="package_id")
    global_yolo_model = global_yolo_package.models.get(model_id="model_id")

    model = project.models.clone(from_model=global_yolo_model,
                                 model_name='yolov5_remote',
                                 project_id=project.id)


def func5():
    global_yolo_model = global_yolo_package.models.get(model_id="model_id")

    model = dl.models.clone(from_model=global_yolo_model,
                            model_name='yolov5_remote',
                            project_id=project.id)
