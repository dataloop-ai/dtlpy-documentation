import dtlpy as dl


def func1():
    import dtlpy as dl
    import os
    project = dl.projects.get(project_name='<project-name>')
    package = project.packages.push(package_name='dummy-model-package',
                                    src_path=os.getcwd(),
                                    modules=[])
    model = package.models.create(model_name='My Model',
                                  description='model for offline model logging',
                                  dataset_id='<dataset-id>',
                                  labels=[])


def func2():
    epoch = np.linspace(0, 9, 10)
    epoch_metric = np.linspace(0, 9, 10)

    for x_metric, y_metric in zip(epoch, epoch_metric):
        model.metrics.create(samples=dl.PlotSample(figure='tutorial plot',
                                                   legend='some metric',
                                                   x=x_metric,
                                                   y=y_metric),
                             dataset_id=model.dataset_id)


def func3():
    samples = model.metrics.list()

    for sample in samples.all():
        print(sample.x, sample.y)

    # or retrieve it as a DataFrame
    df = model.metrics.list().to_df()


