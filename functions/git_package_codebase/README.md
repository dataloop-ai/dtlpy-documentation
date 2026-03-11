# deploy package with code from git

this support in dtlpy>=1.35.13

1. create a public package in GitHub  
   Simple example for it is [git repo](https://github.com/dataloop-ai/package_git_example)  
   main.py - for the running code


2. create an app and service from the git repository  
   use the file [deploy](deploy.py)
   that publishes the DPK and installs the app. To use your own git repo set the codebase in `dataloop.json`:
   gitUrl: the url used to clone  
   gitTag: the branch or tag

![Imgur](https://i.imgur.com/AO6ZZOC.png)

test it by make an execution for this service  
**make sure to set the item_id in filed value**  

    execution = service.execute(execution_input=dl.FunctionIO(name='item',
                                                              value=<item_id>,
                                                              type=dl.PackageInputType.ITEM),
                                project_id=project.id, 
                                function_name='run')

And can see the execution flow and status in our UI Go to Applications prease in the service and choose lastExecution

![Imgur](https://i.imgur.com/646NZf0.png)

You will see all the executions and its status and error if it failed

3. update git and show the service is also updated  
   If want to change the code, change it and push your changes to the git repo after go th sdk and update the service using    
   `service.update()`