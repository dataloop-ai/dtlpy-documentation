import dtlpy as dl

project_by_name = dl.projects.get(project_name='COCO ors')

project_by_id = dl.projects.get(project_id=project_by_name.id)

print(dl.client_api.last_curl)
