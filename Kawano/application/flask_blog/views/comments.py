from flask import request,redirect,url_for,render_template,flash,session
#__init__.pyで作成したappをインポート
from flask_blog import app
from flask_blog.models.comments import Comment
from flask_blog.models.entries import Entry
from flask_blog import db
from sqlalchemy.sql import func
#URLアクセスがあったときの処理
@app.route('/comments/<int:id>/new',methods=['GET'])
def new_comment(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('comments/new.html', id=id, entry=entry)

@app.route('/comments/<int:id>', methods=['POST'])
def add_comment(id):
    #ログイン処理
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    #現在のコメント数抽出
    cid = int(db.session.query(func.max(Comment.cid)).first()) + 1
    #コメント追加処理
    comment = Comment(
        entryid = id,
        cid =  cid,
        text = request.form['ctext']
    )
    db.session.add(comment)
    db.session.commit()
    flash("新しいコメントが追加されました")
    return redirect(url_for('show_entry',  id=id))

@app.route('/comments/<int:id>/<int:cid>/edit',methods=['GET'])
def edit_comment(id, cid):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entryid = id
    cid = cid
    comment = db.session.query(Comment).filter(Comment.entryid==id, Comment.cid==cid).first()
    return render_template('comments/edit.html', comment=comment, entry=entry, entryid=entryid, cid=cid)

@app.route('/entries/<int:id>/<int:cid>/update',methods=['POST'])
def update_comment(id, cid):
    if not session.get('logged_in'):
        return  redirect(url_for('login'))
    comment = Comment.query.filter(Comment.entryid==id and Comment.cid==cid).first()
    comment.text = request.form['ctext']
    db.session.merge(comment)
    db.session.commit()
    flash('コメントが編集されました')
    return redirect(url_for('show_entry', id=id))

@app.route('/entries/<int:id>/<int:cid>/delete',methods=['POST'])
def delete_comment(id, cid):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    comment = Comment.query.filter(Comment.entryid==id and Comment.cid==cid).first()
    db.session.delete(comment)
    db.session.commit()
    flash('コメントが削除されました')
    return redirect(url_for('show_entry', id=id))