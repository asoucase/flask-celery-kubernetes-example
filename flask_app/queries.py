from datetime import datetime
from uuid import uuid4
from pony import orm


def get_all_jobs(db):
    with orm.db_session:
        return orm.select(j for j in db.JobQueue)[:]


def add_job(db, task):
    with orm.db_session:
        job_uuid = uuid4()
        db.JobQueue(uuid=job_uuid, task=task, created=datetime.now())
        return job_uuid


def get_job(db, job_uuid):
    with orm.db_session:
        return db.JobQueue.get(uuid=job_uuid)


def set_job_started(db, job_uuid):
    with orm.db_session:
        j = db.JobQueue.get(uuid=job_uuid)
        j.started = datetime.now()


def set_job_completed(db, job_uuid):
    with orm.db_session:
        j = db.JobQueue.get(uuid=job_uuid)
        j.completed = datetime.now()


def set_job_result(db, job_uuid, result):
    with orm.db_session:
        j = db.JobQueue.get(uuid=job_uuid)
        j.result = result
