from flask_wtf import Form
from wtforms import TextField


class Paper(Form):
    text = TextField('paper')
