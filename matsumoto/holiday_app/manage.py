from holiday import app
from holiday.scripts.db import InitDB
from flask_script import Manager


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db", InitDB())
    manager.run()
