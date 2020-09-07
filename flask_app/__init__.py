import json
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_app.model import get_db
from flask_app.queries import get_all_jobs, add_job
from flask_app.tasks import fib_job

app = Flask(__name__)
app.secret_key = 'the random string that is not very random...'

# Connect to Postgres
db = get_db()


@app.route('/')
def index():
    t = get_all_jobs(db)
    return render_template('index.html', tasks=t)


@app.route('/add', methods=['POST'])
def add():
    n = request.form.get('n', type=int, default=0)
    if n > 0:
        # add task to jobqueue in db
        task = json.dumps({'n': n})
        job_uuid = add_job(db, task)
        # add celery task
        fib_job.delay(job_uuid)
        # notify user
        flash("job added to queue")
    return redirect(url_for('index'))
