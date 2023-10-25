def func1():
    """
    # Advance Configurations
    ## Service Runtime
    """


def func2():
    """
    ## Autoscaler
    When we have changing loads of work, we want the number of replicas of the service to scale up when there are many executions coming in, and scale down otherwise.
    To do so, we need to create an autoscaler:
    """


def func3():
    """
    ## Using Secrets in a Function
    You can use organization integration secrets (key-value) as environment variable inside the function's env.
    First you'll need to add the integrations (UI only), then simply add the integrations' ids whe deploying the service:
    """


def func4():
    """
    Inside the service you can access the values using os package:
    """


def func5():
    """
    ## Progress and Context

    In any function you can add two more inputs: `progress` and `context`.

    For example:

    ```python
    class ServiceRunner(dl.BaseServiceRunner):
    def detect(self, item: dl.Item, progress: dl.Progress, context: dl.Context):
        progress.update(status='inProgress', progress=0,
                        message='execution started')
    ```
    Context is a class that saves all the relevant information for this run, e.g. `context.execution_id`, `context.service_id` and more.

    You can also use the `context.logger` to get a logger instance. Using this logger will help us save the logs in the correct way (log level) and will make it easier to filter them in the logs page.

    Use the python auto complete to check all the dl.Context options.


    Progress can be used to update the progress percent and change the status of each step:

    ```python
    progress.update(progress=0,  message='execution started')
    progress.update(progress=80,  message='almost done')
    progress.update(progress=99,  message='one more sec...')
    progress.update(progress=100,  message='done')
    ```

    """
