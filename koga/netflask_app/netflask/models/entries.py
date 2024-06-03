from netflask import db

class Movie(db.Model):
    __tablename__='movies'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),unique=True)
    text=db.Column(db.Text)
    limit_date=db.Column(db.DateTime)
    def __init__(self,title=None,text=None,limit_date=None):
        self.title=title
        self.text=text
        self.limit_date=limit_date

    def __repr__(self):
        return '<Movie id:{} title:{} text:{} limit_date:{}>'.format(self.id,self.title,self.text,self.limit_date)

class Mylist(db.Model):
    __tablename__='mylist'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),unique=True)
    text=db.Column(db.Text)
    limit_date=db.Column(db.DateTime)
    def __init__(self,title=None,text=None,limit_date=None):
        self.title=title
        self.text=text
        self.limit_date=limit_date

    def __repr__(self):
        return '<Movie id:{} title:{} text:{} limit_date:{}>'.format(self.id,self.title,self.text,self.limit_date)
