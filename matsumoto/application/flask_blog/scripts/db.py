from flask_blog import db
from flask_blog.models.entries import Entry
from flask_script import Command

class InitDB(Command):
    "create databse"

    def run(self):
        db.create_all()
