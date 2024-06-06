from flask_script import Command
from flask_blog import db
# from flask_blog.models.entries import Entry
from flask_blog.models.comments import Comment

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()