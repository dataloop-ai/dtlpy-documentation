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