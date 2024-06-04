from flask_script import Command

from flask_blog import db
from flask_blog.models.posts import Post
from flask_blog.models.users import User


class InitDB(Command):
    "create databse"

    def run(self):
        db.create_all()
