from flask import request,redirect,url_for,render_template,flash,session
from netflask import app
from functools import wraps

def user_login_required(view):#ユーザーログイン識別
    @wraps(view)
    def inner(*args,**kwargs):
        if not session.get('user_logged_in'):
            return redirect(url_for('login'))
        return view(*args,**kwargs)
    return inner

def editor_login_required(view):#編集者ログイン識別
    @wraps(view)
    def inner(*args,**kwargs):
        if not session.get('editor_logged_in'):
            return redirect(url_for('login'))
        return view(*args,**kwargs)
    return inner

@app.route('/login',methods=['GET','POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def login():
    if request.method=='POST':
        if request.form['username']==app.config['USERNAME'] and request.form['password']==app.config['USERPASSWORD']:
            session['user_logged_in']=True
            flash('ログインしました')
            return redirect(url_for('user_movies'))
        if request.form['username']==app.config['EDITORNAME'] and request.form['password']==app.config['EDITORPASSWORD']:
            session['editor_logged_in']=True
            flash('ログインしました')
            return redirect(url_for('edit_movies'))
        else:
            flash('ユーザー名またはパスワードが異なります')
    return render_template('login.html')

@app.route('/logout') #()内のアドレスにアクセスした際に、以下の指示を実行する。
def logout():
    session.pop('user_logged_in',None)
    session.pop('editor_logged_in',None)
    session
    flash('ログアウトしました')
    return redirect(url_for('login'))

