from holiday import db
from holiday.models.holiday import Holiday
from flask_script import Command

class InitDB(Command):
    "create databse"

    def run(self):
        db.create_all()
