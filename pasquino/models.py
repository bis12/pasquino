from pasquino.app import db


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<Message {}: {}>'.format(self.id, self.text)
