from datetime import datetime
import os
from uuid import UUID
from pony.orm import Database, PrimaryKey, Required, Optional


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
    db.bind(provider='postgres',
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            host=os.environ.get('POSTGRES_HOST'),
            database=os.environ.get('POSTGRES_DB'))
    db.generate_mapping(create_tables=True, check_tables=True)
    return db
