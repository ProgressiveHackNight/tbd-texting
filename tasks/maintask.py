# encoding=utf8
from django.core.management import call_command

def run_pull_data():
    print('RUN] Running Scheduled work: Pull Data');
    call_command('pull_data')

def run_send_confirmation():
    print('RUN] Running Scheduled work: Pull Data');
    call_command('send_confirmation')
