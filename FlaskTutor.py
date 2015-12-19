#!/usr/bin/env python

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from app import app, db

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

if __name__ == '__main__':
    # db.create_all()
    manager.run()
    # app.run()

