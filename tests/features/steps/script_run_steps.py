import behave
import subprocess
import os
import time


@behave.when(u"I run script {filepath}")
def step_impl(context, filepath):
    rel_path = os.environ['DATALOOP_TEST_ASSETS']

    # fix params
    for column in context.table.headings:
        index = context.table.get_column_index(column_name=column)
        column = column.replace("<random>", context.random)
        column = column.replace("<rel_path>", rel_path)
        context.table.headings[index] = column

    # set cmds
    cmds = ['python', filepath]
    cmds += context.table.headings

    # run shell command
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    context.out, context.err = p.communicate()

    # save return code
    context.return_code = p.returncode

    # debug
    if context.return_code != 0:
        if context.err is not None:
            print(context.err.decode('utf-8'))
        if context.out is not None:
            print(context.out.decode('utf-8'))


@behave.then(u"I succeed")
def step_impl(context):
    assert context.return_code == 0
