from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config.from_object('holiday.config') #コンフィグの有効化
db = SQLAlchemy(app)

from holiday.views import input,list,result,maintenance_holiday
