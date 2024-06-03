from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('netflask.config') #コンフィグの有効化

db=SQLAlchemy(app)

from netflask.views import views, entries

