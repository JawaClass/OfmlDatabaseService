from flask import Flask
from Service import create_app
# from settings import Config
import os

os.environ["FLASK_DEBUG"] = "1"
 # TEST windows
if os.name == "nt":
    os.environ["W2_FS1_DRIVE_EDV"] = r"\\w2_fs1\edv"
    os.environ["W2_FS1_DRIVE_KNPS_TESTUMGEBUNG"] = r"\\w2_fs1\edv\knps-testumgebung"

# gunicorn -w 2 'wsgi:app'
app = create_app()
celery_app = app.extensions["celery"]

if __name__ == '__main__':
    Flask.run(app, debug=True, port=5000, host='0.0.0.0')
