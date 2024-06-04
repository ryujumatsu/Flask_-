from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from flask_blog import db


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
    title = db.Column(db.String(50))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    user = relationship("User")

    def __init__(self, user_id=None, title=None, text=None):
        self.user_id = user_id
        self.title = title
        self.text = text
        self.created_at = datetime.now()
    

    def __repr__(self):
        return "<Post id:{} user_id: {} title:{} text:{}>".format(self.id, self.user_id, self.title, self.text)
