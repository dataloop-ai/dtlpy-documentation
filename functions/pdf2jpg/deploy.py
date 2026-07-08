import os
import dtlpy as dl
from pdf2image import convert_from_path

project_name = 'MY Project'
service_name = 'pdf2jpg'
input_directory = '/incoming'

project = dl.projects.get(project_name=project_name)


def run(item: dl.Item) -> str:
    filepath = ''
    output = '{}.jpg'.format(item.name)
    dataset = dl.datasets.get(dataset_id=item.datasetId, fetch=False)
    try:
        filepath = item.download()
        pages = convert_from_path(filepath, 500)
        pages[0].save(output, 'JPEG')
        jpg_item = dataset.items.upload(local_path=output,
                                        remote_path='/jpgs',
                                        remote_name=output)
    finally:
        if os.path.isfile(filepath):
            os.remove(filepath)
        if os.path.isfile(output):
            os.remove(output)
    return jpg_item.id


######################
# Create the Service #
######################
service = dl.Service.from_function(
    func=run,
    name=service_name,
    project=project,
    client_api=dl.client_api,
    runtime={
        'concurrency': 32,
        'runnerImage': 'gcr.io/viewo-g/piper/agent/cpu/pdf2jpg:1'
    }
)
print('Service deployed successfully!')

######################
# Create the Trigger #
######################
trigger = service.triggers.create(
    name=service_name,
    execution_mode=dl.TriggerExecutionMode.ONCE,
    resource=dl.TriggerResource.ITEM,
    actions=dl.TriggerAction.CREATED,
    filters=dl.Filters(field='dir', values=input_directory)
)
print('Trigger was created successfully!')
