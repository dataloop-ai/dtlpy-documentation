import dtlpy as dl
import time

project_name = 'My Project'
service_name = 'logs-function'

project = dl.projects.get(project_name=project_name)


def run(item: dl.Item) -> dl.Item:
    for i in range(10):
        print(i)
        print(item.name)
        time.sleep(1)
    return item


##################
# Create service #
##################
service = dl.Service.from_function(
    func=run,
    name=service_name,
    project=project,
    client_api=dl.client_api,
    runtime={'gpu': False, 'numReplicas': 1, 'concurrency': 32}
)
print('Service deployed successfully!')

######################
# Execute a Function #
######################
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
execution = service.execute(
    function_name='run',
    item_id=item.id,
    project_id=project.id
)
execution.logs(follow=True)
