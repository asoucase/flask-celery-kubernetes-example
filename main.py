import time
from flask_app import app

while True:
    try:
        app.run(host='0.0.0.0', port=5000)
    except:
        time.sleep(1)
