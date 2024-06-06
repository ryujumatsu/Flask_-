from flask import request,redirect,url_for,render_template,flash,session
#__init__.pyで作成したappをインポート
from flask_blog import app
from flask_blog.models.comments import Comment
from flask_blog.models.entries import Entry
from flask_blog import db

cid = db.session.query(Comment).get(id).count() + 1
print(cid)