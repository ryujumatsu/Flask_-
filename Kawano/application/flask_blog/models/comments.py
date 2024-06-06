from flask_blog import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'
    entryid = db.Column(db.Integer, primary_key = True, autoincrement=False)
    cid = db.Column(db.Integer, primary_key=True, autoincrement=False)
        # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self,entryid=None,cid=None,text= None):
        self.entryid = entryid
        self.cid = cid
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return'<Entry entryid:{} cid:{} text:{}>'.format(self.entryid,self.cid,self.text)