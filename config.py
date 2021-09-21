<<<<<<< HEAD
DB_USERNAME = 'postgres'
DB_PASSWORD = 'postgres'
port = 5432
db_name = "app_record"
=======
username = "postgres"
password = "postgres"
port = 5432
db_name = "app_record_ml"
>>>>>>> ae353a3266f7477841f64c68a9f0714f446e3c70

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False