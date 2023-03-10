## API for analytics

In this bonus section of the API, we will present an exercise that will teach you how can use the API for analytics. You also have a Jupyter notebook that has all of the code from this section in a single file, which you can run and test yourself. This readme is a guide that will teach you what that code works, so you can understand how to operate or modify it to your needs.

The example we are going to showcase here will extract and print all Annotator activity (active/idle), per task and per item, for a chosen Project. These parameters are:
```
taskId: <tasd.id>, itemId: <item.id> user: <user name>, activity status: <active/idle>, duration <ms>
```
Here is also an example how it would look like, when extracted using the API:
```python
taskId: 6146340f41e985613631785f, itemId: 6141d2c50f129f11d30c2c4b, user: Guy Twito, activity status: idle, duration 300000 
```

There are 3 functions that we will define and use, to get the information we need:
- ```get_active_users(project, start_time, end_time=None)``` 
- ```get_user_info_by_hash(hash_tokens)```
- ```get_report(project: dl.Project, start_time: int, end_time: int = None)```

We will now explore and explain each of the functions, so you get a better understanding of how you can use it - or adapt it to your needs.

### The first function
Before defining the first function, we need to import the necesarry libraries, including Dataloop's ```dtlpy``` library and the ```requests``` library - the latter being the API calls library.
```
import dtlpy as dl
import requests
import time
``` 

The first function we will explore is ```get_active_users(project, start_time, end_time=None)```. You can see it below: 

```
import dtlpy as dl
import requests
import time


def get_active_users(project, start_time, end_time=None):
    report = list()
    page_size = 2
    page = 0
    has_next = True
    while has_next:
        payload = {
            "startTime": start_time,
            "endTime": end_time,
            "context": {
                "projectId": [project.id],
            },
            "measures": [{"measureType": "activeUsers",
                          "page": page,
                          "pageSize": page_size,
                          "sortDirection": "descending"}]
        }

        samples = requests.post(dl.environment() + '/analytics/query',
                                headers=dl.client_api.auth,
                                json=payload)
        try:
            samples = samples.json()
        except KeyError as r:
            print('analytics report: Error: {}'.format(r))
            return

        if len(samples) != 0 and 'response' in samples[0]:
            report += samples[0]['response']
            has_next = samples[0]['hasNext']
            page += 1
        else:
            has_next = False
    return get_user_info_by_hash(report)
```

This is a function that gets the active Users and returns the information as a hash. It sends a ```POST``` API request to the Dataloop environment's ```/analytics/query``` url.

The function requires 3 parameters:
- project - the particular Project you want to run the analytics on - to extract the active Users.
- start_time - the exact time you want your Query to start searching from; for example, if you want to search for users that were active starting one week ago.
- end_time - the exact time you want your querry to stop searching from; for example, active users that were active until (meaning end_time) 1 month ago;

To better understand start_time and end_time, you can think that the 2 variables, together define a timeframe. For example start_time= 365 days ago and end_time = 182.5 days ago (meaning 6 months). If the variables would be defined as so, it would mean that you Query for active users from 1 year ago until 6 months ago.

This function first This function extracts and returns the hash tokens of all active users,  using the next function we will explore, ```get_user_info_by_hash(hash_tokens)```.





### The second function
The second function of this exercise is ```get_user_info_by_hash(hash_tokens)```. This is a simple function that uses a ```POST``` API request to the Dataloop's ```/users/hash``` url, to request a hash containing all of the User information we require. It then checks if the ```samples``` variable can be correctly converted to ```.json``` using a try-except. In case it doesn't correctly convert to a ```.json``` file, the function returns an error message. Otherwise, it returns the ```samples``` variable, containing the extracted hash.

