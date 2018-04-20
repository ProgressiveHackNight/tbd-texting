# encoding=utf8
from django.core.management import call_command
from subprocess import call


def run_pull_data():
    print('RUN] Running Scheduled work: Pull Data');
    call(["python", "manage.py", "pull_data"])


def run_send_confirmation():
    print('RUN] Running Scheduled work: Pull Data');
    # call_command('send_confirmation', interactive=False)
    call(["python", "manage.py", "send_confirmation"])
