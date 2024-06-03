from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('holiday.config')

# import holiday.view
# from holiday.views import input,list

db = SQLAlchemy(app)

# import holiday.views.input
# import holiday.views.list

from holiday.views import input,list,maintenance_date