```
def get_user_info_by_hash(hash_tokens):
    samples = requests.post(dl.environment() + '/users/hash',
                            headers=dl.client_api.auth,
                            json=hash_tokens)
    try:
        samples = samples.json()
    except KeyError as r:
        print('analytics report: Error: {}'.format(r))
        return
    return samples
```
### The third function
The most important function is called ```get_report(project: dl.Project, start_time: int, end_time: int = None)```, and it requires 3 parameters:
- Project - The project to execute the report on.
- Start Time - MS since the epoch, in UTC.
- end_time - MS since the epoch, in UTC.

The function returns list of Annotator activities (based on the hash of an Annotator/User) and a list of an active Users to get the username by hash. You can see the code below:

```
def get_report(project: dl.Project, start_time: int, end_time: int = None):
    """
    generate list of activities for all annotators in all tasks between dates
    :param project: project to execute the report
    :param start_time: MS since the epoch, in UTC.
    :param end_time: MS since the epoch, in UTC.
    :return: report, active_users
    """
    report = list()
    page_size = 100
    page = 0
    has_next = True
    while has_next:
        payload = {
            "startTime": start_time,
            "endTime": end_time,
            "context": {
                "projectId": [project.id],
            },
            "measures": [{"measureType": "userStatsActivityTimeByField",
                          "page": page,
                          "pageSize": page_size,
                          "params": {
                              "groupByFields": ["taskId", "itemId", "userId"]
                          },
                          "sortDirection": "descending"}]
        }
        samples = requests.post(dl.environment() + '/analytics/query',
                                headers=dl.client_api.auth,
                                json=payload)
        try:
            samples = samples.json()
        except KeyError as r:
            print('analytics report: Error: {}'.format(r))
            return
        if len(samples) != 0 and 'response' in samples[0]:
            report += samples[0]['response']
            has_next = samples[0]['hasNext']
            page += 1
        else:
            has_next = False
    active_users_list = get_active_users(project=project, start_time=start_time, end_time=None)
    active_users = dict()
    for active_user in active_users_list:
        active_users[active_user['hash']] = active_user

    return report, active_users

```

### The main() function

The last function we define in this exercise is the ```main()``` function. Here we will use the functions we defined and expained earlier, to perorm API analytics and get all of the active User information we need. The code for this function can be seen below:

```
def main():
    dl.setenv("rc")
    # dl.login() #If you haven't logged in, do it before you try running the code below.
    now = int(time.time() * 1000)
    day = 60*60*24*1000
    start_time = now - day * 30

    project = dl.projects.get(project_name="guy2")
    start_time = project.created_at
    report, active_user = get_report(project=project, start_time=start_time)
    for line in report:
        print("taskId: {}, itemId: {} user: {}, activityStatus: {}, duration {} ".format(
            line['taskId'],
            line['itemId'],
            active_user[line['userId']]['username'],
            line['activityStatus'],
            line['duration']))


if __name__ == "__main__":
    main()
```
In this function, we firstly need to set the working environment to "rc". Then , we need to define the start_time, which is the time from which our API Query will start. 

The example directly under the ```dl.login()``` for setting time describes how you can define the ```start_time``` variable to be 30 days ago. If you want to apply the analyitics, for example, starting 90 days ago, all you have to do is ```start_time = now - day * 90```, or whatever time-frame you require.

After that, we ```GET``` the project we want to run our analytics on, which is, in this case ```guy2``` - change this to your own project when trying the code.

The ```start_time = project.created_at``` means that we will use analytics on all of the users since the project was created. If you want a custom time, define it as described above.

We then use the ```get_report``` function - which uses all of the functions we explained earlier, to extract active Users and their information as a hash list - on our currently selected Project, from our defined ```start_time``` until the present. 

We then print the results on screen by using a ```for``` loop to go through all of the extracted information.

Lastly, we simply execute the ```main()``` function using the last 2 lines of code:
```
if __name__ == "__main__":
    main()
```

### Final thoughts
This exercise, while it may extract simple information, has showcased how you can perform some basic analysis using API calls on a Dataloop Project. Feel free to modify the code to fit your particular needs and perform the analysis you want to. 

You can find the complete code in a Jupyter Notebook we created for you.


