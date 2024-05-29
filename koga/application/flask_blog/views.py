from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app

@app.route('/') #()内のアドレスにアクセスした際に、以下の指示を実行する。
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')


@app.route('/login',methods=['GET','POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def login():
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['password']!=app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in']=True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout') #()内のアドレスにアクセスした際に、以下の指示を実行する。
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))