from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app,db
from flask_blog.models.entries import Entry

@app.route('/') #()内のアドレスにアクセスした際に、以下の指示を実行する。
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entriesdata=Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html',entriesHTML=entriesdata) #HTMLで読み込むentries

@app.route('/entries/new',methods=['GET']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')

@app.route('/entries',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が生成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>',methods=['GET']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry.query.get(id)
    return render_template('entries/show.html',entry=entry)

@app.route('/entries/<int:id>/edit',methods=['GET']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry.query.get(id)
    return render_template('entries/edit.html',entry=entry)

@app.route('/entries/<int:id>/update',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry.query.get(id)
    entry.title=request.form['title']
    entry.text=request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def delete_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))