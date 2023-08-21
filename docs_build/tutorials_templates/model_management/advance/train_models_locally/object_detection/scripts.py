def func1():
    # !pip install torch torchvision imgaug "scikit-image<0.18"
    import matplotlib.pyplot as plt
    from PIL import Image
    import numpy as np
    import dtlpy as dl
    import json
    from dtlpy.ml import train_utils


def func2():
    project = dl.projects.create('Fruit - Model Mgmt')
    dataset = project.datasets.create('Fruit')
    dataset.to_df()
    _ = dataset.items.upload(local_path='../../../../assets/sample_datasets/FruitImage/items/*',
                             local_annotations_path='../../../../assets/sample_datasets/FruitImage/json')
    dataset.add_labels(label_list=['orange', 'banana', 'apple'])
    dataset.open_in_web()


def func3():
    subsets = {'train': json.dumps(dl.Filters(field='dir', values='/train').prepare()),
               'validation': json.dumps(dl.Filters(field='dir', values='/validation').prepare())}
    dataset.metadata['system']['subsets'] = subsets
    dataset.update(True)


def func4():
    import dtlpy as dl
    filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
    filters.add(field='scope', values='public')
    dl.models.list(filters=filters).to_df()
    # get the public model
    pretrained_model = dl.models.get(model_name='pretrained-yolo-v8')

    model = pretrained_model.clone(model_name='fruits-model',
                                   dataset=dataset,
                                   project_id=project.id,
                                   configuration={'epochs': 10,
                                                  'batch_size': 4,
                                                  'imgz': 640,
                                                  'id_to_label_map': {(v - 1): k for k, v in
                                                                      dataset.instance_map.items()}
                                                  })


def func5():
    adapter = dl.packages.build(package=model.package,
                                init_inputs={'model_entity': model},
                                module_name='model-adapter')


def func6():
    print("Training {!r} on dataset {!r}".format(model.name, dataset.name))
    adapter.train_model(model=model)


def func7():
    adapter.model.artifacts.list_content()


def func8():
    item = dl.items.get(item_id='6110d4a41467ded7a8c2a23d')
    annotations = adapter.predict_items([item], with_upload=True)
    image = Image.open(item.download())
    plt.imshow(item.annotations.show(image,
                                     thickness=5))
    print('Classes found: {}'.format([ann.label for ann in annotations[0]]))
