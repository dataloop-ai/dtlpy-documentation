import dtlpy as dl


def func1():
    import dtlpy as dl
    import os
    project = dl.projects.get(project_name='<project_id>')
    package = project.packages.push(package_name='dummy-model-package',
                                    codebase=dl.entities.LocalCodebase(os.getcwd()),
                                    modules=[])
    model = package.models.create(model_name='My Model',
                                  description='model for offline model logging',
                                  dataset_id='<dataset_id>',
                                  labels=[])


def func2():
    epoch = np.linspace(0, 9, 10)
    epoch_metric = np.linspace(0, 9, 10)

    for x_metric, y_metric in zip(epoch, epoch_metric):
        model.add_log_samples(samples=dl.LogSample(figure='tutorial metric',
                                                   legend='metric1',
                                                   x=x_metric,
                                                   y=y_metric),
                              dataset_id=model.dataset_id)


def func3():
    filters = dl.Filters(resource=dl.FiltersResource.PACKAGE, use_defaults=False)
    filters.add(field='scope', values='public')
    dl.packages.list(filters=filters).print()


def func4():
    dataset.metadata['system']['subsets'] = {
        'train': json.dumps(dl.Filters(field='dir', values='/train').prepare()),
        'validation': json.dumps(dl.Filters(field='dir', values='/validation').prepare()),
    }
    dataset.update()


def func5():
    public_yolo_model = dl.models.get(model_id="<model_id>")

    model = project.models.clone(from_model=public_yolo_model,
                                 model_name='yolov5_remote',
                                 project_id=project.id)


def func6():
    public_yolo_model = dl.models.get(model_id="<model_id>")

    model = dl.models.clone(from_model=public_yolo_model,
                            model_name='yolov5_remote',
                            project_id=project.id)
