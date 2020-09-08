import json
import os
from celery import Celery
from flask_app import queries
from flask_app.model import get_db

rbmq_user = os.environ.get('RABBITMQ_USER')  # guest
rbmq_host = os.environ.get('RABBITMQ_HOST')  # rabbitmq
celery = Celery('tasks', broker=f'pyamqp://{rbmq_user}@{rbmq_host}//')


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


@celery.task
def fib_job(job_uuid):
    db = get_db()
    queries.set_job_started(db, job_uuid)
    job = queries.get_job(db, job_uuid)
    payload = json.loads(job.task)
    ans = fib(payload['n'])
    queries.set_job_completed(db, job_uuid)
    queries.set_job_result(db, job_uuid, str(ans))


