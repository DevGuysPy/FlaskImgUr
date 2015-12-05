# import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "postgresql://flask_tutor_user:flasktutorrr@localhost/flask_tutor"
db = SQLAlchemy(app)
# basedir = os.path.abspath(os.path.dirname(__file__))


from main import models, views
