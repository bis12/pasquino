import os

import flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from pasquino import forms


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'TODO:replacethissoon'

db = SQLAlchemy(app)
from pasquino import models

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/<square>', methods=('GET', 'POST'))
def square(square):
    form = forms.Paper()
    if form.validate_on_submit():
        db.session.add(models.Message(form.text.data))
        db.session.commit()
        flask.flash('Feel free to write again.')
    msg = db.session.query(models.Message).order_by(models.Message.id.desc()).first().text
    return flask.render_template('square.html', square=square, msg=msg, form=form)


@app.route('/')
def index():
    return flask.render_template('index.html', square='')

if __name__ == '__main__':
    manager.run()
