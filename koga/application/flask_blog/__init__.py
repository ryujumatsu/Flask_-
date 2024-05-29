from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('flask_blog.config') #コンフィグの有効化

db=SQLAlchemy(app)

import flask_blog.views

