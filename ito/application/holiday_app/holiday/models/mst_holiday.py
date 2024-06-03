from holiday import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column('holi_date', db.DateTime, primary_key = True)
    holi_text = db.Column('holi_text', db.String(20))

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text
        # self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Holiday holi_date:{} holi_text:{}>'.format(self.holi_date, self.holi_text)

# class Entry(db.Model):
#     __tablename__ = 'entries'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), unique=True)
#     text = db.Column(db.Text)
#     created_at = db.Column(db.DateTime)

#     def __init__(self, title=None, text=None):
#         self.title = title
#         self.text = text
#         self.created_at = datetime.utcnow()

#     def __repr__(self):
#         return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)