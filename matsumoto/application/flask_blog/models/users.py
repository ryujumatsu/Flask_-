from sqlalchemy.orm import relationship

from flask_blog import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    password = db.Column(db.Text)


    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
    
    
    def __repr__(self):
        return f"<User id:{self.id} name:{self.name} password:{self.password}>"
