## API for analytics

So we thought, as a first start, to document one example I developed and shared with Prospera a while ago, and maybe the example can be added to the development community.

The example print to the screen all annotator activity (active/idle) per task per item for a project:
taskId: <tasd.id>, itemId: <item.id> user: <user name>, activity status: <active/idle>, duration <ms>

For example:
taskId: 6146340f41e985613631785f, itemId: 6141d2c50f129f11d30c2c4b user: Guy Twito, activity status: idle, duration 300000 

the main function called get_reports, it get 3 parameters:
   Project: project to execute the report
   Start Time: MS since the epoch, in UTC.
   end_time: MS since the epoch, in UTC.
the function return list of annotator activities (with hash annotator) and a list of an active user to get the user name by hash

Next week I'll talk to  Guy and check what modifications can be done to the primary call payload so it can be used in different groups and contexts.


----Code----
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


def main():
    dl.setenv("rc")
    # dl.login()
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
