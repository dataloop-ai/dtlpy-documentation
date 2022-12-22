import datetime
import random
import behave
import time
import jwt
import os

import dtlpy as dl
import numpy as np
from behave_testrail_reporter import TestrailReporter


@behave.given('Platform Interface is initialized as dlp and Environment is set according to git branch')
def before_all(context):
    # set up lists to delete
    if not hasattr(context, 'to_delete_packages_ids'):
        context.to_delete_packages_ids = list()
    if not hasattr(context, 'to_delete_services_ids'):
        context.to_delete_services_ids = list()
    if not hasattr(context, 'to_delete_projects_ids'):
        context.to_delete_projects_ids = list()
    if not hasattr(context, 'to_delete_pipelines_ids'):
        context.to_delete_pipelines_ids = list()
    if not hasattr(context, 'to_delete_feature_set_ids'):
        context.to_delete_feature_set_ids = list()
    if not hasattr(context, 'to_delete_feature_ids'):
        context.to_delete_feature_ids = list()
    if not hasattr(context, 'to_delete_test_assets_dir'):
        context.to_delete_test_assets_dir = list()
    if not hasattr(context, 'timestamp'):
        context.timestamp = list()

    if hasattr(context.feature, 'dataloop_feature_dl'):
        context.dl = context.feature.dataloop_feature_dl
    else:
        # get cookie name
        feature_name = context.feature.name.replace(' ', '_')
        api_counter_name = 'api_counter_{}.json'.format(feature_name)
        api_counter_filepath = os.path.join(os.path.dirname(dl.client_api.cookie_io.COOKIE), api_counter_name)
        # set counter
        dl.client_api.set_api_counter(api_counter_filepath)

        # set context for run
        context.dl = dl

        # reset api counter
        context.dl.client_api.calls_counter.on()
        context.dl.client_api.calls_counter.reset()

        # Set env to rc
        context.dl.setenv('rc')

        # check token
        payload = None
        for i in range(10):
            try:
                payload = jwt.decode(context.dl.token(), algorithms=['HS256'],
                                     verify=False, options={'verify_signature': False})
                break
            except jwt.exceptions.DecodeError:
                time.sleep(np.random.rand())
                pass

        allow_locally_with_user = os.environ.get('ALLOW_RUN_TESTS_LOCALLY_WITH_USER', 'false') == 'true'

        if not allow_locally_with_user and payload['email'] not in ['oa-test-4@dataloop.ai', 'oa-test-1@dataloop.ai',
                                                                    'oa-test-2@dataloop.ai',
                                                                    'oa-test-3@dataloop.ai']:
            assert False, 'Cannot run test on user: "{}". only test users'.format(payload['email'])

        # save to feature level
        context.feature.dataloop_feature_dl = context.dl

        avoid_testrail = os.environ.get('AVOID_TESTRAIL', 'false') == 'true'

        if not avoid_testrail and len(context.config.reporters) == 1:
            build_number = os.environ.get('GITHUB_RUN_NUMBER')
            current_branch = "rc - #" + str(build_number)  # Get the current build branch
            testrail_reporter = TestrailReporter(current_branch)
            testrail_reporter.config['base_url'] = os.environ.get('TESTRAIL_URL')
            context.config.reporters.append(testrail_reporter)


@behave.given('There is a project by the name of "{project_name}"')
def step_impl(context, project_name):
    if hasattr(context.feature, 'dataloop_feature_project'):
        context.project = context.feature.dataloop_feature_project
    else:
        context.num = random.randint(10000, 100000)
        project_name = 'to-delete-test-{}_{}'.format(project_name, str(context.num))
        context.project = context.dl.projects.create(project_name=project_name)
        context.to_delete_projects_ids.append(context.project.id)
        context.feature.dataloop_feature_project = context.project
        time.sleep(5)
    context.dataset_count = 0

    if 'bot.create' in context.feature.tags:
        if hasattr(context.feature, 'bot_user'):
            context.bot_user = context.feature.bot_user
        else:
            bot_name = 'test_bot_{}'.format(random.randrange(1000, 10000))
            context.bot = context.project.bots.create(name=bot_name)
            context.feature.bot = context.bot
            context.bot_user = context.bot.email
            context.feature.bot_user = context.bot_user


@behave.Given(u'There is a dataset by the name of "{dataset_name}')
def step_impl(context, dataset_name):
    if not hasattr(context, 'num'):
        context.num = random.randint(10000, 100000)

    if hasattr(context.feature, 'dataloop_feature_dataset'):
        context.dataset = context.feature.dataloop_feature_dataset
    else:
        num = random.randint(10000, 100000)
        dataset_name = 'to-delete-test-{}_{}'.format(str(num), dataset_name)
        context.dataset = context.project.datasets.create(dataset_name=dataset_name)
        context.feature.dataloop_feature_dataset = context.dataset
        time.sleep(5)


@behave.given(u'There are "{item_count}" items')
def step_impl(context, item_count):
    filepath = "images/hamster.jpg"
    filepath = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], filepath)

    filename = 'file'
    counter = 0
    while counter < int(item_count):
        uploaded_filename = filename + str(counter) + '.jpg'
        import io
        with open(filepath, 'rb') as f:
            buffer = io.BytesIO(f.read())
            buffer.name = uploaded_filename
        context.dataset.items.upload(
            local_path=buffer,
            remote_path=None
        )
        counter += 1


@behave.when(u'I wait "{seconds}"')
def step_impl(_, seconds):
    time.sleep(int(seconds))


@behave.when(u'convert "{date}" to timestamp')
def step_impl(context, date):
    """context.timestamp Will hold the dates in a list"""
    if date == "today":
        context.timestamp.append(datetime.datetime.now().replace(microsecond=0).isoformat())
    elif date == "yesterday":
        context.timestamp.append(
            (datetime.datetime.now() - datetime.timedelta(days=1)).replace(microsecond=0).isoformat())
    elif date == "tomorrow":
        context.timestamp.append(
            (datetime.datetime.now() + datetime.timedelta(days=1)).replace(microsecond=0).isoformat())
    else:
        assert False, "Please provide one of the options : today , yesterday, tomorrow"
