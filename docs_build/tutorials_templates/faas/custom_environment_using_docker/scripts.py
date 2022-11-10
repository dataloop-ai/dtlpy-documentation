def func1():
    service = package.deploy(service_name='my-service',
                             runtime=dl.KubernetesRuntime(
                                 runner_image='docker.io/python:3.8'
                             ))


def func2():
    service = dl.services.get('service-id-or-name')
    service.runtime.runner_image = 'python:3.8'
    service.update()
