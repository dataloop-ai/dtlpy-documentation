import dtlpy as dl

def func1():
    filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
    filters.add(field='scope', values='public')
    dl.models.list(filters=filters).print()



def func2():
    public_model = dl.models.get(model_id="<model_id>")

    model = project.models.clone(from_model=public_model,
                                 model_name='remote_model',
                                 project_id=project.id)

    model.deploy()


def func3():
    custom_model = dl.models.clone(from_model=public_model,
                                   model_name='remote_custom_model',
                                   dataset=dataset,
                                   project_id=project.id,
                                   labels=['label1', 'label2'])


def func4():
    dataset.metadata['system']['subsets'] = {
        'train': json.dumps(dl.Filters(field='dir', values='/train').prepare()),
        'validation': json.dumps(dl.Filters(field='dir', values='/validation').prepare()),
    }
    dataset.update(system_metadata=True)


def func5():
    custom_model.train()
    custom_model.deploy()
