from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    status = db.Column(db.String(10))
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None,status=None):
        self.title = title
        self.text = text
        self.status = status
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} text:{} status:{}>'.format(self.id, self.title, self.text, self.status)