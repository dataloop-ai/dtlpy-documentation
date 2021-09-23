import dtlpy as dl
import time

# Set project name and service name
service_name = 'custom-python'
project_name = 'COCO ors'

project = dl.projects.get(project_name=project_name)


# This is the function that we're going to run
def get_version():
    import sys
    print("Python version")
    print(sys.version)
    return sys.version


# Deploying the service
service = project.services.deploy(func=get_version,
                                  service_name=service_name,
                                  # runtime=dl.KubernetesRuntime(runner_image='python:3.9.7')
                                  )
# TODO fix following
service = project.services.get(service_name=service_name)
service.runtime.runner_image = 'python:3.9.7'
service.update(force=True)

# Executing the function - this should print the function output with the python version
execution = service.execute(function_name='get_version',
                            project_id=project.id)

time.sleep(10)  # maybe need to wait more. if empty - run next 3 lines again
execution = service.executions.get(execution_id=execution.id)
print(execution.latest_status)
print(execution.output)
