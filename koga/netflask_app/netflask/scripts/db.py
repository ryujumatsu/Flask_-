from flask_script import Command
from netflask import db
from netflask.models.entries import Movie,Mylist

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()