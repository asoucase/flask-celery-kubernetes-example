from datetime import datetime
from uuid import UUID, uuid4
from pony.orm import *


def get_model():
    db = Database()

    class JobQueue(db.Entity):
        id = PrimaryKey(int, auto=True)
        uuid = Required(UUID)
        task = Required(str)
        created = Required(datetime)
        started = Optional(datetime)
        completed = Optional(datetime)
        result = Optional(str)

    return db


def get_db():
    # Connect to Postgres
    db = get_model()
    db.bind(provider='postgres', user='demo', password='pass', host='db', database='demo')
    db.generate_mapping(create_tables=True, check_tables=True)
    return db