from flask import request,redirect,url_for,render_template,flash,request,session
from holiday import app

@app.route('/') #()内のアドレスにアクセスした際に、以下の指示を実行する。
def input():
    return render_template('input.html')
