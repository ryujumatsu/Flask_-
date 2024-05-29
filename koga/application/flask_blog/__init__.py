from flask import Flask

app=Flask(__name__)
app.config.from_object('flask_blog.config') #コンフィグの有効化

import flask_blog.views

