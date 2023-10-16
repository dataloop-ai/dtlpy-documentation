import dtlpy as dl


def func1():
    filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
    filters.add(field='scope', values='public')
    dl.models.list(filters=filters).print()


def func2():
    project = dl.projects.get("Models")
    dataset = project.datasets.get("Resnet Classification")
    item = dataset.items.upload(
        'https://github.com/dataloop-ai/dtlpy-documentation/blob/f63d2c6ccefbde90255d7a00bdf9cda45f24cb6f/assets/images/hamster.jpg?raw=true')


def func3():
    public_model = dl.models.get(model_name="pretrained-resnet50")

    model = project.models.clone(from_model=public_model,
                                 model_name='resnet_50',
                                 project_id=project.id)
    service = model.deploy(service_config={'runtime': {"podType": dl.INSTANCE_CATALOG_REGULAR_S}})


def func4():
    model = dl.models.get(model_id=model.id)
    ex = model.predict(item_ids=[item.id])
    ex.wait()

    item.open_in_web()


def func5():
    custom_model = project.models.clone(from_model=public_model,
                                        model_name='finetuning_mode',
                                        dataset=dataset,
                                        project_id=project.id,
                                        labels=['label1', 'label2'])


def func6():
    train_filter = dl.Filters(field='dir', values='/train')
    validation_filter = dl.Filters(field='dir', values='/validation')

    dataset.metadata['system']['subsets'] = {'train': json.dumps(train_filter.prepare()),
                                             'validation': json.dumps(validation_filter.prepare()),
                                             }
    dataset.update(system_metadata=True)


def func7():
    ex = custom_model.train()
    ex.logs(follow=True)  # to stream the logs during training
    custom_model = dl.models.get(model_id=custom_model.id)
    print(custom_model.status)


def func8():
    custom_model.deploy()
    custom_model = dl.models.get(model_id=custom_model.id)  # to get new information on the deployed service
    model.predict(item_ids=[item.id])
