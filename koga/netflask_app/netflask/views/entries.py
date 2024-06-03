from flask import request,redirect,url_for,render_template,flash,session
from netflask import app,db
from netflask.models.entries import Movie,Mylist
from netflask.views.views import user_login_required,editor_login_required

@app.route('/') #()内のアドレスにアクセスした際に、以下の指示を実行する。
@user_login_required
def user_movies():#一覧表示ページ(ユーザー)
    entriesdata=Movie.query.order_by(Movie.id.desc()).all()
    return render_template('entries/user_index.html',entriesHTML=entriesdata)

@app.route('/') #()内のアドレスにアクセスした際に、以下の指示を実行する。
@editor_login_required
def edit_movies():#一覧表示ページ(編集者)
    entriesdata=Movie.query.order_by(Movie.id.desc()).all()
    return render_template('entries/editor_index.html',entriesHTML=entriesdata) 

@app.route('/entries/editor_add_movie',methods=['GET']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
@editor_login_required
def editor_new():#作品追加ページ(編集者)
    return render_template('entries/editor_add_movie.html')

@app.route('/entries',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
@editor_login_required
def add_movie():#作品追加,DB反映
    movie=Movie(
        title=request.form['title'],
        text=request.form['text'],
        limit=request.form['limit']
    )
    db.session.add(movie)
    db.session.commit()
    flash('新しい作品を追加ました')
    return redirect(url_for('entries/editor_index.html'))

@app.route('/entries/<int:id>',methods=['GET']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
@editor_login_required
def editor_movie(id):# 作品情報更新後の処理(編集者)
    movie=Movie.query.get(id)
    return render_template('entries/show.html',entry=movie)

@app.route('/entries/<int:id>/editor_update',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
@editor_login_required
def update_entry(id):# 作品情報更新の処理(編集者)
    entry=Movie.query.get(id)
    entry.title=request.form['title']
    entry.text=request.form['text']
    entry=request.form['limit']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/editor_delete',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
@editor_login_required
def delete_movie(id):
    entry=Movie.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('作品が削除されました')
    return redirect(url_for('edit_movies'))

@app.route('/entries/user_mylist') #()内のアドレスにアクセスした際に、以下の指示を実行する。
@user_login_required
def user_mylist():#一覧表示ページ(ユーザー)
    entriesdata=Mylist.query.order_by(Mylist.id.desc()).all()
    return render_template('entries/user_mylist.html',entriesHTML=entriesdata) #HTMLで読み込むentries
