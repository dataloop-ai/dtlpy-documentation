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
        model.add_log_samples(samples=dl.LogSample(figure='tutorial plot',
                                                   legend='some metric',
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
    dataset.update(system_metadata=True)


def func5():
    public_model = dl.models.get(model_id="<model_id>")

    model = project.models.clone(from_model=public_model,
                                 model_name='remote_model',
                                 project_id=project.id)

    model.deploy()


def func6():
    custom_model = dl.models.clone(from_model=public_model,
                                   model_name='remote_custom_model',
                                   dataset=dataset,
                                   project_id=project.id,
                                   labels=['label1', 'label2'])
    model.train()
    model.deploy()


def func7():
    package = dl.packages.get(package_id=model.package_id)

    # build model
    adapter = package.build(module_name='model-adapter')  # module name varies by model
    adapter.load_from_model(model_entity=model)


def func8():
    item = dl.items.get(item_id='631ef21d240440c5455788b7')
    annotations = adapter.predict_items([item], with_upload=True)
    image = np.asarray(Image.open(item.download()))
    plt.imshow(item.annotations.show(image,
                                     thickness=5))
    print('Prediction: {}'.format(annotations[0][0].label))
