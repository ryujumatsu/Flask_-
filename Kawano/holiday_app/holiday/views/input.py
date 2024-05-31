from flask import request,redirect,url_for,render_template,flash,session
#__init__.pyで作成したappをインポート
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db
#URLアクセスがあったときの処理
@app.route('/')##http
def input():
    return render_template('input.html')
