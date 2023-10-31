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
    train_filter = dl.Filters(field='dir', values='/train')
    validation_filter = dl.Filters(field='dir', values='/validation')

    custom_model = project.models.clone(from_model=public_model,
                                        model_name='finetuning_mode',
                                        dataset=dataset,
                                        project_id=project.id,
                                        train_filter=train_filter,
                                        validation_filter=validation_filter)


def func6():
    ex = custom_model.train(service_config={'runtime': {"podType": dl.INSTANCE_CATALOG_REGULAR_S}})
    # Or with a full service config:
    ex = custom_model.train(service_config={
        'runtime': dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_GPU_K80_S,
                                        autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                            min_replicas=0,
                                            max_replicas=1),
                                        preemptible=False,
                                        concurrency=1).to_json(),
        'executionTimeout': 10000 * 3600
    })
    ex.logs(follow=True)  # to stream the logs during training
    custom_model = dl.models.get(model_id=custom_model.id)
    print(custom_model.status)


def func7():
    custom_model.deploy()
    custom_model = dl.models.get(model_id=custom_model.id)  # to get new information on the deployed service
    model.predict(item_ids=[item.id])
