# encoding=utf8

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import maintask
import time
from rq import Queue
from worker import conn

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=6)
def timed_for_task():
    q = Queue(connection=conn)
    result = q.enqueue(maintask.run_pull_data, timeout=500)

    time.sleep(180)

    result2  = q.enqueue(maintask.run_send_confirmation, timeout=500)


@sched.scheduled_job('interval', minutes=60)
def timed_for_task():
    q = Queue(connection=conn)
    result = q.enqueue(maintask.run_send_reminder, timeout=1000)


sched.start()
