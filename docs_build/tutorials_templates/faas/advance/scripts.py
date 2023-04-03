import dtlpy as dl


class Scripts:
    def func1(self):
        package: dl.Package
        service = package.deploy(
            service_name='my-service',
            runtime=dl.KubernetesRuntime(
                pod_type=dl.InstanceCatalog.REGULAR_S,
                concurrency=10,
                runner_image='python:3.9',  # optional - any custom docker image,
                autoscaler=dl.KubernetesRabbitmqAutoscaler(
                    min_replicas=0,
                    max_replicas=1,
                    queue_length=10,
                    cooldown_period=300,
                    polling_interval=10
                )))

    def func2(self):
        autoscaler = dl.KubernetesRabbitmqAutoscaler(
            min_replicas=0,
            max_replicas=1,
            queue_length=10,
            # cooldown_period: define how long to wait before scaling down (reducing the number of replicas) in case the queue is below the queue_length.
            cooldown_period=300,
            # polling_interval (in seconds): this parameter defines how often the queue is being sampled to perform any action.
            polling_interval=10
        )

    def func3(self):
        package: dl.Package
        package.services.deploy(name='with-integrations',
                                secrets=['integrationId'])

    def func4(self):
        import os
        print(os.environ['INTEGRATION_NAME'])
